#!/usr/bin/env python3
"""
╔════════════════════════════════════════════════════════════════╗
║                                                                ║
║    🚀 AI PUSH-UP TRACKER - STARTUP SCRIPTS REFERENCE          ║
║                                                                ║
║    Advanced Startup Manager for All Platforms                 ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
"""

# ============================================================================
# QUICK REFERENCE CARD
# ============================================================================

QUICK_REFERENCE = """
┌────────────────────────────────────────────────────────────────┐
│              STARTUP SCRIPTS - QUICK REFERENCE                 │
└────────────────────────────────────────────────────────────────┘

🖥️  PLATFORMS:
   • macOS/Linux:  start.sh (bash)
   • Windows:      start-app.bat (batch)

⚡ QUICK START:
   Linux/macOS:    chmod +x start.sh && ./start.sh 7
   Windows:        start-app.bat

📋 MENU OPTIONS (0-7):

   ┌─────────────────────────────────────────────────────────────┐
   │ 1) Install/Update Dependencies                              │
   │    └─ Checks & installs Python & Node.js packages           │
   │                                                              │
   │ 2) Activate Virtual Environment                             │
   │    └─ Creates & activates venv                              │
   │                                                              │
   │ 3) Start Backend Only                                       │
   │    └─ FastAPI on http://localhost:8000                      │
   │                                                              │
   │ 4) Start Frontend Only                                      │
   │    └─ React+Vite on http://localhost:5173                   │
   │                                                              │
   │ 5) Start Both (Backend + Frontend)                          │
   │    └─ Both services running simultaneously                   │
   │                                                              │
   │ 6) Kill All Processes                                       │
   │    └─ Safely terminates all services                        │
   │                                                              │
   │ 7) Full Startup (Install + Activate + Start)                │
   │    └─ Everything in one command (FASTEST!)                  │
   │                                                              │
   │ 0) Exit                                                      │
   │    └─ Close startup manager                                 │
   └─────────────────────────────────────────────────────────────┘

💻 DIRECT COMMANDS (No Menu):

   Linux/macOS:
   ┌─────────────────────────────────────────────────────────────┐
   │ ./start.sh install                 # Install dependencies   │
   │ ./start.sh venv                    # Activate venv          │
   │ ./start.sh start                   # Start both             │
   │ ./start.sh backend                 # Backend only           │
   │ ./start.sh frontend                # Frontend only          │
   │ ./start.sh kill                    # Kill all               │
   └─────────────────────────────────────────────────────────────┘

   Windows:
   ┌─────────────────────────────────────────────────────────────┐
   │ start-app.bat install              # Install dependencies   │
   │ start-app.bat venv                 # Activate venv          │
   │ start-app.bat start                # Start both             │
   │ start-app.bat backend              # Backend only           │
   │ start-app.bat frontend             # Frontend only          │
   │ start-app.bat kill                 # Kill all               │
   └─────────────────────────────────────────────────────────────┘

🌐 SERVICE URLS:

   ┌────────────────────────────────────┐
   │ Frontend    http://localhost:5173  │
   │ Backend     http://localhost:8000  │
   │ API Docs    http://localhost:8000/docs │
   └────────────────────────────────────┘

📝 VIEWING LOGS:

   Linux/macOS:
   ┌─────────────────────────────────────────────────────────────┐
   │ tail -f logs/backend.log           # Watch backend logs     │
   │ tail -f logs/frontend.log          # Watch frontend logs    │
   └─────────────────────────────────────────────────────────────┘

   Windows:
   ┌─────────────────────────────────────────────────────────────┐
   │ Check logs/ folder in file explorer                          │
   │ Open backend.log or frontend.log with text editor           │
   └─────────────────────────────────────────────────────────────┘

✅ WORKFLOW EXAMPLES:

   First Time Setup:
   ┌─────────────────────────────────────────────────────────────┐
   │ Run: ./start.sh 7                                           │
   │ Or select option 7 from interactive menu                    │
   └─────────────────────────────────────────────────────────────┘

   Daily Development:
   ┌─────────────────────────────────────────────────────────────┐
   │ Run: ./start.sh 5  (or ./start.sh start)                    │
   │ Or select option 5 from menu                                │
   └─────────────────────────────────────────────────────────────┘

   Backend Development:
   ┌─────────────────────────────────────────────────────────────┐
   │ Run: ./start.sh 3  (or ./start.sh backend)                  │
   │ View: tail -f logs/backend.log                              │
   └─────────────────────────────────────────────────────────────┘

   Troubleshooting:
   ┌─────────────────────────────────────────────────────────────┐
   │ Run: ./start.sh 6  (kill all processes)                     │
   │ Then: ./start.sh 5  (start fresh)                           │
   └─────────────────────────────────────────────────────────────┘

🔍 TROUBLESHOOTING:

   Problem: Python not found
   └─ Install from https://www.python.org/downloads/
   
   Problem: Port 8000 already in use
   └─ Run: ./start.sh 6 (kills all processes)
   
   Problem: npm not found
   └─ Install Node.js from https://nodejs.org/
   
   Problem: Dependencies not installing
   └─ Run: pip install --no-cache-dir -r backend_requirements.txt

📊 FEATURES:

   ✅ Interactive menu system
   ✅ 7 smart operations
   ✅ Direct command support
   ✅ Automatic logging
   ✅ Process tracking
   ✅ Error handling
   ✅ Windows support
   ✅ macOS/Linux support
   ✅ Virtual environment support
   ✅ Dependency management
   ✅ Safe process cleanup
   ✅ Comprehensive documentation

📚 DOCUMENTATION:

   • QUICK_START.md         - 30-second startup guide
   • STARTUP_GUIDE.md       - Comprehensive guide
   • STARTUP_CHANGELOG.md   - What changed overview
   • STARTUP_IMPLEMENTATION.md - Technical details

💾 FILES CREATED:

   start.sh                 - Linux/macOS startup script
   start-app.bat           - Windows startup script
   logs/                   - Auto-created logs directory
   logs/backend.log        - Backend server output
   logs/frontend.log       - Frontend server output
   logs/backend.pid        - Backend process ID
   logs/frontend.pid       - Frontend process ID

🎯 BEST PRACTICES:

   1. First time? Always run option 7 (Full Startup)
   2. Daily use? Use option 5 (Start Both)
   3. Issues? Use option 6 (Kill All) then restart
   4. Debugging? Check logs/ directory for output
   5. Automation? Use direct commands (no menu)

⚠️  REQUIREMENTS:

   • Python 3.8+
   • Node.js 18+ (optional, for frontend)
   • 2 GB RAM minimum
   • Internet connection (first install)

📞 QUICK HELP:

   Q: How do I know what's running?
   A: Check http://localhost:5173 and http://localhost:8000

   Q: Where are my logs?
   A: In the logs/ directory (auto-created)

   Q: How do I stop services?
   A: Press Ctrl+C or use option 6 (Kill All)

   Q: Can I run backend and frontend separately?
   A: Yes, use options 3 & 4 (or direct commands)

   Q: What if I'm stuck?
   A: Option 6 (Kill All) then try again

════════════════════════════════════════════════════════════════════

Created: November 2025
Version: 2.0 (Advanced)
Status: Production Ready ✅

For more info, see: STARTUP_GUIDE.md

════════════════════════════════════════════════════════════════════
"""

if __name__ == "__main__":
    print(QUICK_REFERENCE)
