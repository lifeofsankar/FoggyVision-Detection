# test_camera.py
import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    print("Camera opened successfully.")
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Camera Test', frame)
        else:
            print("Error: Failed to capture image")
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()