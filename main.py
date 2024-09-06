# import cv2
# from cvzone.HandTrackingModule import HandDetector

# cap=cv2.VideoCapture(0)
# cap.set(3,1280)
# cap.set(4,720)


# detector=HandDetector(detectionCon=0.8)
# startDist=None
# scale=0
# cx,cy=500,500

# while True:
#     success, img=cap.read()
#     hands,img=detector.findHands(img)
#     img1=cv2.imread("OIP.jpeg")
    
#     if len(hands)==2:
#         #print(detector.fingersUp(hands[0]),detector.fingersUp(hands[1]))
#         if detector.fingersUp(hands[0])==[1,1,0,0,0]and\
#             detector.fingersUp(hands[1])==[1,1,0,0,0]:
#                 #print("Zoom Gesture")
#                 lmList1=hands[0]["lmList"]
#                 lmList2=hands[1]["lmList"]
                
#                 if startDist is None:
#                 #lmList1[8],lmList2[8]
                
#                     length,info,img=detector.findDistance(lmList1[8],lmList2[8],img)
#                     print(length)
#                     startDist=length
                    
#                     length, info, img=detector.findDistance(lmList[8],lmList2[8],img)
#                     length, info, img=detector.findDistance(hands[0]["center"],hands[1]["center"],img)
                    
#                     scale=int((length-startDist)//2)
#                     cx,cy=info[4:]
#                     print(scale)
#                 else:
#                     startDist=None
                
#                 try:    
#                     h1,w1,_=img1.shape
#                     newH,newW=((h1+scale)//2)*2,((w1+scale)//2)*2
#                     img1=cv2.resize(img1,(newW,newH))
#                 except:
#                      pass
        
        
#                 img[cy-newH//2:cy+newH//2,cx-newW//2:cx+newW//2]=img1
#                 cv2.imshow("Image",img)
#                 cv2.waitKey(1)



import cv2
from cvzone.HandTrackingModule import HandDetector

# Initialize video capture and window size
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Width
cap.set(4, 720)   # Height

# Initialize hand detector
detector = HandDetector(detectionCon=0.8)
startDist = None
scale = 0
cx, cy = 500, 500

# Load the image to be zoomed
img1 = cv2.imread("OIP.jpeg")

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)  # Detect hands
    
    if len(hands) == 2:
        # Check if both hands show the zoom gesture (index finger and thumb up)
        if detector.fingersUp(hands[0]) == [1, 1, 0, 0, 0] and \
           detector.fingersUp(hands[1]) == [1, 1, 0, 0, 0]:
            
            # Get landmark positions of index fingers (tip of index fingers)
            lmList1 = hands[0]["lmList"]
            lmList2 = hands[1]["lmList"]
            
            # Calculate distance between index fingers
            if startDist is None:
                length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)
                startDist = length  # Set the initial distance
            else:
                length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)
                scale = int((length - startDist) // 2)  # Calculate scale based on distance difference
                cx, cy = info[4:]  # Get the center coordinates between both hands
                print(scale)
        else:
            startDist = None  # Reset start distance if hands are not in zoom gesture
    
    # Try to resize the image based on the calculated scale
    try:
        h1, w1, _ = img1.shape
        newH, newW = ((h1 + scale) // 2) * 2, ((w1 + scale) // 2) * 2  # Ensure even dimensions
        img1_resized = cv2.resize(img1, (newW, newH))
        
        # Overlay the resized image onto the video feed
        img[cy - newH // 2:cy + newH // 2, cx - newW // 2:cx + newW // 2] = img1_resized
    except Exception as e:
        print("Error:", e)
    
    # Show the result
    cv2.imshow("Image", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
