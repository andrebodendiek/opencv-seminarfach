import cv2 

from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon=0.8)

cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)

# Initial position of rectangle
cX, cY, w, h = (400, 400, 100, 100)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    if success == True:
      hands, img = detector.findHands(img)
      # hands = detector.findHands(img, draw=False)

      if hands:
        position = hands[0]['center']
        lmList = hands[0]['lmList']
        cursor = lmList[8]
        if cX - w // 2 < cursor[0] < cX + w // 2 and \
          cY - h // 2 < cursor[1] < cY + h // 2:
          cX, cY, _ = cursor
      
      cv2.rectangle(img, 
                    (cX - w // 2, cY - h // 2), 
                    (cX + w // 2, cY + h // 2), 
                    (255, 0, 0), 
                    cv2.FILLED)

      cv2.imshow("Image", img)
      
      if cv2.waitKey(1) and 0xFF == ord('q'):
         break

    else:
       break
    
cap.release()
cv2.destroyAllWindows()