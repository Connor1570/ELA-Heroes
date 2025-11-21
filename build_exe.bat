@echo off
TITLE Building ELA Heroes...
CLS

ECHO Installing/Updating PyInstaller...
venv\Scripts\pip install pyinstaller

ECHO.
ECHO Building Executable...
ECHO This may take a minute.
venv\Scripts\pyinstaller --noconsole --onefile --name "ELA Heroes" --clean main.py

ECHO.
ECHO Build Complete!
ECHO You can find your game in the "dist" folder.
PAUSE
