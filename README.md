# LIVE Vehicle Tracking System

Real-time vehicle detection and multi-object tracking using YOLO + ByteTrack.

## Exact vehicle names

COCO model classes used:

- bicycle
- car
- motorcycle
- bus
- train
- truck

## Requirements

- Windows 10/11
- Python 3.11.x
- Webcam OR IP/RTSP camera
- Internet connection for first YOLO model download

## Webcam setup

1. Extract the ZIP.
2. Open the project folder.
3. Run `setup.bat`.
4. Run `run_live.bat`.
5. The default camera is device 0.
6. Press Q to stop.

## Command Prompt

```cmd
cd live_vehicle_tracking_system
setup.bat
run_live.bat
```

## CCTV / IP camera

Run:

```cmd
rtsp_live.bat
```

Then enter your RTSP URL, for example:

```text
rtsp://username:password@192.168.1.100:554/stream
```

The exact RTSP path depends on your camera manufacturer.

## Tracking

Each detected vehicle can receive a persistent tracking ID from ByteTrack while it remains trackable.

Example:

```text
car ID 1
car ID 2
truck ID 3
motorcycle ID 4
```

## Future upgrades

- Unique vehicle counting across line crossings
- Direction detection
- Speed estimation with camera calibration
- License plate detection and OCR
- Traffic violation detection
- Database logging
- Web dashboard
- Multiple CCTV cameras
- GPU/CUDA optimization
