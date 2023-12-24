import cv2 as cv
import mediapipe as mp

def detect_finger_joints(image):
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)
    mp_drawing = mp.solutions.drawing_utils
    results = hands.process(image)