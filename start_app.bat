@echo off
TITLE Sign Language AI - Auto Launcher
CLS

ECHO ======================================================
ECHO      SIGN LANGUAGE AI - ONE CLICK INSTALLER
ECHO ======================================================

:: 1. Check for Python 3.10 specifically (Required for MediaPipe)
py -3.10 --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    ECHO ❌ ERROR: Python 3.10 is missing!
    ECHO.
    ECHO MediaPipe requires Python 3.10. Please install it:
    ECHO 1. Go to: https://www.python.org/downloads/release/python-31011/
    ECHO 2. Download "Windows installer (64-bit)"
    ECHO 3. IMPORTANT: Check "Add Python to PATH" during install.
    ECHO.
    PAUSE
    EXIT /B
)

:: 2. Create Virtual Environment (If missing)
IF NOT EXIST "venv" (
    ECHO 📦 Creating a fresh virtual environment...
    py -3.10 -m venv venv
)

:: 3. Install Libraries (Directly into venv)
ECHO ⬇️  Checking/Installing libraries...
.\venv\Scripts\python.exe -m pip install -r requirements.txt

:: 4. Run the Project
ECHO.
ECHO 🚀 STARTING AI...
ECHO.
.\venv\Scripts\python.exe main.py

:: 5. Pause only if it crashes
IF %ERRORLEVEL% NEQ 0 (
    ECHO.
    ECHO ❌ The app crashed or closed. Read the error above.
    PAUSE
)