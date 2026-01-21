# 💪 AI Push-Up Tracker

> **Real-time push-up tracking using AI pose detection with a bold neobrutalism interface**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![React 18](https://img.shields.io/badge/react-18.2-61dafb.svg)](https://reactjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-009688.svg)](https://fastapi.tiangolo.com/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Latest-ff6f00.svg)](https://google.github.io/mediapipe/)

**Track your push-ups with real-time AI feedback on form and rep counting!**

<p align="center">
  <img src="https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey" alt="Platforms">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
</p>

---

## ✨ Features

🎯 **Real-Time Pose Detection**
- MediaPipe AI tracking with 33 body landmarks
- 30 FPS video processing
- Form-based colored skeleton overlay (Green = Correct, Red = Wrong)

📊 **Smart Rep Counting**
- Automatic push-up detection
- Form validation required for counting
- Hysteresis filtering to prevent false counts
- Cooldown period to avoid double-counting

🎨 **Neobrutalism Design**
- Bold black borders and chunky shadows
- Vibrant yellow background with contrasting cards
- Space Grotesk typography
- No scrolling - everything visible at once

🔊 **Audio Feedback**
- Wrong form alert beep
- Correct form chime

⚡ **Modern Architecture**
- React 18 + Vite frontend
- FastAPI + Uvicorn backend
- WebSocket real-time stats (10 Hz)
- MJPEG video streaming (30 FPS)

---

## 🚀 Quick Start

### One-Line Startup (Recommended)

**macOS / Linux / Git Bash:**
```bash
./start-app.sh
```

**Windows (Native):**
```cmd
start-app.bat
```

**That's it!** The script will:
- ✅ Check Python & Node.js installation
- ✅ Install all dependencies automatically
- ✅ Start backend and frontend servers
- ✅ Open in separate terminal windows

### Access the App
Open your browser to: **http://localhost:5173**

---

## 📋 System Requirements

### Minimum
- **Python:** 3.8+
- **Node.js:** 18.0+
- **RAM:** 4GB
- **Webcam:** Built-in or USB camera

### Recommended
- **Python:** 3.11+
- **Node.js:** 20.0+
- **RAM:** 8GB
- **CPU:** Multi-core processor

---

## 🎮 How to Use

1. **Start the app** using `./start-app.sh` or `start-app.bat`
2. **Click START** to activate the camera
3. **Position yourself** in front of the camera
4. **Do push-ups** - the app will:
   - Track your form in real-time
   - Display skeleton overlay (green/red)
   - Count valid reps automatically
   - Show your current stage (Up/Down)
5. **Click RESET** to start over
6. **Click STOP** to pause tracking

### Perfect Push-Up Form
- **Elbow angle:** Should reach ~90° at bottom
- **Back straightness:** Maintain ~180° (no sagging/arching)
- **Full extension:** Push up to ~160° elbow angle

---

## 📚 Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - Detailed startup instructions for all platforms
- **[DOCUMENTATION.md](DOCUMENTATION.md)** - Complete project documentation (tech stack, architecture, API, configuration)
- **[VISUAL_STARTUP_GUIDE.md](VISUAL_STARTUP_GUIDE.md)** - ASCII diagrams and visual flow charts
- **[STARTUP_SCRIPTS_SUMMARY.md](STARTUP_SCRIPTS_SUMMARY.md)** - Script features and technical details
- **[LAUNCH_GUIDE.txt](LAUNCH_GUIDE.txt)** - Original launch instructions

---

## 🏗️ Architecture

```
Frontend (React + Vite)          Backend (FastAPI + Uvicorn)
      :5173                              :8000
        │                                  │
        ├──── HTTP API Calls ─────────────►│
        │     (Start/Stop/Reset)           │
        │                                  │
        ◄──── WebSocket Stats ─────────────┤
        │     (10 Hz updates)              │
        │                                  │
        ◄──── MJPEG Video Stream ──────────┤
              (30 FPS)                     │
                                           │
                                           ├─► OpenCV Camera
                                           │   (640x480)
                                           │
                                           ├─► MediaPipe Pose
                                           │   (33 landmarks)
                                           │
                                           └─► PushUpAnalyzer
                                               (Form validation + Rep counting)
```

---

## 🛠️ Technology Stack

### Frontend
- **React** 18.2.0 - UI framework
- **Vite** 5.0.0 - Build tool & dev server
- **Axios** 1.6.0 - HTTP client
- **CSS3** - Neobrutalism styling

### Backend
- **FastAPI** 0.104.1 - Web framework
- **Uvicorn** 0.24.0 - ASGI server
- **OpenCV** 4.10.0 - Camera & video processing
- **MediaPipe** 0.10.14 - AI pose detection
- **WebSockets** 12.0 - Real-time communication
- **NumPy** 1.26.4 - Numerical computing

---

## 📦 Installation

### Automatic (Recommended)
Use the startup scripts - they handle everything!

### Manual

**Backend:**
```bash
pip install -r requirements.txt
pip install -r backend_requirements.txt
python backend.py
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

---

## 🔧 Configuration

Edit detection parameters in `backend.py` (lines 18-26):

```python
MODEL_COMPLEXITY = 0        # 0=lite, 1=full, 2=heavy
MIN_DETECTION_CONF = 0.5    # Detection threshold (0.0-1.0)
ELBOW_DOWN_THRESHOLD = 90   # Bottom angle (degrees)
ELBOW_UP_THRESHOLD = 160    # Top angle (degrees)
BACK_TOLERANCE = 25         # Back deviation allowed (degrees)
SMOOTHING_ALPHA = 0.3       # EMA smoothing (0.0-1.0)
COOLDOWN_FRAMES = 15        # Frames between reps (~0.5s at 30fps)
```

### Tuning Guide
- **Harder reps:** Increase `ELBOW_DOWN_THRESHOLD`
- **Easier counting:** Decrease `ELBOW_UP_THRESHOLD`
- **Stricter form:** Decrease `BACK_TOLERANCE`
- **Smoother angles:** Increase `SMOOTHING_ALPHA`
- **Prevent double-counts:** Increase `COOLDOWN_FRAMES`

---

## 🐛 Troubleshooting

### Camera Not Working
- **macOS:** System Preferences → Security & Privacy → Camera → Allow Terminal
- **Linux:** Check `/dev/video0` permissions
- **Windows:** Settings → Privacy → Camera → Allow apps

### Port Already in Use
```bash
# macOS/Linux
lsof -ti:8000 | xargs kill -9

# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### Dependencies Failed
```bash
# Update pip
python -m pip install --upgrade pip

# Reinstall
pip install -r requirements.txt --upgrade
```

### More Help
Check [DOCUMENTATION.md](DOCUMENTATION.md) for comprehensive troubleshooting

---

## 📁 Project Structure

```
ai-pushup-tracker/
├── start-app.sh              # Universal startup script (macOS/Linux)
├── start-app.bat             # Windows startup script
├── backend.py                # FastAPI server
├── requirements.txt          # Python packages (OpenCV, MediaPipe)
├── backend_requirements.txt  # FastAPI packages
├── utils/
│   ├── pose_utils.py        # Pose detection & analysis
│   └── audio_manager.py     # Sound feedback
├── assets/
│   ├── style.css            # Legacy styles
│   ├── beep.wav             # Wrong form sound
│   └── chime.wav            # Correct form sound
├── frontend/
│   ├── package.json         # Node dependencies
│   ├── vite.config.js       # Vite configuration
│   └── src/
│       ├── main.jsx         # React entry point
│       ├── App.jsx          # Main component
│       ├── App.css          # Neobrutalism styles
│       └── components/
│           ├── StatCard.jsx     # Stat display
│           ├── CameraFeed.jsx   # Video stream
│           └── Controls.jsx     # Buttons
└── docs/
    ├── DOCUMENTATION.md          # Complete documentation
    ├── QUICKSTART.md             # Quick start guide
    ├── VISUAL_STARTUP_GUIDE.md   # Visual diagrams
    └── STARTUP_SCRIPTS_SUMMARY.md # Script details
```

---

## 🎯 API Endpoints

### REST API
- `POST /camera/start` - Start camera
- `POST /camera/stop` - Stop camera
- `POST /reset` - Reset counters
- `GET /stats` - Get current stats
- `GET /video_feed` - MJPEG stream

### WebSocket
- `WS /ws/stats` - Real-time stats (10 Hz)

### API Docs
Visit **http://localhost:8000/docs** when backend is running

---

## 🚢 Deployment

### Frontend Build
```bash
cd frontend
npm run build
# Output: frontend/dist/
```

Deploy `dist/` to:
- Netlify
- Vercel
- GitHub Pages
- Any static hosting

### Backend Deploy
- Docker container
- Railway
- Render
- Heroku
- AWS EC2

---

## 🔮 Future Enhancements

- [ ] Multiple exercise types (squats, planks, sit-ups)
- [ ] User profiles and history
- [ ] Workout sessions and timers
- [ ] Analytics dashboard with charts
- [ ] Social features and leaderboards
- [ ] Mobile app (React Native)
- [ ] Voice commands and coaching
- [ ] Fitness tracker integration

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Exowdious**
- GitHub: [@exowdious](https://github.com/exowdious)
- Year: 2025

---

## 🙏 Acknowledgments

- **MediaPipe** by Google for pose detection
- **FastAPI** by Sebastián Ramírez for the amazing web framework
- **React** team at Meta for the UI library
- **Vite** team for the blazing-fast build tool
- **OpenCV** community for computer vision tools
- **Space Grotesk** font by Florian Karsten

---

## ⭐ Star History

If you found this project helpful, please consider giving it a star! ⭐

---

<p align="center">
  <strong>Built with ❤️ using React, FastAPI, and MediaPipe</strong>
</p>

<p align="center">
  <strong>© 2025 EXOWDIOUS - All Rights Reserved</strong>
</p>

---

**Ready to track your push-ups? Run `./start-app.sh` and let's go! 💪**
