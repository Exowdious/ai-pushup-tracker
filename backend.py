"""
FastAPI Backend for AI Push-Up Tracker
Provides REST API endpoints and video streaming with pose detection
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import cv2
import numpy as np
import json
import asyncio
from typing import Optional
import base64
from utils.pose_utils import PoseDetector, PushUpAnalyzer
from utils.audio_manager import AudioManager

# ----------------------- CONFIGURATION -----------------------
MODEL_COMPLEXITY = 0
MIN_DETECTION_CONF = 0.5
TRACKING_CONF = 0.5
ELBOW_DOWN_THRESHOLD = 90
ELBOW_UP_THRESHOLD = 160
BACK_TOLERANCE = 25
SMOOTHING_ALPHA = 0.3
COOLDOWN_FRAMES = 15

# ----------------------- FASTAPI SETUP -----------------------
app = FastAPI(title="AI Push-Up Tracker API")

# CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development flexibility
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------- GLOBAL STATE -----------------------
class AppState:
    def __init__(self):
        self.camera = None
        self.running = False
        self.pose_detector = PoseDetector(MODEL_COMPLEXITY, MIN_DETECTION_CONF, TRACKING_CONF)
        self.analyzer = PushUpAnalyzer(
            elbow_down_threshold=ELBOW_DOWN_THRESHOLD,
            elbow_up_threshold=ELBOW_UP_THRESHOLD,
            back_tolerance=BACK_TOLERANCE,
            smoothing_alpha=SMOOTHING_ALPHA,
            cooldown_frames=COOLDOWN_FRAMES,
        )
        self.audio_manager = AudioManager("assets/beep.wav", "assets/chime.wav")
        self.last_form = "Neutral"
        self.stats = {
            "total_reps": 0,
            "form_state": "Neutral",
            "stage": "Up"
        }

state = AppState()

# ----------------------- API ENDPOINTS -----------------------

@app.get("/")
async def root():
    return {"message": "AI Push-Up Tracker API", "status": "running"}

@app.post("/camera/start")
async def start_camera():
    """Start the camera capture"""
    if not state.running:
        state.camera = cv2.VideoCapture(0)
        if not state.camera.isOpened():
            state.camera = None
            return {"status": "error", "message": "Could not access camera. Check permissions."}
        
        state.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        state.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        state.camera.set(cv2.CAP_PROP_FPS, 30)
        state.running = True
        return {"status": "started", "message": "Camera started successfully"}
    return {"status": "already_running", "message": "Camera is already running"}

@app.post("/camera/stop")
async def stop_camera():
    """Stop the camera capture"""
    if state.running:
        state.running = False
        if state.camera:
            state.camera.release()
            state.camera = None
        return {"status": "stopped", "message": "Camera stopped successfully"}
    return {"status": "not_running", "message": "Camera is not running"}

@app.post("/reset")
async def reset_stats():
    """Reset rep counter and stats"""
    state.analyzer.reset()
    state.audio_manager.reset()  # Reset audio state
    state.stats = {
        "total_reps": 0,
        "form_state": "Neutral",
        "stage": "Up"
    }
    state.last_form = "Neutral"
    return {"status": "reset", "message": "Stats reset successfully", "stats": state.stats}

@app.get("/stats")
async def get_stats():
    """Get current statistics"""
    return state.stats

# ----------------------- VIDEO STREAMING -----------------------

def generate_frames():
    """Generate video frames with pose detection"""
    while state.running:
        if state.camera is None or not state.camera.isOpened():
            break
            
        ret, frame = state.camera.read()
        if not ret:
            continue

        # Pose detection
        results = state.pose_detector.detect_landmarks(frame)
        
        if results.pose_landmarks:
            h, w = frame.shape[:2]
            keypoints = state.pose_detector.get_keypoints(results, w, h)
            analysis = state.analyzer.analyze_pose(keypoints)
            
            # Update stats
            state.stats.update({
                'total_reps': analysis.get("total_reps", 0),
                'form_state': analysis.get("form_state", "Neutral"),
                'stage': analysis.get("stage", "Up")
            })

            # Audio feedback
            form = analysis.get("form_state", "Neutral")
            if form != state.last_form:
                if form == "Wrong":
                    state.audio_manager.play_beep("Wrong")
                elif form == "Correct":
                    state.audio_manager.play_chime("Correct")
                state.last_form = form

            # Draw skeleton with form-based color
            color = (0, 255, 0) if form == "Correct" else (255, 0, 0)
            frame = state.pose_detector.draw_skeleton(frame, results, color=color)

        # Encode frame
        _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 85])
        frame_bytes = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.get("/video_feed")
async def video_feed():
    """Stream video with pose detection"""
    return StreamingResponse(
        generate_frames(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )

# ----------------------- WEBSOCKET FOR REAL-TIME STATS -----------------------

@app.websocket("/ws/stats")
async def websocket_stats(websocket: WebSocket):
    """WebSocket endpoint for real-time statistics updates"""
    await websocket.accept()
    try:
        while True:
            # Send current stats every 100ms
            await websocket.send_json(state.stats)
            await asyncio.sleep(0.1)
    except WebSocketDisconnect:
        print("WebSocket disconnected")

# ----------------------- RUN SERVER -----------------------
if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting AI Push-Up Tracker Backend...")
    print("📹 API: http://localhost:8000")
    print("📊 Docs: http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
