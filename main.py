import cv2
from cvzone.HandTrackingModule import HandDetector

cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)


detector=HandDetector(detectionCon=0.8)
startDiist=None

while True:
    success, img=cap.read()
    hands,img=detector.findHands(img)
    img1=cv2.imread("OIP.jpeg")
    
    if len(hands)==2:
        #print(detector.fingersUp(hands[0]),detector.fingersUp(hands[1]))
        if detector.fingersUp(hands[0])==[1,1,0,0,0]and\
            detector.fingersUp(hands[1])==[1,1,0,0,0]:
                #print("Zoom Gesture")
                lmList1=hands[0]["lmList"]
                lmList2=hands[1]["lmList"]
                
                if startDist is None:
                #lmList1[8],lmList2[8]
                    length,info,img=detector.findDistance(lmList1[8],lmList2[8],img)
                    print(length)
                    startDisr=length
        
        
    img[10:260,10:260]=img1
    cv2.imshow("Image",img)
    cv2.waitKey(1)