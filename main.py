import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)
startDist = None
scale = 0
cx, cy = 500, 500

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img) 
    img1 = cv2.imread("C:/Users/uhche/Desktop/ZoomGesture/VirtualZoomGesture/image.jpg")
    
    if img1 is None:
        print("Error: Could not load image.")
        continue
    
    img1_resized = cv2.resize(img1, (250, 250))
    
   
    if 0 <= cx - 125 and 0 <= cy - 125 and cx + 125 <= img.shape[1] and cy + 125 <= img.shape[0]:
        img[cy-125:cy+125, cx-125:cx+125] = img1_resized
    
    if len(hands) == 2:
        if detector.fingersUp(hands[0]) == [1, 1, 0, 0, 0] and\
           detector.fingersUp(hands[1]) == [1, 1, 0, 0, 0]:
            lmList1 = hands[0]["lmList"]  
            lmList2 = hands[1]["lmList"] 
            
            length, info, img = detector.findDistance(lmList1[8][0:2], lmList2[8][0:2], img)

            print(length)
            
            if startDist is None:
                startDist = length
                length, info, img = detector.findDistance(lmList1[8][0:2], lmList2[8][0:2], img)
                scale = int((length - startDist) // 2)
                cx, cy = info[4:]  
                print(scale)
            else:
                startDist = None
       
                h1, w1, _ = img1.shape
                newH, newW = ((h1 + scale) // 2) * 2, ((w1 + scale) // 2) * 2  
                img1_resized = cv2.resize(img1, (newW, newH))
                
                
                if 0 <= cx - newH // 2 and 0 <= cy - newW // 2 and cx + newH // 2 <= img.shape[1] and cy + newW // 2 <= img.shape[0]:
                    img[cy-newH//2:cy+newH//2, cx-newW//2:cx+newW//2] = img1_resized
                
                length, info, img = detector.findDistance(lmList1[8][0:2], lmList2[8][0:2], img)
                print(scale)
                print(f"Scale: {scale}, Center: ({cx}, {cy})")


    cv2.imshow("Image", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
