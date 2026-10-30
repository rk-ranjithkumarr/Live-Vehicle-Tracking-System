from ultralytics import YOLO
import cv2
import argparse
import time

# Exact COCO vehicle classes
VEHICLE_CLASSES = {
    1: "bicycle",
    2: "car",
    3: "motorcycle",
    5: "bus",
    6: "train",
    7: "truck",
}

def main():
    parser = argparse.ArgumentParser(
        description="Real-time multi-vehicle detection and tracking"
    )
    parser.add_argument(
        "--source",
        default="0",
        help="0 for webcam, video device index, or RTSP/IP camera URL"
    )
    parser.add_argument(
        "--conf",
        type=float,
        default=0.35,
        help="Detection confidence threshold"
    )
    args = parser.parse_args()

    source = int(args.source) if args.source.isdigit() else args.source

    print("Loading YOLO model...")
    model = YOLO("yolo11n.pt")

    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        raise RuntimeError(
            f"Cannot open camera/source: {args.source}"
        )

    print("LIVE VEHICLE TRACKING STARTED")
    print("Press Q to quit.")

    previous_time = time.time()

    while True:
        ret, frame = cap.read()

        if not ret:
            print("No frame received. Camera/source may have stopped.")
            break

        results = model.track(
            frame,
            persist=True,
            classes=list(VEHICLE_CLASSES.keys()),
            tracker="bytetrack.yaml",
            conf=args.conf,
            verbose=False
        )

        result = results[0]
        annotated = result.plot()

        vehicle_counts = {name: 0 for name in VEHICLE_CLASSES.values()}

        if result.boxes is not None and result.boxes.cls is not None:
            class_ids = result.boxes.cls.int().cpu().tolist()

            for class_id in class_ids:
                if class_id in VEHICLE_CLASSES:
                    vehicle_counts[VEHICLE_CLASSES[class_id]] += 1

        total = sum(vehicle_counts.values())

        # FPS
        current_time = time.time()
        fps = 1.0 / max(current_time - previous_time, 1e-6)
        previous_time = current_time

        # Information panel
        cv2.rectangle(
            annotated,
            (10, 10),
            (310, 205),
            (0, 0, 0),
            -1
        )

        cv2.putText(
            annotated,
            f"LIVE VEHICLES: {total}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        cv2.putText(
            annotated,
            f"Car: {vehicle_counts['car']}",
            (20, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (255, 255, 255),
            1
        )

        cv2.putText(
            annotated,
            f"Motorcycle: {vehicle_counts['motorcycle']}",
            (20, 95),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (255, 255, 255),
            1
        )

        cv2.putText(
            annotated,
            f"Bus: {vehicle_counts['bus']}",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (255, 255, 255),
            1
        )

        cv2.putText(
            annotated,
            f"Truck: {vehicle_counts['truck']}",
            (20, 145),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (255, 255, 255),
            1
        )

        cv2.putText(
            annotated,
            f"FPS: {fps:.1f}",
            (20, 180),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (255, 255, 255),
            1
        )

        cv2.imshow("LIVE Vehicle Tracking System", annotated)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Live tracking stopped.")

if __name__ == "__main__":
    main()
