import cv2
import numpy as np
from playsound import playsound
import threading

cam = cv2.VideoCapture(0)
buzzing = False
while True:
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    bframe1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    bframe2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    threshold = 1450000
    difference = cv2.absdiff(bframe1, bframe2)
    cv2.imshow('Your Web Cam', frame2)
    difference_sum = np.sum(difference)
    if difference_sum >= threshold and not buzzing:
        thread = threading.Thread(target=playsound, args=['beep.wav'])
        thread.start()
        buzzing = True
        continue
    buzzing = False
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
