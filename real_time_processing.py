import cv2
from fog_removal import enhance_image
from object_detection import detect_objects

def process_video_stream():
    cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)  # Use AVFoundation backend

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image")
            break

        enhanced_frame = enhance_image(frame)
        if enhanced_frame is None:
            print("Error: Failed to enhance image")
            break

        results = detect_objects(enhanced_frame)
        if results is None:
            print("Error: Failed to detect objects")
            break

        # Display results
        for *box, conf, cls in results.xyxy[0].tolist():
            x1, y1, x2, y2 = map(int, box)
            label = f'{results.names[int(cls)]} {conf:.2f}'
            cv2.rectangle(enhanced_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(enhanced_frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow('Object Detection', enhanced_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()