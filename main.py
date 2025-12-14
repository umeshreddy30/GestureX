import cv2
import mediapipe as mp
import sys
import time

def main():
    print(f"✅ AI System Loading... (Python {sys.version.split()[0]})")
    
    # Initialize Hand Tracking
    mp_hands = mp.solutions.hands
    mp_draw = mp.solutions.drawing_utils
    hands = mp_hands.Hands(
        min_detection_confidence=0.5, 
        min_tracking_confidence=0.5
    )

    # Open Camera
    print("📷 Opening Webcam...")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Error: Could not open webcam.")
        print("   -> Try changing 'cv2.VideoCapture(0)' to 1 or 2 in main.py")
        input("Press Enter to exit...")
        return

    print("✨ System Ready! Press 'q' to stop.")

    p_time = 0

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

        # Calculate FPS
        c_time = time.time()
        fps = 1 / (c_time - p_time) if (c_time - p_time) > 0 else 0
        p_time = c_time
        
        # Display Text
        cv2.putText(img, f'FPS: {int(fps)}', (10, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        cv2.imshow("Sign Language AI", img)

        # Exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()