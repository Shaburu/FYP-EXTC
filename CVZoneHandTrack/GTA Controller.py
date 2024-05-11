import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
detector = HandDetector(detectionCon= 0.7, maxHands= 1)
keyboard = Controller()

while True:
    _, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        finger = detector.fingersUp(hands[0])
        if finger == [0,0,0,0,0]:
            keyboard.press('w')
            keyboard.release('s')
            keyboard.release('a')
            keyboard.release('d')

        elif finger == [1,1,1,1,1]:
            keyboard.press('s')
            keyboard.release('w')
        elif finger == [0,0,1,0,0]:
            keyboard.press('a')
            keyboard.release('d')
        elif finger == [1,0,0,0,0]:
            keyboard.press('d')
            keyboard.release('a')

    else:
        keyboard.release('w')
        keyboard.release('s')

    cv2.imshow("left right", img)
    if cv2.waitKey(1) == ord ("q"):
        break