import sys

# 1. Robust Import Check
try:
    import cv2
    import mediapipe as mp
    import numpy as np
except ImportError as e:
    print("\n" + "="*40)
    print("❌ CRITICAL ERROR: Library not found")
    print(f"Missing: {e.name}")
    print("Please run: pip install opencv-python mediapipe numpy")
    print("="*40 + "\n")
    sys.exit(1)

def main():
    print(f"✅ Python Version: {sys.version.split()[0]}")
    print("✅ Libraries loaded successfully. Attempting to open camera...")

    # Initialize MediaPipe
    mp_hands = mp.solutions.hands
    mp_draw = mp.solutions.drawing_utils
    hands = mp_hands.Hands(
        max_num_hands=2,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )

    # Open Camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Error: Camera not found. If using Docker, webcam is not supported by default.")
        return

    print("🎥 Camera Active! Press 'q' to exit.")

    while True:
        success, img = cap.read()
        if not success:
            continue

        # Convert to RGB for MediaPipe
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)

        # Draw Landmarks
        if results.multi_hand_landmarks:
            for hand_lms in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(img, hand_lms, mp_hands.HAND_CONNECTIONS)
                
                # Get Index Finger Tip (ID 8)
                h, w, c = img.shape
                cx, cy = int(hand_lms.landmark[8].x * w), int(hand_lms.landmark[8].y * h)
                cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

        cv2.imshow("Sign Language AI", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()