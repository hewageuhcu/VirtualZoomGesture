import cv2
from cvzone.HandDTrackingModule import HandDetector
cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)


detector=HandDetector(detectionCon=0.8)

while True:
    success, img=cap.read()
    hands,img=detector.findHands(img)
    cv2.imshow("Image",img)
    cv2.waitKey(1)