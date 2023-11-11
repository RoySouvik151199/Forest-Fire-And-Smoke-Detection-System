import cv2
from playsound import playsound

fire_detector_cascade = cv2.CascadeClassifier('fire_detection_model.xml')
video_capture = cv2.VideoCapture(0)

while True:
    ret, current_frame = video_capture.read()
    gray_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
    
    detected_fires = fire_detector_cascade.detectMultiScale(current_frame, scaleFactor=1.2, minNeighbors=5)

    for (x, y, w, h) in detected_fires:
        cv2.rectangle(current_frame, (x-10, y-10), (x+w+10, y+h+10), (0, 255, 0), 3)
        region_of_interest_gray = gray_frame[y:y+h, x:x+w]
        region_of_interest_color = current_frame[y:y+h, x:x+w]
        print("Fire detected!")
        playsound('fire_alarm.mp3')

    cv2.imshow('Fire Detection', current_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
