import streamlit as st
import cv2
import numpy as np
from utils.pose_utils import PoseDetector, PushUpAnalyzer
from utils.audio_manager import AudioManager

# ----------------------- PAGE CONFIG -----------------------
st.set_page_config(
    page_title="AI PUSH-UP TRACKER 💪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------------- LOAD CSS -----------------------
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ----------------------- AUDIO -----------------------
audio_manager = AudioManager("assets/beep.wav", "assets/chime.wav")

# ----------------------- SESSION STATE -----------------------
if "total_reps" not in st.session_state:
    st.session_state.total_reps = 0
if "form_state" not in st.session_state:
    st.session_state.form_state = "Neutral"
if "stage" not in st.session_state:
    st.session_state.stage = "Up"

# ----------------------- FIXED SETTINGS -----------------------
MODEL_COMPLEXITY = 0
MIN_DETECTION_CONF = 0.3
TRACKING_CONF = 0.3
ELBOW_DOWN_THRESHOLD = 80
ELBOW_UP_THRESHOLD = 165
BACK_TOLERANCE = 20
SMOOTHING_ALPHA = 0.2
COOLDOWN_FRAMES = 8

# ----------------------- VIDEO PROCESSOR (Browser client) -----------------------
import time
import threading

class CameraWorker(threading.Thread):
    """Optimized background thread for camera capture and pose detection."""

    def __init__(self, src=0):
        super().__init__()
        self.src = src
        self.cap = None
        self.running = False
        self.frame = None
        self.lock = threading.Lock()
        self.pose_detector = PoseDetector(MODEL_COMPLEXITY, MIN_DETECTION_CONF, TRACKING_CONF)
        self.analyzer = PushUpAnalyzer(
            elbow_down_threshold=ELBOW_DOWN_THRESHOLD,
            elbow_up_threshold=ELBOW_UP_THRESHOLD,
            back_tolerance=BACK_TOLERANCE,
            smoothing_alpha=SMOOTHING_ALPHA,
            cooldown_frames=COOLDOWN_FRAMES,
        )
        self.last_form = "Neutral"
        self.data = {}
        self.daemon = True

    def start_camera(self):
        if not self.running:
            self.running = True
            if not self.is_alive():
                self.start()

    def stop_camera(self):
        self.running = False

    def run(self):
        """Optimized capture loop with minimal overhead."""
        while True:
            if self.running:
                # Initialize camera once
                if self.cap is None or not self.cap.isOpened():
                    self.cap = cv2.VideoCapture(self.src)
                    self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                    self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
                    self.cap.set(cv2.CAP_PROP_FPS, 30)

                ret, img = self.cap.read()
                if not ret:
                    time.sleep(0.03)
                    continue

                # Pose detection and analysis
                results = self.pose_detector.detect_landmarks(img)
                
                if results.pose_landmarks:
                    h, w = img.shape[:2]
                    keypoints = self.pose_detector.get_keypoints(results, w, h)
                    analysis = self.analyzer.analyze_pose(keypoints)
                    
                    # Update shared data atomically
                    self.data.update({
                        'total_reps': analysis.get("total_reps", 0),
                        'form_state': analysis.get("form_state", "Neutral"),
                        'stage': analysis.get("stage", "Up")
                    })

                    # Audio feedback
                    form = analysis.get("form_state", "Neutral")
                    if form != self.last_form:
                        if form == "Wrong":
                            audio_manager.play_beep("Wrong")
                        elif form == "Correct":
                            audio_manager.play_chime("Correct")
                        self.last_form = form

                    # Draw skeleton with form-based color
                    color = (0, 255, 0) if form == "Correct" else (255, 0, 0)
                    img = self.pose_detector.draw_skeleton(img, results, color=color)

                # Convert to RGB once
                disp = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                with self.lock:
                    self.frame = disp

                time.sleep(0.02)
            else:
                # Clean up when stopped
                if self.cap is not None:
                    self.cap.release()
                    self.cap = None
                time.sleep(0.1)

# Initialize CameraWorker in session_state
if "camera_worker" not in st.session_state:
    st.session_state.camera_worker = CameraWorker(src=0)

cw = st.session_state.camera_worker

# Sync session state from shared data
for key in ['total_reps', 'form_state', 'stage']:
    st.session_state[key] = cw.data.get(key, st.session_state.get(key, 0 if key == 'total_reps' else 'Neutral' if key == 'form_state' else 'Up'))

# ----------------------- HEADER -----------------------
st.markdown('''
<div style="text-align: center; margin-bottom: 3rem;">
    <h1>💪 AI PUSH-UP TRACKER 💪</h1>
</div>
''', unsafe_allow_html=True)

# ----------------------- STATS ROW -----------------------
col1, col2, col3 = st.columns(3)

# Determine form state color class
form_class = "neo-card-correct" if st.session_state.form_state == "Correct" else \
             "neo-card-wrong" if st.session_state.form_state == "Wrong" else \
             "neo-card-neutral"

with col1:
    st.markdown(f'''
    <div class="neo-card {form_class}" style="text-align: center;">
        <h2>{st.session_state.form_state.upper()}</h2>
        <p>FORM STATUS</p>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown(f'''
    <div class="neo-card" style="text-align: center;">
        <h2>{st.session_state.total_reps}</h2>
        <p>TOTAL REPS</p>
    </div>
    ''', unsafe_allow_html=True)

with col3:
    st.markdown(f'''
    <div class="neo-card" style="text-align: center;">
        <h2>{st.session_state.stage.upper()}</h2>
        <p>STAGE</p>
    </div>
    ''', unsafe_allow_html=True)

# ----------------------- CAMERA FEED -----------------------
st.markdown('<div class="camera-container">', unsafe_allow_html=True)
st.markdown('<h3 style="text-align: center; margin-bottom: 1rem;">📹 LIVE FEED</h3>', unsafe_allow_html=True)
img_placeholder = st.empty()
st.markdown('</div>', unsafe_allow_html=True)

# ----------------------- CONTROLS -----------------------
st.markdown('<div style="margin-top: 2rem;">', unsafe_allow_html=True)
ctrl_col1, ctrl_col2, ctrl_col3 = st.columns(3)

with ctrl_col1:
    if st.button("🚀 START", key="start_btn", use_container_width=True):
        if not cw.running:
            cw.start_camera()

with ctrl_col2:
    if st.button("⏸️ STOP", key="stop_btn", use_container_width=True):
        if cw.running:
            cw.stop_camera()

with ctrl_col3:
    if st.button("🔄 RESET", key="reset_btn", use_container_width=True):
        cw.analyzer.reset()
        cw.data = {}
        st.session_state.total_reps = 0
        st.session_state.form_state = "Neutral"
        st.session_state.stage = "Up"

st.markdown('</div>', unsafe_allow_html=True)

# ----------------------- DISPLAY LOOP -----------------------
if cw.running:
    with cw.lock:
        frame = cw.frame
    if frame is not None:
        img_placeholder.image(frame, channels="RGB", use_container_width=True)
    else:
        img_placeholder.markdown(
            '<div style="text-align: center; padding: 3rem; font-size: 1.5rem;">⚡ INITIALIZING...</div>',
            unsafe_allow_html=True
        )
    time.sleep(0.05)
    st.rerun()
else:
    img_placeholder.markdown(
        '<div style="text-align: center; padding: 3rem; font-size: 1.5rem;">📷 PRESS START TO BEGIN</div>',
        unsafe_allow_html=True
    )
