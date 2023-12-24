cap = cv.VideoCapture(0)

while True:
    # خواندن تصویر از دوربین
    ret, frame = cap.read()
    
    # تشخیص مفاصل انگشتان
    frame = detect_finger_joints(frame)
    
    # نمایش تصویر
    cv.imshow('Finger Joints Detection', frame)
    
    # خروجی از برنامه در صورت فشردن دکمه 'q'
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


# آزاد کردن منابع
cap.release()
cv2.destroyAllWindows()