# AI Push-Up Tracker - React + FastAPI Version

## 🎨 Full Neobrutalism Design
Bold, raw, and unapologetic UI with thick black borders, vibrant colors, and chunky shadows.

## 🏗️ Architecture

### Backend (Python + FastAPI)
- **File**: `backend.py`
- **Port**: 8000
- **Features**:
  - REST API endpoints for camera control
  - Real-time video streaming with pose detection
  - WebSocket for live statistics updates
  - MediaPipe pose detection
  - Push-up form analysis

### Frontend (React + Vite)
- **Directory**: `frontend/`
- **Port**: 5173
- **Features**:
  - Modern React with hooks
  - Real-time stats via WebSocket
  - Responsive neobrutalism design
  - Live video feed streaming

## 🚀 Setup Instructions

### 1. Install Backend Dependencies

```bash
# Install FastAPI and related packages
pip install -r backend_requirements.txt

# Your existing requirements for pose detection
pip install -r requirements.txt
```

### 2. Install Frontend Dependencies

```bash
cd frontend
npm install
```

## 🎮 Running the Application

### Start Backend Server (Terminal 1)
```bash
python backend.py
```
The backend will start on `http://localhost:8000`

### Start Frontend Dev Server (Terminal 2)
```bash
cd frontend
npm run dev
```
The frontend will start on `http://localhost:5173`

## 🌐 Usage

1. Open your browser and go to `http://localhost:5173`
2. Click **🚀 START** to begin camera capture
3. Perform push-ups and watch the real-time tracking!
4. Click **⏸️ STOP** to pause tracking
5. Click **🔄 RESET** to reset your rep counter

## 📡 API Endpoints

- `GET /` - Health check
- `POST /camera/start` - Start camera capture
- `POST /camera/stop` - Stop camera capture
- `POST /reset` - Reset rep counter
- `GET /stats` - Get current statistics
- `GET /video_feed` - MJPEG video stream
- `WS /ws/stats` - WebSocket for real-time stats

## 🎨 Neobrutalism Design Features

- **Bold 4px black borders** on all elements
- **8px chunky shadows** for depth
- **Vibrant color palette**: Yellow bg, cyan/pink/purple buttons
- **Space Grotesk font** - heavy and uppercase
- **Interactive animations** - elements shift on hover/click
- **Form-based colors**: Green (correct), Red (wrong), Cyan (neutral)

## 🔧 Tech Stack

**Backend:**
- FastAPI - Modern Python web framework
- Uvicorn - ASGI server
- OpenCV - Video capture
- MediaPipe - Pose detection
- WebSockets - Real-time communication

**Frontend:**
- React 18 - UI library
- Vite - Fast build tool
- Axios - HTTP client
- CSS3 - Neobrutalism styling

## 📝 Project Structure

```
ai-pushup-tracker/
├── backend.py                 # FastAPI server
├── backend_requirements.txt   # Backend dependencies
├── requirements.txt           # Pose detection dependencies
├── utils/                     # Pose detection utilities
│   ├── pose_utils.py
│   └── audio_manager.py
├── assets/                    # Audio files
│   ├── beep.wav
│   └── chime.wav
└── frontend/                  # React application
    ├── package.json
    ├── vite.config.js
    ├── index.html
    └── src/
        ├── main.jsx
        ├── App.jsx
        ├── App.css
        └── components/
            ├── StatCard.jsx
            ├── CameraFeed.jsx
            └── Controls.jsx
```

## 🐛 Troubleshooting

### Backend Issues
- **Camera not opening**: Check camera permissions
- **Port 8000 in use**: Change port in `backend.py` and `App.jsx`
- **Import errors**: Install all dependencies

### Frontend Issues
- **Can't connect to backend**: Ensure backend is running on port 8000
- **WebSocket errors**: Check CORS settings in `backend.py`
- **Build errors**: Delete `node_modules` and run `npm install` again

## 🎯 Performance Optimizations

- Vite for fast development and optimized production builds
- WebSocket for efficient real-time updates
- MJPEG streaming for smooth video
- React component memoization
- Efficient pose detection with MediaPipe

## 📄 License

MIT License - Feel free to modify and use!
