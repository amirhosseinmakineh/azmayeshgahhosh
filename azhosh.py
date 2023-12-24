    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            for finger in mp_hands.HandLandmark:
                joint = hand_landmarks.landmark[finger]
                joint_x = int(joint.x * image.shape[1])
                joint_y = int(joint.y * image.shape[0])
                cv.circle(image, (joint_x, joint_y), 5, (0, 255, 0), -1)
    
    return image