@echo off
echo Starting HTML to JPG Converter...
echo.

@echo off
REM kpi_gen.bat - wrapper to call main.py with a file location and optional file name
REM Usage: html2jpg.bat 
REM Activate the virtual environment
call "%~dp0.venv\Scripts\activate.bat"
REM Change working directory to the script location (project root)
pushd "%~dp0" || (
  echo Failed to change directory to script folder "%~dp0"
  exit /b 1
)

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