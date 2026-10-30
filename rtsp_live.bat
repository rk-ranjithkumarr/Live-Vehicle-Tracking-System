@echo off
title LIVE CCTV Vehicle Tracking

call venv\Scripts\activate

set /p CAMERA_URL=Enter RTSP/IP camera URL: 

python live_vehicle_tracking.py --source "%CAMERA_URL%"

pause
