import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
success, img = cap.read()
h, w, _ = img.shape

detector = HandDetector(maxHands=1, detectionCon=0.5)

while True:
    # Get image frame
    success, img = cap.read()
    # Find the hand and its landmarks
    hands, img = detector.findHands(img)
    cv2.imshow("image",img)
    cv2.waitKey(1)