@echo off
TITLE Sign Language AI - Installer & Launcher
CLS

ECHO ======================================================
ECHO   SIGN LANGUAGE AI - AUTO SETUP
ECHO ======================================================

:: 1. SEARCH FOR PYTHON 3.10
:: We look for the standard install path or the global command
SET PYTHON_CMD=py -3.10
%PYTHON_CMD% --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    SET PYTHON_CMD=python
)

:: Check if the found command is actually version 3.10
%PYTHON_CMD% -c "import sys; exit(0) if sys.version_info[:2] == (3, 10) else exit(1)" >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    ECHO ❌ ERROR: Python 3.10 is not detected.
    ECHO MediaPipe REQUIRES Python 3.10.
    ECHO.
    ECHO Please download it here: https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe
    ECHO (Make sure to check 'Add to PATH' during installation)
    PAUSE
    EXIT /B
)

ECHO ✅ Found Compatible Python: %PYTHON_CMD%

:: 2. CREATE VIRTUAL ENVIRONMENT
IF NOT EXIST "venv" (
    ECHO 📦 Creating virtual environment...
    %PYTHON_CMD% -m venv venv
)

:: 3. INSTALL LIBRARIES
ECHO ⬇️  Checking libraries...
call venv\Scripts\activate
pip install --upgrade pip >nul 2>&1
pip install opencv-python mediapipe numpy >nul 2>&1

:: 4. RUN PROJECT
ECHO 🚀 Launching Camera...
python main.py

PAUSE