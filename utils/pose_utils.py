"""
utils/pose_utils.py
Pose detection, skeleton tracking, and push-up analysis utilities.
Updated for MediaPipe 0.10.30+ using the new Tasks API.
"""

import cv2
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import urllib.request
import os
from pathlib import Path


# ============================================================
# Download model if not exists
# ============================================================
def download_pose_model():
    """Download the pose landmarker model if not present."""
    model_path = Path(__file__).parent / "pose_landmarker_lite.task"
    if not model_path.exists():
        print("Downloading pose landmarker model...")
        url = "https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_lite/float16/1/pose_landmarker_lite.task"
        urllib.request.urlretrieve(url, str(model_path))
        print("Model downloaded successfully!")
    return str(model_path)


# ============================================================
# PoseDetector: wraps MediaPipe PoseLandmarker (new Tasks API)
# ============================================================

class PoseDetector:
    # Landmark indices matching the old API
    POSE_LANDMARKS = {
        'LEFT_SHOULDER': 11,
        'RIGHT_SHOULDER': 12,
        'LEFT_ELBOW': 13,
        'RIGHT_ELBOW': 14,
        'LEFT_WRIST': 15,
        'RIGHT_WRIST': 16,
        'LEFT_HIP': 23,
        'RIGHT_HIP': 24,
        'LEFT_KNEE': 25,
        'RIGHT_KNEE': 26,
    }
    
    # Pose connections for drawing skeleton
    POSE_CONNECTIONS = [
        (11, 12), (11, 13), (13, 15), (12, 14), (14, 16),  # Arms
        (11, 23), (12, 24), (23, 24),  # Torso
        (23, 25), (25, 27), (24, 26), (26, 28),  # Legs
    ]
    
    def __init__(self, model_complexity=1, detection_confidence=0.4, tracking_confidence=0.4):
        """Wrapper around MediaPipe PoseLandmarker (new Tasks API).

        model_complexity: ignored in new API (using lite model)
        detection_confidence: minimum initial detection confidence
        tracking_confidence: minimum tracking confidence for subsequent frames
        """
        model_path = download_pose_model()
        
        base_options = python.BaseOptions(model_asset_path=model_path)
        options = vision.PoseLandmarkerOptions(
            base_options=base_options,
            output_segmentation_masks=False,
            min_pose_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence,
            num_poses=1
        )
        self.detector = vision.PoseLandmarker.create_from_options(options)
        self._last_result = None

    def detect_landmarks(self, frame):
        """Detect human pose landmarks in a given BGR frame."""
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
        result = self.detector.detect(mp_image)
        
        # Create a wrapper object similar to old API
        class ResultWrapper:
            def __init__(self, detection_result):
                self.pose_landmarks = None
                if detection_result.pose_landmarks and len(detection_result.pose_landmarks) > 0:
                    self.pose_landmarks = detection_result.pose_landmarks[0]
                self._raw = detection_result
        
        self._last_result = ResultWrapper(result)
        return self._last_result

    def draw_skeleton(self, frame, results, color=(0, 255, 0)):
        """Draw a full-body skeleton overlay.

        color: RGB tuple for both landmarks and connections.
        """
        if not results.pose_landmarks:
            return frame
        
        landmarks = results.pose_landmarks
        h, w = frame.shape[:2]
        
        # Convert RGB color to BGR for OpenCV
        bgr = (int(color[2]), int(color[1]), int(color[0]))
        
        # Draw connections
        for start_idx, end_idx in self.POSE_CONNECTIONS:
            if start_idx < len(landmarks) and end_idx < len(landmarks):
                start = landmarks[start_idx]
                end = landmarks[end_idx]
                start_point = (int(start.x * w), int(start.y * h))
                end_point = (int(end.x * w), int(end.y * h))
                cv2.line(frame, start_point, end_point, bgr, 4)
        
        # Draw landmarks
        for landmark in landmarks:
            cx, cy = int(landmark.x * w), int(landmark.y * h)
            cv2.circle(frame, (cx, cy), 6, bgr, -1)
        
        return frame

    def get_keypoints(self, results, frame_width, frame_height):
        """Return key joint coordinates required for push-up analysis."""
        if not results.pose_landmarks:
            return None

        landmarks = results.pose_landmarks
        
        def get_point(idx):
            if idx < len(landmarks):
                lm = landmarks[idx]
                return (int(lm.x * frame_width), int(lm.y * frame_height))
            return (0, 0)
        
        keypoints = {
            'left_shoulder': get_point(self.POSE_LANDMARKS['LEFT_SHOULDER']),
            'right_shoulder': get_point(self.POSE_LANDMARKS['RIGHT_SHOULDER']),
            'left_elbow': get_point(self.POSE_LANDMARKS['LEFT_ELBOW']),
            'right_elbow': get_point(self.POSE_LANDMARKS['RIGHT_ELBOW']),
            'left_wrist': get_point(self.POSE_LANDMARKS['LEFT_WRIST']),
            'right_wrist': get_point(self.POSE_LANDMARKS['RIGHT_WRIST']),
            'left_hip': get_point(self.POSE_LANDMARKS['LEFT_HIP']),
            'right_hip': get_point(self.POSE_LANDMARKS['RIGHT_HIP']),
            'left_knee': get_point(self.POSE_LANDMARKS['LEFT_KNEE']),
            'right_knee': get_point(self.POSE_LANDMARKS['RIGHT_KNEE']),
        }
        return keypoints


# ============================================================
# Angle and Push-up Analysis
# ============================================================

def calculate_angle(a, b, c):
    """Compute the angle (in degrees) formed by points a-b-c."""
    a, b, c = np.array(a), np.array(b), np.array(c)
    ba, bc = a - b, c - b
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc) + 1e-6)
    angle = np.degrees(np.arccos(np.clip(cosine_angle, -1.0, 1.0)))
    return angle


class PushUpAnalyzer:
    """Analyzes push-up motion with smoothing, hysteresis, and form checks."""

    def __init__(
        self,
        elbow_down_threshold: float = 85.0,
        elbow_up_threshold: float = 165.0,
        back_tolerance: float = 18.0,
        smoothing_alpha: float = 0.25,
        cooldown_frames: int = 6,
    ):
        # thresholds
        self.elbow_down_threshold = float(elbow_down_threshold)
        self.elbow_up_threshold = float(elbow_up_threshold)
        self.back_tolerance = float(back_tolerance)
        # smoothing (EMA)
        self.alpha = float(np.clip(smoothing_alpha, 0.0, 1.0))
        self.filtered_elbow = None
        # state
        self.stage = "Up"
        self.bottom_reached = False
        self.total_reps = 0
        self.form_state = "Neutral"
        self.cooldown_frames = int(max(0, cooldown_frames))
        self._cooldown = 0

    def set_params(self, elbow_down_threshold=None, elbow_up_threshold=None, back_tolerance=None, smoothing_alpha=None, cooldown_frames=None):
        if elbow_down_threshold is not None:
            self.elbow_down_threshold = float(elbow_down_threshold)
        if elbow_up_threshold is not None:
            self.elbow_up_threshold = float(elbow_up_threshold)
        if back_tolerance is not None:
            self.back_tolerance = float(back_tolerance)
        if smoothing_alpha is not None:
            self.alpha = float(np.clip(smoothing_alpha, 0.0, 1.0))
        if cooldown_frames is not None:
            self.cooldown_frames = int(max(0, cooldown_frames))

    def reset(self):
        """Reset all counters and state to initial values"""
        self.filtered_elbow = None
        self.stage = "Up"
        self.bottom_reached = False
        self.total_reps = 0
        self.form_state = "Neutral"
        self._cooldown = 0

    def _ema(self, value: float) -> float:
        if self.filtered_elbow is None:
            self.filtered_elbow = value
            return value
        self.filtered_elbow = self.alpha * value + (1.0 - self.alpha) * self.filtered_elbow
        return self.filtered_elbow

    def analyze_pose(self, keypoints):
        """Analyze push-up form, stage, rep counting, and progress.

        Returns dict with: stage, total_reps, form_state, elbow_angle, back_angle, progress
        """
        if keypoints is None:
            # No person detected in frame
            return {
                "stage": self.stage,
                "total_reps": self.total_reps,
                "form_state": "Neutral",
                "elbow_angle": None,
                "back_angle": None,
                "progress": 0.0,
            }

        # Calculate elbow and hip angles (both sides)
        left_elbow = calculate_angle(keypoints['left_shoulder'], keypoints['left_elbow'], keypoints['left_wrist'])
        right_elbow = calculate_angle(keypoints['right_shoulder'], keypoints['right_elbow'], keypoints['right_wrist'])
        left_hip = calculate_angle(keypoints['left_shoulder'], keypoints['left_hip'], keypoints['left_knee'])
        right_hip = calculate_angle(keypoints['right_shoulder'], keypoints['right_hip'], keypoints['right_knee'])

        # Use the minimum elbow angle to ensure both arms bend adequately
        raw_elbow = float(min(left_elbow, right_elbow))
        elbow_angle = self._ema(raw_elbow)
        back_angle = float(np.mean([left_hip, right_hip]))

        # Calculate body orientation to detect actual push-up position
        shoulder_y = (keypoints['left_shoulder'][1] + keypoints['right_shoulder'][1]) / 2
        hip_y = (keypoints['left_hip'][1] + keypoints['right_hip'][1]) / 2
        wrist_y = (keypoints['left_wrist'][1] + keypoints['right_wrist'][1]) / 2
        knee_y = (keypoints['left_knee'][1] + keypoints['right_knee'][1]) / 2
        
        body_horizontal = abs(shoulder_y - hip_y) < 100
        hands_on_ground = wrist_y > shoulder_y + 50
        legs_extended = knee_y >= hip_y - 50
        plank_back_angle = 155 <= back_angle <= 200
        elbow_in_range = 60 <= elbow_angle <= 180
        
        in_pushup_position = (
            body_horizontal and 
            hands_on_ground and 
            legs_extended and 
            plank_back_angle and 
            elbow_in_range
        )
        
        # Form check: keep back fairly straight (close to 180)
        good_back = abs(180.0 - back_angle) <= self.back_tolerance
        
        # Only show Correct/Wrong when in actual push-up position
        if in_pushup_position:
            self.form_state = "Correct" if good_back else "Wrong"
        else:
            self.form_state = "Neutral"

        # Progress (0 at top, 1 at/below bottom)
        denom = max(1.0, (self.elbow_up_threshold - self.elbow_down_threshold))
        progress = np.clip((self.elbow_up_threshold - elbow_angle) / denom, 0.0, 1.0)

        # Rep state machine with hysteresis + cooldown
        if self._cooldown > 0:
            self._cooldown -= 1

        mid_threshold = (self.elbow_down_threshold + self.elbow_up_threshold) / 2
        
        if not in_pushup_position:
            if self.stage not in ["Up", "Down"]:
                self.stage = "Up"
        else:
            if elbow_angle <= self.elbow_down_threshold and good_back:
                self.bottom_reached = True
                self.stage = "Down"
            elif (
                self.bottom_reached
                and elbow_angle >= self.elbow_up_threshold
                and good_back
                and self._cooldown == 0
            ):
                self.stage = "Up"
                self.total_reps += 1
                self.bottom_reached = False
                self._cooldown = self.cooldown_frames
            elif elbow_angle <= mid_threshold:
                self.stage = "Down"
            elif elbow_angle >= self.elbow_up_threshold - 10:
                self.stage = "Up"

        return {
            "stage": self.stage,
            "total_reps": self.total_reps,
            "form_state": self.form_state,
            "elbow_angle": round(float(elbow_angle), 1),
            "back_angle": round(float(back_angle), 1),
            "progress": float(progress),
            "debug": {
                "left_elbow": round(float(left_elbow), 1),
                "right_elbow": round(float(right_elbow), 1),
                "left_hip": round(float(left_hip), 1),
                "right_hip": round(float(right_hip), 1),
            },
        }