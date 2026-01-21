# 🚀 Quick Start Guide

## Universal Startup Scripts

This project includes **cross-platform startup scripts** that automatically detect your operating system, install dependencies, and launch the application.

---

## For macOS & Linux Users 🍎🐧

### Option 1: Universal Script (Recommended)
```bash
./start-app.sh
```

**Features:**
- ✅ Auto-detects macOS/Linux
- ✅ Checks Python & Node.js installation
- ✅ Auto-installs all dependencies
- ✅ Interactive menu with 5 options
- ✅ Beautiful colored terminal output
- ✅ Opens servers in separate terminal windows

### Quick Start Options
```bash
./start-app.sh both      # Start both servers (shortcut)
./start-app.sh backend   # Start backend only (shortcut)
./start-app.sh frontend  # Start frontend only (shortcut)
./start-app.sh --skip-checks  # Skip dependency checks
```

### Menu Options
1. **Start Both (Recommended)** - Opens backend + frontend in separate terminals
2. **Start Backend Only** - Python FastAPI server on port 8000
3. **Start Frontend Only** - React Vite dev server on port 5173
4. **Install Dependencies** - Reinstall all packages
5. **Exit** - Quit the script

---

## For Windows Users 🪟

### Option 1: Git Bash / WSL
```bash
./start-app.sh
```
(Same as macOS/Linux)

### Option 2: Native Windows (Command Prompt / PowerShell)
```cmd
start-app.bat
```

**Features:**
- ✅ Native Windows batch file
- ✅ Checks Python & Node.js installation
- ✅ Auto-installs all dependencies
- ✅ Interactive menu
- ✅ Opens servers in separate CMD windows

### Double-Click Method
1. Navigate to project folder in File Explorer
2. Double-click `start-app.bat`
3. Choose your option from the menu

---

## What Gets Installed?

### Python Packages
- **OpenCV** (4.10.0.84) - Computer vision
- **MediaPipe** (0.10.14) - Pose detection AI
- **FastAPI** (0.104.1) - Backend API framework
- **Uvicorn** (0.24.0) - ASGI server
- **WebSockets** (12.0) - Real-time communication
- **NumPy** (1.26.4) - Numerical computing

### Node.js Packages
- **React** (18.2.0) - UI framework
- **Vite** (5.0.0) - Build tool & dev server
- **Axios** (1.6.0) - HTTP client

---

## System Requirements

### Minimum Requirements
- **Python:** 3.8 or higher
- **Node.js:** 18.0 or higher
- **npm:** 9.0 or higher
- **Webcam:** Built-in or USB camera

### Recommended
- **Python:** 3.11+
- **Node.js:** 20.0+
- **RAM:** 4GB minimum, 8GB recommended
- **CPU:** Multi-core processor for smooth video processing

---

## Troubleshooting

### Script won't run (macOS/Linux)
```bash
# Make executable
chmod +x start-app.sh

# Run with bash explicitly
bash start-app.sh
```

### Python not found
- **macOS:** Install via Homebrew: `brew install python@3.11`
- **Linux:** `sudo apt install python3` or `sudo yum install python3`
- **Windows:** Download from https://www.python.org/downloads/

### Node.js not found
Download from: https://nodejs.org/

### Camera not working
- **macOS:** System Preferences → Security & Privacy → Camera → Allow Terminal
- **Linux:** Check `/dev/video0` permissions
- **Windows:** Settings → Privacy → Camera → Allow apps

### Port already in use
```bash
# Kill process on port 8000 (backend)
# macOS/Linux:
lsof -ti:8000 | xargs kill -9

# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### Dependencies fail to install
```bash
# Update pip
python -m pip install --upgrade pip

# Install with verbose output
pip install -r requirements.txt --verbose

# Windows: Run as Administrator
# macOS: Use sudo if needed
```

---

## Manual Installation (Alternative)

If you prefer manual setup:

### Backend
```bash
# Install Python packages
pip install -r requirements.txt
pip install -r backend_requirements.txt

# Start backend
python backend.py
```

### Frontend
```bash
# Install Node packages
cd frontend
npm install

# Start frontend
npm run dev
```

---

## Access Points

Once running:
- **Frontend UI:** http://localhost:5173
- **Backend API:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs

---

## Stopping the Application

### Keyboard Shortcut
Press `Ctrl+C` in the terminal running the server

### Kill All Processes
```bash
# macOS/Linux
pkill -f "python backend.py"
pkill -f "vite"

# Windows
taskkill /F /IM python.exe
taskkill /F /IM node.exe
```

---

## Old Scripts (Still Available)

Legacy scripts for backward compatibility:

```bash
./start.sh           # Original dual startup (macOS/Linux)
./start-backend.sh   # Backend only
./start-frontend.sh  # Frontend only
```

---

## 🎮 Controls
- **🚀 START** - Begin camera tracking
- **⏸️ STOP** - Pause tracking
- **🔄 RESET** - Reset rep counter

## 🎨 What You'll See
- **Form Status Card** - Changes color based on your form
  - 🟢 Green = Correct form
  - 🔴 Red = Wrong form
  - 🔵 Cyan = Neutral
- **Total Reps** - Your push-up count
- **Stage** - Current position (UP/DOWN)
- **Live Feed** - Real-time video with skeleton overlay

---

## Need Help?

1. Check **DOCUMENTATION.md** for complete project details
2. Check **LAUNCH_GUIDE.txt** for step-by-step instructions
3. View backend logs in terminal
4. Check browser console (F12) for frontend errors
5. Verify camera permissions

---

**Built with ❤️ by Exowdious**

**© 2025 - AI Push-Up Tracker**
