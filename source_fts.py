import cv2
import mediapipe as mp
import face_recognition

# Initialize Mediapipe Face Detection
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
"""arduinoSerial=serial.Serial(port="/dev/cu.usbserial-0001",baudrate=9600,timeout=0.5) 
"""
# Open webcam
cap = cv2.VideoCapture(0)

with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue
        # Convert the frame to RGB
        frame_width = frame.shape[1]
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(frame_rgb)
        frame_height, frame_width, _ = frame.shape
        # Draw face detections
        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(frame, detection)
                keypoints = detection.location_data.relative_keypoints

                # Calculate the average of the keypoints
                avg_x, avg_y = 0, 0
                for keypoint in keypoints:
                    x = int(keypoint.x * frame_width)
                    y = int(keypoint.y * frame_height)
                    avg_x += x
                    avg_y += y
                avg_x /= len(keypoints)
                avg_y /= len(keypoints)
                angle=(avg_x/frame_width)*180
                #arduinoSerial.write(f"{angle}\n".encode("utf-8"))
                print(angle)
                # Display the average point
                cv2.circle(frame, (int(avg_x), int(avg_y)), 8, (0, 255, 0), -1)   

        cv2.imshow('Mediapipe Face Detection', frame)

        if cv2.waitKey(1)== ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
