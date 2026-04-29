@echo off
echo Starting HTML to JPG Converter...
echo.

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH.
    pause
    exit /b 1
)


:: Run the script
uv run main.py

pause