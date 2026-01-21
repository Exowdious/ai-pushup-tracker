#!/usr/bin/env python3
"""
AI Push-Up Tracker - Startup Script
Cross-platform startup script for macOS, Linux, and Windows.
© 2025 Exowdious
"""

import os
import sys
import subprocess
import platform
import shutil
from pathlib import Path

# ANSI color codes
class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    MAGENTA = '\033[0;35m'
    CYAN = '\033[0;36m'
    BOLD = '\033[1m'
    NC = '\033[0m'  # No Color

# Disable colors on Windows CMD (unless using Windows Terminal)
if platform.system() == 'Windows' and 'WT_SESSION' not in os.environ:
    for attr in dir(Colors):
        if not attr.startswith('_'):
            setattr(Colors, attr, '')

def print_banner():
    """Print ASCII art banner."""
    print(f"{Colors.CYAN}")
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║        █████╗ ██╗    ██████╗ ██╗   ██╗███████╗██╗  ██╗    ║
    ║       ██╔══██╗██║    ██╔══██╗██║   ██║██╔════╝██║  ██║    ║
    ║       ███████║██║    ██████╔╝██║   ██║███████╗███████║    ║
    ║       ██╔══██║██║    ██╔═══╝ ██║   ██║╚════██║██╔══██║    ║
    ║       ██║  ██║██║    ██║     ╚██████╔╝███████║██║  ██║    ║
    ║       ╚═╝  ╚═╝╚═╝    ╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═╝    ║
    ║                                                           ║
    ║           ██╗   ██╗██████╗     ████████╗██████╗           ║
    ║           ██║   ██║██╔══██╗    ╚══██╔══╝██╔══██╗          ║
    ║           ██║   ██║██████╔╝       ██║   ██████╔╝          ║
    ║           ██║   ██║██╔═══╝        ██║   ██╔══██╗          ║
    ║           ╚██████╔╝██║            ██║   ██║  ██║          ║
    ║            ╚═════╝ ╚═╝            ╚═╝   ╚═╝  ╚═╝          ║
    ║                                                           ║
    ║              T R A C K E R   -   S T A R T U P            ║
    ║                                                           ║
    ║                      © 2025 Exowdious                     ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    print(f"{Colors.NC}")

def print_system_info():
    """Print system information."""
    print(f"{Colors.BOLD}{Colors.CYAN}┌─────────────────────────────────────────────────────────┐{Colors.NC}")
    print(f"{Colors.BOLD}{Colors.CYAN}│{Colors.NC}                 {Colors.BOLD}SYSTEM INFORMATION{Colors.NC}                  {Colors.BOLD}{Colors.CYAN}│{Colors.NC}")
    print(f"{Colors.BOLD}{Colors.CYAN}└─────────────────────────────────────────────────────────┘{Colors.NC}")
    print(f"{Colors.YELLOW}Operating System:{Colors.NC} {Colors.GREEN}{platform.system()} {platform.release()}{Colors.NC}")
    print(f"{Colors.YELLOW}Python Version:{Colors.NC}   {Colors.GREEN}{sys.version.split()[0]}{Colors.NC}")
    print(f"{Colors.YELLOW}Working Directory:{Colors.NC} {Colors.GREEN}{os.getcwd()}{Colors.NC}")
    print()

def check_node():
    """Check if Node.js is installed."""
    print(f"{Colors.BLUE}[1/2]{Colors.NC} {Colors.BOLD}Checking Node.js installation...{Colors.NC}")
    
    if shutil.which('node'):
        result = subprocess.run(['node', '--version'], capture_output=True, text=True)
        print(f"{Colors.GREEN}✓{Colors.NC} Node.js found: {Colors.GREEN}{result.stdout.strip()}{Colors.NC}")
    else:
        print(f"{Colors.RED}✗{Colors.NC} Node.js not found!")
        print(f"{Colors.YELLOW}Please install Node.js 18+ from:{Colors.NC}")
        print(f"  {Colors.CYAN}https://nodejs.org/{Colors.NC}")
        return False
    
    if shutil.which('npm'):
        result = subprocess.run(['npm', '--version'], capture_output=True, text=True)
        print(f"{Colors.GREEN}✓{Colors.NC} npm found: {Colors.GREEN}{result.stdout.strip()}{Colors.NC}")
    else:
        print(f"{Colors.RED}✗{Colors.NC} npm not found!")
        return False
    
    print()
    return True

def install_deps():
    """Install Python and Node.js dependencies if needed."""
    print(f"{Colors.BLUE}[2/2]{Colors.NC} {Colors.BOLD}Checking dependencies...{Colors.NC}")
    
    # Check if frontend node_modules exists
    frontend_dir = Path('frontend')
    if not (frontend_dir / 'node_modules').exists():
        print(f"{Colors.YELLOW}Installing frontend dependencies...{Colors.NC}")
        subprocess.run(['npm', 'install'], cwd=frontend_dir)
    else:
        print(f"{Colors.GREEN}✓{Colors.NC} Frontend dependencies already installed")
    
    print()
    return True

def show_menu():
    """Show interactive menu."""
    print(f"{Colors.BOLD}{Colors.CYAN}┌─────────────────────────────────────────────────────────┐{Colors.NC}")
    print(f"{Colors.BOLD}{Colors.CYAN}│{Colors.NC}                   {Colors.BOLD}SELECT STARTUP MODE{Colors.NC}                 {Colors.BOLD}{Colors.CYAN}│{Colors.NC}")
    print(f"{Colors.BOLD}{Colors.CYAN}└─────────────────────────────────────────────────────────┘{Colors.NC}")
    print()
    print(f"{Colors.BOLD}{Colors.GREEN}[1]{Colors.NC} {Colors.BOLD}Start Both (Recommended){Colors.NC} - Backend + Frontend")
    print(f"{Colors.BOLD}{Colors.GREEN}[2]{Colors.NC} {Colors.BOLD}Start Backend Only{Colors.NC}       - Python FastAPI server")
    print(f"{Colors.BOLD}{Colors.GREEN}[3]{Colors.NC} {Colors.BOLD}Start Frontend Only{Colors.NC}      - React Vite dev server")
    print(f"{Colors.BOLD}{Colors.RED}[4]{Colors.NC} {Colors.BOLD}Exit{Colors.NC}")
    print()

def start_backend():
    """Start the backend server."""
    print(f"{Colors.BOLD}{Colors.MAGENTA}┌─────────────────────────────────────────────────────────┐{Colors.NC}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}│{Colors.NC}              {Colors.BOLD}STARTING BACKEND SERVER{Colors.NC}                 {Colors.BOLD}{Colors.MAGENTA}│{Colors.NC}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}└─────────────────────────────────────────────────────────┘{Colors.NC}")
    print(f"{Colors.GREEN}Backend:{Colors.NC}  {Colors.CYAN}http://localhost:8000{Colors.NC}")
    print(f"{Colors.GREEN}API Docs:{Colors.NC} {Colors.CYAN}http://localhost:8000/docs{Colors.NC}")
    print()
    print(f"{Colors.YELLOW}Press Ctrl+C to stop{Colors.NC}")
    print()
    
    subprocess.run([sys.executable, 'backend.py'])

def start_frontend():
    """Start the frontend dev server."""
    print(f"{Colors.BOLD}{Colors.MAGENTA}┌─────────────────────────────────────────────────────────┐{Colors.NC}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}│{Colors.NC}             {Colors.BOLD}STARTING FRONTEND SERVER{Colors.NC}                {Colors.BOLD}{Colors.MAGENTA}│{Colors.NC}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}└─────────────────────────────────────────────────────────┘{Colors.NC}")
    print(f"{Colors.GREEN}Frontend:{Colors.NC} {Colors.CYAN}http://localhost:5173{Colors.NC}")
    print()
    print(f"{Colors.YELLOW}Press Ctrl+C to stop{Colors.NC}")
    print()
    
    subprocess.run(['npm', 'run', 'dev'], cwd='frontend')

def start_both():
    """Start both servers - backend in background, frontend in foreground."""
    print(f"{Colors.BOLD}{Colors.MAGENTA}┌─────────────────────────────────────────────────────────┐{Colors.NC}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}│{Colors.NC}           {Colors.BOLD}STARTING BOTH SERVERS{Colors.NC}                    {Colors.BOLD}{Colors.MAGENTA}│{Colors.NC}")
    print(f"{Colors.BOLD}{Colors.MAGENTA}└─────────────────────────────────────────────────────────┘{Colors.NC}")
    print(f"{Colors.GREEN}Backend:{Colors.NC}  {Colors.CYAN}http://localhost:8000{Colors.NC}")
    print(f"{Colors.GREEN}Frontend:{Colors.NC} {Colors.CYAN}http://localhost:5173{Colors.NC}")
    print()
    
    cwd = Path.cwd()
    
    # Determine the correct python executable (from venv if exists)
    if (cwd / 'venv' / 'bin' / 'python3').exists():
        python_exe = str(cwd / 'venv' / 'bin' / 'python3')
    else:
        python_exe = sys.executable
        
    # Check if port 8000 is occupied and kill process if needed
    try:
        if platform.system() != 'Windows':
            cmd = "lsof -i :8000 | grep LISTEN | awk '{print $2}' | xargs kill -9"
            subprocess.run(cmd, shell=True, stderr=subprocess.DEVNULL)
    except Exception:
        pass
    
    # Start backend in background
    print(f"{Colors.YELLOW}Starting backend server...{Colors.NC}")
    backend_log = open('logs/backend.log', 'w')
    Path('logs').mkdir(exist_ok=True)
    backend_proc = subprocess.Popen(
        [python_exe, 'backend.py'],
        cwd=cwd,
        stdout=backend_log,
        stderr=subprocess.STDOUT
    )
    
    # Wait a bit for backend to start
    import time
    time.sleep(2)
    
    # Check if backend started successfully
    if backend_proc.poll() is not None:
        print(f"{Colors.RED}✗{Colors.NC} Backend failed to start! Check logs/backend.log")
        return
    
    print(f"{Colors.GREEN}✓{Colors.NC} Backend started (PID: {backend_proc.pid})")
    print(f"{Colors.CYAN}  Logs: logs/backend.log{Colors.NC}")
    print()
    
    # Start frontend in foreground
    print(f"{Colors.YELLOW}Starting frontend server...{Colors.NC}")
    print(f"{Colors.YELLOW}Press Ctrl+C to stop both servers{Colors.NC}")
    print()
    
    try:
        subprocess.run(['npm', 'run', 'dev'], cwd=cwd / 'frontend')
    except KeyboardInterrupt:
        pass
    finally:
        # Clean up backend when frontend exits
        print(f"\n{Colors.YELLOW}Stopping backend server...{Colors.NC}")
        backend_proc.terminate()
        backend_proc.wait()
        backend_log.close()
        print(f"{Colors.GREEN}✓{Colors.NC} All servers stopped")

def main():
    """Main entry point."""
    os.chdir(Path(__file__).parent)  # Change to script directory
    
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    print_banner()
    print_system_info()
    
    # Check for command line arguments
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg in ['both', '1']:
            check_node()
            install_deps()
            start_both()
            return
        elif arg in ['backend', '2']:
            start_backend()
            return
        elif arg in ['frontend', '3']:
            check_node()
            install_deps()
            start_frontend()
            return
        elif arg == '--skip-checks':
            pass  # Continue to menu without checks
        else:
            print(f"Usage: {sys.argv[0]} [both|backend|frontend|--skip-checks]")
            return
    
    # Run checks
    if not (len(sys.argv) > 1 and sys.argv[1] == '--skip-checks'):
        if not check_node():
            return
        install_deps()
    
    # Interactive menu
    while True:
        show_menu()
        try:
            choice = input(f"{Colors.YELLOW}Enter your choice [1-4]:{Colors.NC} ").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{Colors.GREEN}Goodbye!{Colors.NC}")
            break
        
        print()
        
        if choice == '1':
            start_both()
            break
        elif choice == '2':
            start_backend()
            break
        elif choice == '3':
            start_frontend()
            break
        elif choice == '4':
            print(f"{Colors.GREEN}Thanks for using AI Push-Up Tracker!{Colors.NC}")
            print(f"{Colors.CYAN}© 2025 Exowdious{Colors.NC}")
            break
        else:
            print(f"{Colors.RED}Invalid choice. Please enter 1-4.{Colors.NC}")
            print()

if __name__ == '__main__':
    main()
