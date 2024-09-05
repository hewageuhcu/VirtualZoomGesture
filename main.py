import cv2
from cvzone.HandTrackingModule import HandDetector

cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)


detector=HandDetector(detectionCon=0.8)

while True:
    success, img=cap.read()
    hands,img=detector.findHands(img)
    img1=cv2.imread("OIP.jpeg")
    
    if len(hands)==2:
        print("Zoom Gesture")
        print(detector.fingersUp(hands[0]),detector.fingersUp(hands[1]))
    
    img[10:260,10:260]=img1
    cv2.imshow("Image",img)
    cv2.waitKey(1)