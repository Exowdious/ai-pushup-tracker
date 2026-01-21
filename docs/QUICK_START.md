# 🚀 Quick Start - 30 Seconds to Running

## Linux/macOS

```bash
# Step 1: Make executable
chmod +x start.sh

# Step 2: Run (choose interactive menu or direct command)
./start.sh              # Interactive menu
./start.sh 7            # Full setup (fastest)
./start.sh start        # Just start services
```

## Windows

```cmd
# Just run this:
start-app.bat

# Or use command line:
start-app.bat install
start-app.bat start
```

---

## 🎯 What You Get

| Feature | Status |
|---------|--------|
| ✅ Dependencies installed | Auto |
| ✅ Virtual environment | Auto |
| ✅ Backend running | http://localhost:8000 |
| ✅ Frontend running | http://localhost:5173 |
| ✅ Logging enabled | `logs/` directory |

---

## 📋 Menu Options (Numbered)

```
1 = Install dependencies
2 = Activate venv only
3 = Backend only
4 = Frontend only
5 = Start both (RECOMMENDED)
6 = Kill all processes
7 = Full setup (FASTEST)
0 = Exit
```

---

## 💡 Pro Tips

- **First time?** Choose option 7 (Full Startup)
- **Daily use?** Choose option 5 (Start Both)
- **Having issues?** Choose option 6 (Kill All) then restart
- **View logs?** `tail -f logs/backend.log` or `logs/frontend.log`
- **Stuck?** Check if ports 8000 & 5173 are free

---

## ⚠️ Requirements

- Python 3.8+
- Node.js 18+ (optional, for frontend development)
- 2 GB RAM minimum
- Internet connection (for dependency download)

---

## 🔧 Common Commands

| Task | Command |
|------|---------|
| Install deps | `./start.sh install` |
| Start all | `./start.sh start` |
| Kill all | `./start.sh kill` |
| View backend log | `tail -f logs/backend.log` |
| View frontend log | `tail -f logs/frontend.log` |

---

**Next:** Open http://localhost:5173 in your browser! 🎉
