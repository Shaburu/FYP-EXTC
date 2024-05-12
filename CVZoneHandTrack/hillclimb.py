import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller
import time
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
detector = HandDetector(detectionCon= 0.9, maxHands= 1)
keyboard = Controller()

while True:
    _, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        finger = detector.fingersUp(hands[0])
        if finger == [0,0,0,0,0]:
            keyboard.press(Key.right)
            keyboard.release(Key.left)
        elif finger == [1,1,1,1,1]:
            keyboard.press(Key.left)
            keyboard.release(Key.right)

    else:
        keyboard.release(Key.right)
        keyboard.release(Key.left)

    cv2.imshow("left right", img)
    if cv2.waitKey(1) == ord ("q"):
        break
