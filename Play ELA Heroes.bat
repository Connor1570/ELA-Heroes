@echo off
TITLE ELA Heroes Launcher
CLS

ECHO Starting ELA Heroes...
ECHO.

:: Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    ECHO Error: Python is not found. Please install Python 3.11 or higher from python.org.
    PAUSE
    EXIT /B
)

:: Check if venv exists, if not create it
IF NOT EXIST "venv" (
    ECHO First time setup: Creating virtual environment...
    python -m venv venv
    ECHO Installing dependencies...
    venv\Scripts\pip install -r requirements.txt
    ECHO Setup complete!
    ECHO.
)

:: Launch the game
:: Using pythonw to hide the console window after launch
START venv\Scripts\pythonw.exe main.py

EXIT
