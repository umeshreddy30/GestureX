import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
import time

st.set_page_config(page_title="Sign Language AI", page_icon="✋", layout="wide")

st.sidebar.title("⚙️ Settings")
detect_conf = st.sidebar.slider("Min Detection Confidence", 0.0, 1.0, 0.5)
track_conf = st.sidebar.slider("Min Tracking Confidence", 0.0, 1.0, 0.5)

st.title("✋ Edge AI Dashboard")

col1, col2 = st.columns([3, 1])
with col1:
    stframe = st.empty()
with col2:
    st.write("Status Log:")
    log_text = st.empty()

def run_app():
    # Attempt to fix camera connection
    cap = cv2.VideoCapture(1) # <--- TRY CHANGING THIS TO 1 IF IT FAILS
    
    if not cap.isOpened():
        log_text.error("❌ Error: Camera 0 not found.")
        st.error("Could not access webcam. Please change 'VideoCapture(0)' to '1' in app.py")
        return

    log_text.success("✅ Camera Connected!")
    
    mp_hands = mp.solutions.hands
    mp_draw = mp.solutions.drawing_utils
    hands = mp_hands.Hands(
        min_detection_confidence=detect_conf,
        min_tracking_confidence=track_conf
    )

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            log_text.warning("⚠️ Reading frame failed (Camera might be busy/disconnected).")
            break
            
        # Resize to improve performance
        frame = cv2.resize(frame, (640, 480))
        
        # Color conversion BGR -> RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        results = hands.process(frame)
        
        if results.multi_hand_landmarks:
            for hand_lms in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_lms, mp_hands.HAND_CONNECTIONS)

        stframe.image(frame, channels="RGB", use_container_width=True)

    cap.release()

if st.button('🚀 START CAMERA'):
    run_app()