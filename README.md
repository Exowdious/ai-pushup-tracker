# 🤖 AI Push-Up Tracker

> **Created by Exowdious**

A real-time AI-powered push-up tracker that uses computer vision to count reps, analyze form, and provide audio feedback. Built with **Python (FastAPI + MediaPipe)** and **React**.

![Project Banner](https://img.shields.io/badge/AI-Powered-blue?style=for-the-badge)
![Exowdious](https://img.shields.io/badge/Created%20By-Exowdious-purple?style=for-the-badge)

---

## ✨ Features

- **Real-time Form Analysis**: Detects body alignment and elbow angles.
- **Smart Counting**: Only counts correctly executed push-ups.
- **Audio Feedback**: Beeps for bad form, chimes for good reps.
- **Privacy First**: All processing runs locally on your machine.
- **Cross-Platform**: Works on macOS, Windows, and Linux.

---

## 🚀 Quick Start (macOS / Linux)

The easiest way to run the project is using the universal startup script.

### Prerequisites
- Python 3.10+
- Node.js & npm

### 1. Setup Environment
```bash
# Clone the repository (if you haven't already)
git clone <repository-url>
cd ai-pushup-tracker

# Create a virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### 2. Install Dependencies
```bash
# Install Python dependencies
pip install -r requirements.txt -r backend_requirements.txt

# Install Frontend dependencies
cd frontend
npm install
cd ..
```

### 3. Run the App
```bash
# Make sure venv is active!
python start.py
```
Select **Option 1: Start Both** from the menu.
- **Frontend**: http://localhost:5173
- **Backend**: http://localhost:8000

---

## 🪟 Quick Start (Windows)

### Prerequisites
- Python 3.10+
- Node.js
- PowerShell or Command Prompt

### 1. Setup Environment
```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate
```

### 2. Install Dependencies
```powershell
# Install Python dependencies
pip install -r requirements.txt -r backend_requirements.txt

# Install Frontend dependencies
cd frontend
npm install
cd ..
```

### 3. Run the App
```powershell
# Ensure venv is active
python start.py
```
Select **Option 1** to launch.

---

## 🐳 Docker Setup (Advanced)

> **⚠️ macOS Note**: Docker on macOS usually **cannot access the webcam**. Use the native setup above for full functionality.

```bash
# Build and run containers
docker-compose up --build
```

---

## 🛠️ Troubleshooting

### 🎥 specific to macOS: Camera Permission
If you see **"Failed to start camera"** but the **backend logs** say `OpenCV: not authorized`:
1. **Grant Permission**: macOS will ask for Terminal camera access. Click **Allow**.
2. **Restart**: You MUST restart the script (`Ctrl+C` then `python start.py`) after granting permission.

### 🌐 Port Conflicts
If port `5173` is busy, the frontend will switch to `5174`.
- The backend is configured to accept connections from **any port** (`*`), so it will work automatically.

### 🐍 Virtual Environment
Always ensure your terminal shows `(venv)` before running scripts.
- **Mac**: `source venv/bin/activate`
- **Win**: `.\venv\Scripts\activate`

---

## 📜 License
© 2025 **Exowdious**. All Rights Reserved.
