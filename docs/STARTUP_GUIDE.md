# 🚀 AI PUSH-UP TRACKER - Startup Guide

Advanced startup scripts for easy project initialization and management across all platforms.

---

## 📋 Features

### ✨ Both Scripts Include:
- **Dependency Installation** - Install/update Python and Node.js packages
- **Virtual Environment Management** - Create and activate Python virtual environment
- **Backend Server** - Start FastAPI server (Port 8000)
- **Frontend Server** - Start React + Vite dev server (Port 5173)
- **Process Management** - Kill all running processes
- **Interactive Menu** - User-friendly menu system
- **Direct Commands** - Run commands without interactive menu
- **Logging** - Automatic logs directory creation

---

## 🖥️ Linux / macOS (Bash Script)

### File: `start.sh`

#### Quick Start
```bash
# Make script executable
chmod +x start.sh

# Run interactive menu
./start.sh

# Or run specific command
./start.sh install      # Install dependencies
./start.sh venv         # Activate virtual environment
./start.sh start        # Start both services
./start.sh backend      # Start backend only
./start.sh frontend     # Start frontend only
./start.sh kill         # Kill all processes
```

#### Interactive Menu Options
```
1) Install/Update Dependencies
2) Activate Virtual Environment Only
3) Start Backend Only
4) Start Frontend Only
5) Start Both (Backend + Frontend)
6) Kill All Processes
7) Full Startup (Install + Activate + Start All)
0) Exit
```

#### What It Does

**Option 1: Install Dependencies**
- ✓ Checks Python and pip installation
- ✓ Installs backend packages from `backend_requirements.txt`
- ✓ Checks Node.js and npm
- ✓ Installs frontend packages via `npm install`

**Option 2: Activate Virtual Environment**
- ✓ Creates `venv/` if it doesn't exist
- ✓ Activates the virtual environment
- ✓ Shows activation command for future use

**Option 3-5: Start Services**
- ✓ Creates logs directory
- ✓ Starts backend on `http://localhost:8000`
- ✓ Starts frontend on `http://localhost:5173`
- ✓ Saves process PIDs for cleanup

**Option 6: Kill All Processes**
- ✓ Kills processes by saved PIDs
- ✓ Force kills by port as fallback
- ✓ Cleans up both backend and frontend

**Option 7: Full Startup**
- ✓ Installs dependencies
- ✓ Activates virtual environment
- ✓ Starts both services
- ✓ Provides running URLs and logging info

#### Environment Detection
The script automatically detects:
- Python 3 or Python 2
- pip or pip3
- Node.js availability
- System type (Linux/macOS)

#### Log Files
Logs are stored in `logs/` directory:
```
logs/
  backend.log       # Backend FastAPI output
  frontend.log      # Frontend React + Vite output
  backend.pid       # Backend process ID
  frontend.pid      # Frontend process ID
```

View logs with:
```bash
tail -f logs/backend.log
tail -f logs/frontend.log
```

---

## 🪟 Windows (Batch Script)

### File: `start-app.bat`

#### Quick Start
```cmd
REM Run interactive menu
start-app.bat

REM Or run specific command
start-app.bat install      # Install dependencies
start-app.bat venv         # Activate virtual environment
start-app.bat start        # Start both services
start-app.bat backend      # Start backend only
start-app.bat frontend     # Start frontend only
start-app.bat kill         # Kill all processes
```

#### Interactive Menu Options
```
1) Install/Update Dependencies
2) Activate Virtual Environment Only
3) Start Backend Only
4) Start Frontend Only
5) Start Both (Backend + Frontend)
6) Kill All Processes
7) Full Startup (Install + Activate + Start All)
0) Exit
```

#### What It Does

Same features as the Bash script but for Windows:

**Option 1: Install Dependencies**
- ✓ Validates Python and pip
- ✓ Upgrades backend packages
- ✓ Validates Node.js and npm
- ✓ Installs frontend dependencies

**Option 2: Activate Virtual Environment**
- ✓ Creates `venv\` directory
- ✓ Activates via `venv\Scripts\activate.bat`
- ✓ Shows manual activation command

**Option 3-5: Start Services**
- ✓ Opens services in separate command windows
- ✓ Backend: `http://localhost:8000`
- ✓ Frontend: `http://localhost:5173`
- ✓ Creates logs directory

**Option 6: Kill All Processes**
- ✓ Force kills Python processes
- ✓ Force kills Node processes
- ✓ Terminates child processes

**Option 7: Full Startup**
- ✓ Complete setup from scratch
- ✓ Installs all dependencies
- ✓ Activates environment
- ✓ Launches both services

#### Multiple Windows
When starting both services:
- Backend runs in: "AI Pushup Tracker - Backend" window
- Frontend runs in: "AI Pushup Tracker - Frontend" window
- Main menu stays open for additional commands

---

## 📊 Service URLs

After successful startup:

| Service | URL | Purpose |
|---------|-----|---------|
| Frontend | `http://localhost:5173` | React Web App |
| Backend | `http://localhost:8000` | FastAPI Server |
| API Docs | `http://localhost:8000/docs` | Swagger UI |
| Redoc | `http://localhost:8000/redoc` | ReDoc Docs |

---

## 🛠️ Troubleshooting

### Python Not Found
**Linux/macOS:**
```bash
# Install Python
brew install python3  # macOS
sudo apt-get install python3  # Ubuntu/Debian

# Verify installation
python3 --version
pip3 --version
```

**Windows:**
- Download from https://www.python.org/downloads/
- Add Python to PATH during installation
- Verify: `python --version`

### Node.js Not Found
**All Platforms:**
- Download from https://nodejs.org/
- Install LTS version (18+ recommended)
- Verify: `node --version` and `npm --version`

### Port Already in Use
If ports 8000 or 5173 are occupied:

**Find Process Using Port (macOS/Linux):**
```bash
lsof -i :8000      # Backend port
lsof -i :5173      # Frontend port
kill -9 <PID>      # Kill by process ID
```

**Find Process Using Port (Windows):**
```cmd
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### Dependency Installation Issues

**Clear pip cache:**
```bash
pip install --no-cache-dir -r backend_requirements.txt
```

**Reinstall in virtual environment:**
```bash
# Linux/macOS
source venv/bin/activate
pip install -r backend_requirements.txt

# Windows
venv\Scripts\activate
pip install -r backend_requirements.txt
```

**Force npm reinstall:**
```bash
cd frontend
rm -rf node_modules package-lock.json  # Linux/macOS
rmdir /s node_modules                  # Windows
npm install
```

---

## 📁 Project Structure Expected

```
ai-pushup-tracker/
├── start.sh                    # Bash script (Linux/macOS)
├── start-app.bat              # Batch script (Windows)
├── backend.py                 # FastAPI main file
├── backend_requirements.txt    # Python dependencies
├── requirements.txt           # Additional Python deps (optional)
├── frontend/                  # React application
│   ├── package.json
│   ├── src/
│   └── node_modules/
└── logs/                      # Created by scripts
    ├── backend.log
    ├── frontend.log
    ├── backend.pid
    └── frontend.pid
```

---

## 🔄 Workflow Examples

### Complete Fresh Setup (All Platforms)
```bash
# Interactive menu - Select option 7
./start.sh              # Linux/macOS
start-app.bat           # Windows

# Command line - Full startup
./start.sh 7            # Auto-run all steps
```

### Development Workflow
```bash
# Initial setup
./start.sh install
./start.sh venv

# Daily startup - Start both services
./start.sh start

# If stuck - Kill and restart
./start.sh kill
./start.sh start
```

### Backend Development Only
```bash
# Install dependencies
./start.sh install

# Start only backend
./start.sh backend

# View backend logs
tail -f logs/backend.log
```

### Frontend Development Only
```bash
# Install dependencies
./start.sh install

# Start only frontend
./start.sh frontend

# View frontend logs
tail -f logs/frontend.log
```

---

## 🎯 Best Practices

1. **Initial Setup**: Run Full Startup (Option 7) first time
2. **Daily Use**: Use Option 5 (Start Both) for quick launch
3. **Debugging**: Keep separate terminal tabs for each service log
4. **Cleanup**: Use Option 6 (Kill All) before system shutdown
5. **Virtual Environment**: Activate it when doing Python development
6. **Logs**: Check logs when services won't start

---

## 📝 Notes

- Scripts are cross-platform compatible (with platform-specific versions)
- Virtual environment is optional but recommended
- Logs help troubleshoot issues
- Both services can run simultaneously
- Scripts handle missing dependencies gracefully
- Process IDs saved for reliable cleanup

---

## ❓ FAQ

**Q: Can I run backend and frontend separately?**
A: Yes, use Options 3 and 4 (or `backend` and `frontend` commands)

**Q: Where are the logs stored?**
A: In the `logs/` directory created by the scripts

**Q: How do I stop the services?**
A: Press Ctrl+C in the terminals, or use Option 6 (Kill All)

**Q: Can I use the scripts from anywhere?**
A: Scripts should be run from the project root directory

**Q: What if installation fails?**
A: Check if Python/Node.js are installed, install manually if needed

**Q: Can I modify the port numbers?**
A: Edit `BACKEND_PORT` and `FRONTEND_PORT` variables in scripts

---

## 🤝 Support

For issues or questions:
1. Check the Troubleshooting section
2. Verify all prerequisites are installed
3. Check log files for error details
4. Ensure you're running from project root

---

**Last Updated:** November 2025
**Version:** 2.0 (Advanced)
