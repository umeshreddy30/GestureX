import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self, mode=False, max_hands=2, detection_con=0.5, track_con=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.detection_con = detection_con
        self.track_con = track_con

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.max_hands,
            min_detection_confidence=self.detection_con,
            min_tracking_confidence=self.track_con
        )
        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, img, draw=True):
        """
        Processes the image and detects hands.
        Returns the image with drawings (optional) and the results object.
        """
        # Convert BGR to RGB for MediaPipe
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_rgb.flags.writeable = False
        
        self.results = self.hands.process(img_rgb)

        img_rgb.flags.writeable = True
        
        if self.results.multi_hand_landmarks:
            for hand_lms in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(
                        img, 
                        hand_lms, 
                        self.mp_hands.HAND_CONNECTIONS,
                        self.mp_draw.DrawingSpec(color=(121, 22, 76), thickness=2, circle_radius=4),
                        self.mp_draw.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2)
                    )
        return img

    def find_position(self, img, hand_no=0):
        """
        Returns a list of landmarks [id, x, y] for a specific hand.
        """
        lm_list = []
        if self.results.multi_hand_landmarks:
            # Check if the requested hand exists
            if len(self.results.multi_hand_landmarks) > hand_no:
                my_hand = self.results.multi_hand_landmarks[hand_no]
                for id, lm in enumerate(my_hand.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lm_list.append([id, cx, cy])
        return lm_list