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
        if finger == [1,1,1,1,1]: # all fingers up
            keyboard.press(Key.space)
            keyboard.release(Key.left)
            keyboard.release(Key.right)
            keyboard.release(Key.down)
            time.sleep(0.3)

        elif finger == [0,1,1,1,1]:
            keyboard.press(Key.down)
            keyboard.release(Key.left)
            keyboard.release(Key.right)
        elif finger == [0,0,0,0,0]:
            keyboard.press(Key.up)
            keyboard.release(Key.left)
            keyboard.release(Key.right)
        elif finger == [0,0,0,0,1]:
            keyboard.press(Key.right)
            keyboard.release(Key.left)
            keyboard.release(Key.up)
            keyboard.release(Key.down)
            time.sleep(0.3)
        elif finger == [1,0,0,0,0]:
            keyboard.press(Key.left)
            keyboard.release(Key.up)
            keyboard.release(Key.right)
            keyboard.release(Key.down)
            time.sleep(0.3)

        elif finger == [0,1,0,0,1]:
            keyboard.press('a')
            keyboard.release(Key.left)
            keyboard.release(Key.right)
            keyboard.release(Key.down)

    else:
        keyboard.release('w')
        keyboard.release('s')
        keyboard.release('a')
        keyboard.release('d')
        keyboard.release('w')
        keyboard.release('f')
        keyboard.release(Key.shift)

    cv2.imshow("left right", img)
    if cv2.waitKey(1) == ord ("q"):
        break

    