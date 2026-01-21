# AI Push-Up Tracker - Complete Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Architecture](#architecture)
4. [Technology Stack](#technology-stack)
5. [Design System](#design-system)
6. [How It Works](#how-it-works)
7. [Installation & Setup](#installation--setup)
8. [API Documentation](#api-documentation)
9. [Component Structure](#component-structure)
10. [Configuration](#configuration)
11. [Troubleshooting](#troubleshooting)
12. [Development Guide](#development-guide)
13. [Performance Optimization](#performance-optimization)
14. [Future Enhancements](#future-enhancements)

---

## Project Overview

**AI Push-Up Tracker** is a real-time computer vision application that tracks push-up exercises using MediaPipe pose detection. The system provides live feedback on form correctness, counts repetitions automatically, and displays all metrics in a bold neobrutalism-themed interface.

### Key Objectives
- **Real-time pose detection** using AI/ML
- **Accurate rep counting** with form validation
- **Visual feedback** on exercise form quality
- **Modern web interface** with React frontend
- **Production-ready architecture** with separated frontend/backend

### Target Users
- Fitness enthusiasts
- Personal trainers
- Home workout practitioners
- Developers learning computer vision

---

## Features

### Core Functionality
✅ **Real-time Pose Detection**
- 33 body landmarks tracked at 30 FPS
- MediaPipe Pose estimation
- Skeletal overlay visualization

✅ **Automatic Rep Counting**
- Motion-based detection
- Hysteresis filtering to prevent false counts
- Cooldown period between reps

✅ **Form Analysis**
- Back straightness monitoring
- Elbow angle measurement
- Real-time correctness feedback

✅ **Visual Feedback**
- Green skeleton: Correct form
- Red skeleton: Incorrect form
- Live stats display

✅ **Audio Feedback**
- Beep sound: Wrong form detected
- Chime sound: Correct form achieved

### User Interface Features
✅ **Neobrutalism Design**
- Bold 4px black borders
- Chunky 8px shadows
- Vibrant color palette
- Space Grotesk typography

✅ **Real-time Updates**
- WebSocket connection for stats
- MJPEG video streaming
- Instant UI feedback

✅ **Responsive Layout**
- Desktop optimized (2:1 camera-to-stats ratio)
- Mobile compatible
- No scrolling required

✅ **Controls**
- Start/Stop camera
- Reset counter
- Status indicator

---

## Architecture

### System Design

```
┌─────────────────────────────────────────────────────────────┐
│                        USER BROWSER                         │
│                    (http://localhost:5173)                  │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │           React Frontend (Vite)                     │   │
│  │                                                     │   │
│  │  Components:                                        │   │
│  │  • App.jsx (Main container)                        │   │
│  │  • StatCard.jsx (Form/Reps/Stage display)         │   │
│  │  • CameraFeed.jsx (Video stream display)          │   │
│  │  • Controls.jsx (Start/Stop/Reset buttons)        │   │
│  │                                                     │   │
│  │  State Management:                                  │   │
│  │  • React Hooks (useState, useEffect, useRef)      │   │
│  │  • WebSocket connection for real-time stats       │   │
│  └─────────────────────────────────────────────────────┘   │
│                           │                                 │
│                           ▼                                 │
│           HTTP + WebSocket + MJPEG Stream                   │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    BACKEND SERVER                           │
│                  (http://localhost:8000)                    │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              FastAPI Application                    │   │
│  │                                                     │   │
│  │  REST Endpoints:                                    │   │
│  │  • POST /camera/start  - Start camera              │   │
│  │  • POST /camera/stop   - Stop camera               │   │
│  │  • POST /reset         - Reset counters            │   │
│  │  • GET  /stats         - Get current stats         │   │
│  │  • GET  /video_feed    - MJPEG stream              │   │
│  │                                                     │   │
│  │  WebSocket:                                         │   │
│  │  • WS /ws/stats        - Real-time stats push      │   │
│  └─────────────────────────────────────────────────────┘   │
│                           │                                 │
│                           ▼                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │           Pose Detection Pipeline                   │   │
│  │                                                     │   │
│  │  1. OpenCV Camera Capture (640x480 @ 30fps)       │   │
│  │  2. MediaPipe Pose Detection (33 landmarks)       │   │
│  │  3. Angle Calculation (elbows, hips)              │   │
│  │  4. Form Analysis (back straightness)             │   │
│  │  5. Rep State Machine (Up/Down detection)         │   │
│  │  6. Smoothing & Filtering (EMA, cooldown)         │   │
│  │  7. Skeleton Drawing (colored overlay)            │   │
│  │  8. Frame Encoding (JPEG compression)             │   │
│  └─────────────────────────────────────────────────────┘   │
│                           │                                 │
│                           ▼                                 │
│  ┌─────────────────────────────────────────────────────┐   │
│  │              Utility Modules                        │   │
│  │                                                     │   │
│  │  • PoseDetector (MediaPipe wrapper)                │   │
│  │  • PushUpAnalyzer (Rep counting logic)             │   │
│  │  • AudioManager (Sound feedback)                   │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

### Data Flow

1. **Video Input** → Camera → OpenCV → BGR frames
2. **Detection** → MediaPipe → 33 pose landmarks
3. **Analysis** → Calculate angles → Form validation → Rep counting
4. **Visualization** → Draw skeleton → JPEG encode → MJPEG stream
5. **Stats** → WebSocket → JSON → React state → UI update

### Communication Protocols

| Protocol | Purpose | Data Format | Frequency |
|----------|---------|-------------|-----------|
| **HTTP POST** | Control commands | JSON | On demand |
| **HTTP GET** | Video stream | MJPEG | 30 FPS |
| **WebSocket** | Stats updates | JSON | 10 Hz (100ms) |
| **CORS** | Cross-origin | Headers | All requests |

---

## Technology Stack

### Frontend Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| **React** | 18.2.0 | UI library for component-based architecture |
| **Vite** | 5.0.0 | Fast build tool and dev server |
| **Axios** | 1.6.0 | HTTP client for API requests |
| **CSS3** | - | Neobrutalism styling with custom properties |
| **WebSocket API** | Native | Real-time bidirectional communication |

**Why React + Vite?**
- ⚡ Lightning-fast hot module reload
- 📦 Optimized production builds
- 🎯 Modern JavaScript features (ES modules)
- 🔧 Easy configuration
- 💡 Better developer experience than Streamlit

### Backend Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| **FastAPI** | 0.104.1 | Modern async Python web framework |
| **Uvicorn** | 0.24.0 | ASGI server for FastAPI |
| **OpenCV** | 4.11.0 | Computer vision and camera capture |
| **MediaPipe** | Latest | Google's pose detection ML model |
| **NumPy** | Latest | Numerical computations for angles |
| **WebSockets** | 12.0 | Real-time communication |

**Why FastAPI?**
- 🚀 High performance (async/await)
- 📚 Automatic API documentation (Swagger)
- 🔒 Type safety with Pydantic
- 🌐 Built-in WebSocket support
- ⚡ Better than Flask for real-time apps

### AI/ML Technologies

| Technology | Model | Purpose |
|------------|-------|---------|
| **MediaPipe Pose** | BlazePose | 33-landmark full-body pose estimation |
| **TensorFlow Lite** | Backend | Optimized ML inference |
| **XNNPACK** | Delegate | CPU acceleration for neural networks |

**MediaPipe Features:**
- 🎯 Real-time inference (30+ FPS)
- 📱 Mobile-optimized
- 🌐 Cross-platform
- 🔋 Low latency
- 💪 Robust to occlusions

### Development Tools

| Tool | Purpose |
|------|---------|
| **npm** | Frontend package management |
| **pip** | Backend package management |
| **Git** | Version control |
| **VS Code** | Recommended IDE |
| **Chrome DevTools** | Frontend debugging |
| **Python Debugger** | Backend debugging |

---

## Design System

### Neobrutalism Principles

**Neobrutalism** is a web design trend characterized by:
- **Raw, unpolished aesthetics**
- **Bold, thick borders**
- **Chunky drop shadows**
- **Vibrant, contrasting colors**
- **Heavy typography**
- **No gradients or blur**
- **Honest, functional design**

### Color Palette

```css
Primary Colors:
--neo-black: #000000    /* Borders, text, shadows */
--neo-white: #FFFFFF    /* Card backgrounds */
--neo-yellow: #FFE66D   /* Page background */

Accent Colors:
--neo-pink: #FF6B9D     /* Title shadows, accents */
--neo-cyan: #00F5FF     /* Neutral state, buttons */
--neo-green: #4ADE80    /* Correct form, success */
--neo-red: #FF5757      /* Wrong form, errors */
--neo-purple: #A78BFA   /* Reset button */

Shadows:
--neo-shadow: 8px 8px 0px #000000
--neo-shadow-sm: 4px 4px 0px #000000

Borders:
--neo-border: 4px solid #000000
```

### Typography

```css
Font Family: 'Space Grotesk', monospace, sans-serif
Font Weight: 700 (Bold only)
Text Transform: UPPERCASE
Letter Spacing: 1-3px

Sizes:
- Title: 2.5rem (clamp 1.5rem - 2.5rem)
- Camera Header: 1.3rem
- Stats Value: 3rem
- Stats Label: 0.9rem
- Button: 1.1rem
- Status: 0.9rem
- Footer: 0.85rem
```

### Component Styling

**Box Model:**
```
┌─────────────────────────────────────────┐
│ ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓ │ ← 4px border
│ ┃                                   ┃ │
│ ┃          CONTENT                  ┃ │ ← Padding inside
│ ┃                                   ┃ │
│ ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ │
└─────────────────────────────────────────┘
      └─ 4-8px shadow offset
```

**Interactive States:**
```
Default:   transform: translate(0, 0)
Hover:     transform: translate(2px, 2px)
Active:    transform: translate(4px, 4px)
```

### Layout Grid

**Desktop (>968px):**
```
┌──────────────────────────────────────────────────┐
│  AI PUSH-UP TRACKER (Full Width Title)          │
├────────────────────────────┬─────────────────────┤
│ 📹 LIVE FEED               │ FORM STATUS         │
│                            │ TOTAL REPS          │
│                            │ STAGE               │
│    [Camera 2/3 width]      │ READY TO START      │
│                            │ CONTROLS            │
│                            │ © 2025 EXOWDIOUS    │
│ [Empty Footer]             │                     │
└────────────────────────────┴─────────────────────┘
        66% width                   33% width
```

**Mobile (<968px):**
```
┌────────────────────┐
│ AI PUSH-UP TRACKER │
├────────────────────┤
│ 📹 LIVE FEED       │
│  [Camera]          │
├────────────────────┤
│ FORM │ REPS │STAGE│ (Horizontal scroll)
├────────────────────┤
│ STATUS             │
├────────────────────┤
│ START│STOP│RESET  │ (Horizontal scroll)
└────────────────────┘
```

---

## How It Works

### Pose Detection Pipeline

#### 1. Camera Capture
```python
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)
ret, frame = cap.read()
```

#### 2. MediaPipe Processing
```python
# Convert BGR to RGB
rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# Process with MediaPipe
results = pose.process(rgb)

# Extract 33 landmarks
landmarks = results.pose_landmarks
```

#### 3. Angle Calculation
```python
def calculate_angle(a, b, c):
    """Calculate angle at point b formed by points a-b-c"""
    ba = a - b
    bc = c - b
    cosine = np.dot(ba, bc) / (norm(ba) * norm(bc))
    angle = np.degrees(np.arccos(clip(cosine, -1, 1)))
    return angle

# Key angles
elbow_angle = min(left_elbow, right_elbow)
back_angle = mean([left_hip, right_hip])
```

#### 4. Form Analysis
```python
# Check back straightness (should be ~180°)
good_back = abs(180 - back_angle) <= BACK_TOLERANCE

# Set form state
form_state = "Correct" if good_back else "Wrong"
```

#### 5. Rep Counting State Machine
```python
if elbow_angle <= DOWN_THRESHOLD and good_back:
    bottom_reached = True
    stage = "Down"
elif bottom_reached and elbow_angle >= UP_THRESHOLD and good_back:
    stage = "Up"
    total_reps += 1
    bottom_reached = False
    cooldown = COOLDOWN_FRAMES
```

#### 6. Smoothing & Filtering

**Exponential Moving Average (EMA):**
```python
filtered_angle = alpha * raw_angle + (1 - alpha) * filtered_angle
```

**Hysteresis:**
- Different thresholds for down (90°) and up (160°)
- Prevents oscillation at boundary

**Cooldown:**
- 15 frames (~0.5 seconds) between counts
- Prevents double-counting

#### 7. Visualization
```python
# Draw skeleton with form-based color
color = (0, 255, 0) if correct else (255, 0, 0)
mp_drawing.draw_landmarks(frame, landmarks, connections, color)
```

### State Management Flow

```
Frontend State (React):
├── isRunning: boolean
├── stats: {
│   ├── total_reps: number
│   ├── form_state: "Correct" | "Wrong" | "Neutral"
│   └── stage: "Up" | "Down"
│   }
└── wsRef: WebSocket connection

Backend State (FastAPI):
├── running: boolean
├── camera: cv2.VideoCapture
├── pose_detector: PoseDetector
├── analyzer: PushUpAnalyzer
└── stats: dict
```

### Real-time Communication

**WebSocket Flow:**
```
1. Frontend: wsRef.current = new WebSocket('ws://localhost:8000/ws/stats')
2. Backend: await websocket.accept()
3. Loop:
   - Backend: await websocket.send_json(stats)
   - Frontend: wsRef.onmessage = (event) => setStats(JSON.parse(event.data))
   - Delay: 100ms
```

**Video Streaming:**
```
1. Frontend: <img src="http://localhost:8000/video_feed" />
2. Backend: def generate_frames():
3. Loop:
   - Capture frame
   - Detect pose
   - Draw skeleton
   - Encode JPEG
   - Yield: b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame_bytes
```

---

## Installation & Setup

### Prerequisites

- **Python 3.11+**
- **Node.js 18+**
- **npm 9+**
- **Webcam** (built-in or USB)
- **macOS/Linux/Windows**

### Backend Setup

```bash
# Navigate to project directory
cd ai-pushup-tracker

# Create virtual environment (optional)
conda create -n ai_ptrack python=3.11
conda activate ai_ptrack

# Install dependencies
pip install -r requirements.txt
pip install -r backend_requirements.txt

# Start backend server
python backend.py

# Backend runs on http://localhost:8000
# API docs: http://localhost:8000/docs
```

### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev

# Frontend runs on http://localhost:5173
```

### Quick Start (Automated)

```bash
# Option 1: Single command (runs both)
./start.sh

# Option 2: Separate terminals
./start-backend.sh    # Terminal 1
./start-frontend.sh   # Terminal 2
```

### Production Build

```bash
# Build optimized frontend
cd frontend
npm run build

# Output: frontend/dist/
# Deploy dist/ to static hosting (Netlify, Vercel, etc.)
```

---

## API Documentation

### REST Endpoints

#### `GET /`
Health check endpoint.

**Response:**
```json
{
  "message": "AI Push-Up Tracker API",
  "status": "running"
}
```

#### `POST /camera/start`
Start camera capture and pose detection.

**Response:**
```json
{
  "status": "started",
  "message": "Camera started successfully"
}
```

#### `POST /camera/stop`
Stop camera capture.

**Response:**
```json
{
  "status": "stopped",
  "message": "Camera stopped successfully"
}
```

#### `POST /reset`
Reset rep counter and all statistics.

**Response:**
```json
{
  "status": "reset",
  "message": "Stats reset successfully",
  "stats": {
    "total_reps": 0,
    "form_state": "Neutral",
    "stage": "Up"
  }
}
```

#### `GET /stats`
Get current statistics snapshot.

**Response:**
```json
{
  "total_reps": 5,
  "form_state": "Correct",
  "stage": "Down"
}
```

#### `GET /video_feed`
MJPEG video stream with pose overlay.

**Response:** 
- Content-Type: `multipart/x-mixed-replace; boundary=frame`
- Continuous stream of JPEG frames

### WebSocket Endpoint

#### `WS /ws/stats`
Real-time statistics stream.

**Connection:**
```javascript
const ws = new WebSocket('ws://localhost:8000/ws/stats')
```

**Message Format:**
```json
{
  "total_reps": 5,
  "form_state": "Correct",
  "stage": "Down"
}
```

**Frequency:** Every 100ms (10 Hz)

### CORS Configuration

Allowed origins:
- `http://localhost:5173` (Vite dev server)
- `http://localhost:3000` (Create React App)

All methods and headers allowed for development.

---

## Component Structure

### Frontend File Structure

```
frontend/
├── index.html                    # HTML entry point
├── package.json                  # Dependencies & scripts
├── vite.config.js               # Vite configuration
└── src/
    ├── main.jsx                 # React entry point
    ├── App.jsx                  # Main application component
    ├── App.css                  # Neobrutalism styles
    └── components/
        ├── StatCard.jsx         # Individual stat display
        ├── CameraFeed.jsx       # Video stream component
        └── Controls.jsx         # Control buttons
```

### Component Props

**StatCard.jsx:**
```jsx
<StatCard
  title="FORM STATUS"           // string
  value={stats.form_state}      // string | number
  variant="correct"             // 'default' | 'correct' | 'wrong' | 'neutral'
/>
```

**CameraFeed.jsx:**
```jsx
<CameraFeed
  isRunning={true}              // boolean
  apiUrl="http://localhost:8000" // string
/>
```

**Controls.jsx:**
```jsx
<Controls
  isRunning={false}             // boolean
  onStart={handleStart}         // () => void
  onStop={handleStop}           // () => void
  onReset={handleReset}         // () => void
/>
```

### Backend File Structure

```
ai-pushup-tracker/
├── backend.py                   # FastAPI application
├── requirements.txt             # Pose detection dependencies
├── backend_requirements.txt     # FastAPI dependencies
├── utils/
│   ├── pose_utils.py           # Pose detection classes
│   └── audio_manager.py        # Audio feedback
└── assets/
    ├── beep.wav                # Wrong form sound
    └── chime.wav               # Correct form sound
```

### Key Classes

**PoseDetector:**
```python
class PoseDetector:
    def __init__(model_complexity, detection_confidence, tracking_confidence)
    def detect_landmarks(frame) -> results
    def draw_skeleton(frame, results, color) -> frame
    def get_keypoints(results, width, height) -> dict
```

**PushUpAnalyzer:**
```python
class PushUpAnalyzer:
    def __init__(elbow_down, elbow_up, back_tolerance, smoothing, cooldown)
    def analyze_pose(keypoints) -> dict
    def reset() -> None
    def set_params(**kwargs) -> None
```

---

## Configuration

### Backend Configuration

**Location:** `backend.py` lines 18-26

```python
MODEL_COMPLEXITY = 0        # 0=lite, 1=full, 2=heavy
MIN_DETECTION_CONF = 0.5    # Initial detection threshold (0.0-1.0)
TRACKING_CONF = 0.5         # Tracking confidence (0.0-1.0)
ELBOW_DOWN_THRESHOLD = 90   # Angle for "down" position (degrees)
ELBOW_UP_THRESHOLD = 160    # Angle for "up" position (degrees)
BACK_TOLERANCE = 25         # Allowed back deviation from 180° (degrees)
SMOOTHING_ALPHA = 0.3       # EMA smoothing factor (0.0-1.0)
COOLDOWN_FRAMES = 15        # Frames between rep counts (~0.5s at 30fps)
```

### Camera Settings

```python
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)    # Resolution width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)   # Resolution height
cap.set(cv2.CAP_PROP_FPS, 30)             # Target frame rate
```

### Frontend Configuration

**API URL:** `frontend/src/App.jsx` line 8
```javascript
const API_URL = 'http://localhost:8000'
```

**Vite Proxy:** `frontend/vite.config.js`
```javascript
server: {
  port: 5173,
  proxy: {
    '/api': {
      target: 'http://localhost:8000',
      changeOrigin: true
    }
  }
}
```

### Parameter Tuning Guide

| Parameter | Effect | Increase | Decrease |
|-----------|--------|----------|----------|
| **ELBOW_DOWN** | Bottom depth required | Harder reps | Easier reps |
| **ELBOW_UP** | Top extension required | Easier reps | Harder reps |
| **BACK_TOLERANCE** | Form strictness | More lenient | More strict |
| **SMOOTHING_ALPHA** | Angle smoothing | More responsive | More stable |
| **COOLDOWN_FRAMES** | Time between counts | Slower counting | Faster counting |

---

## Troubleshooting

### Common Issues

#### Backend Issues

**Problem:** `Port 8000 already in use`
```bash
# Find and kill process
lsof -ti:8000 | xargs kill -9

# Or change port in backend.py
uvicorn.run(app, host="0.0.0.0", port=8001)
```

**Problem:** `Camera not found`
```bash
# Check camera access
# macOS: System Preferences → Security & Privacy → Camera
# Linux: Check /dev/video0 permissions
# Windows: Camera privacy settings

# Try different camera index
cap = cv2.VideoCapture(1)  # Try 0, 1, 2...
```

**Problem:** `ModuleNotFoundError: mediapipe`
```bash
pip install mediapipe
```

**Problem:** Low FPS / Laggy video
```python
# Reduce resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

# Or use lighter model
MODEL_COMPLEXITY = 0
```

#### Frontend Issues

**Problem:** `Cannot connect to backend`
- Check backend is running on port 8000
- Check CORS configuration
- Check firewall settings

**Problem:** `WebSocket connection failed`
```javascript
// Add error handling
wsRef.current.onerror = (error) => {
  console.error('WebSocket error:', error)
  // Attempt reconnection
}
```

**Problem:** Video not loading
- Check backend `/video_feed` endpoint
- Verify camera started (POST `/camera/start`)
- Check browser console for errors

#### Pose Detection Issues

**Problem:** Skeleton not appearing
- Ensure good lighting
- Position body fully in frame
- Increase detection confidence
- Check if person detected in logs

**Problem:** Inaccurate rep counting
- Adjust thresholds (see Configuration)
- Ensure proper push-up form
- Check back straightness
- Increase cooldown period

**Problem:** False positives (counting when not exercising)
- Increase COOLDOWN_FRAMES
- Tighten BACK_TOLERANCE
- Increase detection confidence
- Ensure stable camera position

---

## Development Guide

### Project Setup for Development

```bash
# Clone repository
git clone <repo-url>
cd ai-pushup-tracker

# Backend setup
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt -r backend_requirements.txt

# Frontend setup
cd frontend
npm install
cd ..
```

### Development Workflow

1. **Start Backend** (Terminal 1)
   ```bash
   python backend.py
   # With auto-reload:
   uvicorn backend:app --reload
   ```

2. **Start Frontend** (Terminal 2)
   ```bash
   cd frontend
   npm run dev
   ```

3. **Make Changes**
   - Frontend: Hot reload automatic
   - Backend: Restart server (or use --reload)

4. **Test Changes**
   - Frontend: `http://localhost:5173`
   - Backend API: `http://localhost:8000/docs`

### Code Style Guidelines

**Python (Backend):**
```python
# PEP 8 style guide
# Type hints recommended
def analyze_pose(self, keypoints: dict) -> dict:
    pass

# Docstrings for classes and functions
"""
Brief description.

Args:
    param: description

Returns:
    description
"""
```

**JavaScript (Frontend):**
```javascript
// Functional components with hooks
// CamelCase for components
// lowercase for variables

const StatCard = ({ title, value, variant }) => {
  // Component logic
}
```

**CSS:**
```css
/* BEM-like naming */
.stat-card { }
.stat-card__title { }
.stat-card--correct { }

/* CSS custom properties for theming */
:root {
  --neo-black: #000000;
}
```

### Adding New Features

**New Stat Display:**
1. Add to backend stats dict
2. Send via WebSocket
3. Add StatCard in App.jsx
4. Style in App.css

**New Control:**
1. Add backend endpoint
2. Add button in Controls.jsx
3. Wire up with handleClick

**New Exercise Type:**
1. Create new analyzer class
2. Add exercise selection UI
3. Switch analyzer based on selection

### Debugging Tips

**Backend:**
```python
# Add print statements
print(f"Elbow angle: {elbow_angle}")

# Use Python debugger
import pdb; pdb.set_trace()

# Check logs in terminal
```

**Frontend:**
```javascript
// Console logging
console.log('Stats:', stats)

// React DevTools
// Install browser extension

// Network tab
// Check WebSocket frames
// Check API responses
```

---

## Performance Optimization

### Backend Optimizations

**1. Model Complexity**
```python
# Lite model (fastest)
MODEL_COMPLEXITY = 0  # ~40 FPS

# Full model (balanced)
MODEL_COMPLEXITY = 1  # ~30 FPS

# Heavy model (most accurate)
MODEL_COMPLEXITY = 2  # ~15 FPS
```

**2. Frame Resolution**
```python
# Low (fastest)
640x480  # Current

# High (better quality)
1280x720  # Slower

# Ultra low (embedded systems)
320x240  # Very fast
```

**3. JPEG Quality**
```python
cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 85])
# Range: 0-100
# Lower = smaller size, faster, lower quality
```

**4. Processing Optimizations**
- Use `model_complexity=0` for speed
- Enable `smooth_landmarks=True`
- Disable segmentation
- Process every Nth frame if needed

### Frontend Optimizations

**1. React Optimizations**
```javascript
// Memoize components
const StatCard = React.memo(({ title, value, variant }) => {
  // ...
})

// Debounce updates
const debouncedUpdate = debounce(setStats, 100)
```

**2. WebSocket Optimization**
```javascript
// Reduce update frequency
await asyncio.sleep(0.2)  // 5 Hz instead of 10 Hz
```

**3. Build Optimization**
```bash
npm run build
# Vite optimizations:
# - Code splitting
# - Tree shaking
# - Minification
# - Asset optimization
```

### Benchmarking

**Expected Performance:**
- Backend FPS: 25-30
- Frontend FPS: 30 (matching stream)
- WebSocket latency: <50ms
- Rep detection latency: <100ms

**Monitoring:**
```python
import time
start = time.time()
# ... processing ...
fps = 1 / (time.time() - start)
print(f"FPS: {fps:.1f}")
```

---

## Future Enhancements

### Planned Features

**1. Exercise Library**
- Squats
- Planks
- Sit-ups
- Jumping jacks
- Custom exercises

**2. User Profiles**
- Multiple users
- Personal records
- Goal tracking
- Progress history

**3. Workout Sessions**
- Session timing
- Set/rep tracking
- Rest timers
- Workout plans

**4. Analytics Dashboard**
- Charts and graphs
- Weekly/monthly stats
- Form quality trends
- Personal bests

**5. Social Features**
- Leaderboards
- Share achievements
- Challenge friends
- Community workouts

**6. Advanced ML**
- Exercise auto-detection
- Form correction suggestions
- Difficulty adjustment
- Injury prevention

**7. Mobile App**
- React Native version
- iOS/Android support
- Offline mode
- Push notifications

**8. Voice Control**
- Voice commands
- Audio coaching
- Motivational feedback

**9. Integration**
- Fitness tracker sync (Fitbit, Apple Health)
- Social media sharing
- Export data (CSV, JSON)

### Technical Improvements

**1. Testing**
```bash
# Unit tests
pytest backend/tests/

# Frontend tests
npm run test

# E2E tests
playwright test
```

**2. CI/CD**
```yaml
# GitHub Actions
name: CI
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: npm test
      - run: pytest
```

**3. Docker Deployment**
```dockerfile
# Dockerfile
FROM python:3.11-slim
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "backend.py"]
```

**4. Database**
```python
# PostgreSQL for user data
# Redis for session caching
# InfluxDB for time-series metrics
```

**5. Authentication**
```python
# JWT tokens
# OAuth (Google, GitHub)
# User management
```

---

## Credits & License

### Development
**Developer:** Exowdious
**Year:** 2025
**License:** MIT

### Technologies Used
- **MediaPipe:** Google LLC
- **React:** Meta Platforms, Inc.
- **FastAPI:** Sebastián Ramírez
- **OpenCV:** OpenCV Foundation
- **Vite:** Evan You & Vite Team

### Design Inspiration
- **Neobrutalism:** Modern web design trend
- **Space Grotesk:** Florian Karsten (Google Fonts)

### Resources
- [MediaPipe Documentation](https://google.github.io/mediapipe/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [Vite Documentation](https://vitejs.dev/)

---

## Contact & Support

### Questions?
- Check the documentation above
- Review `LAUNCH_GUIDE.txt` for quick start
- See `QUICKSTART.md` for commands
- Check `COMPARISON.md` for architecture info

### Issues?
- Check Troubleshooting section
- Review browser console logs
- Check backend terminal output
- Verify camera permissions

### Contribute?
- Fork the repository
- Create feature branch
- Submit pull request
- Follow code style guidelines

---

**Built with ❤️ using React, FastAPI, and MediaPipe**

**© 2025 EXOWDIOUS - All Rights Reserved**
