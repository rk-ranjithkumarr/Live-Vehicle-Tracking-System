@echo off
title LIVE Vehicle Tracking - Setup

echo ==========================================
echo    LIVE VEHICLE TRACKING SYSTEM
echo ==========================================
echo.

python --version
if errorlevel 1 (
    echo Python was not found in PATH.
    echo Install Python 3.11 and try again.
    pause
    exit /b 1
)

if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

call venv\Scripts\activate

echo.
echo Upgrading pip...
python -m pip install --upgrade pip

echo.
echo Installing libraries...
pip install -r requirements.txt

echo.
echo Setup complete.
echo.
pause
