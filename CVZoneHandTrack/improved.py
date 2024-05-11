import cv2
import time
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller

class HandGestureController:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 640)
        self.cap.set(4, 480)
        self.detector = HandDetector(detectionCon=0.9, maxHands=1)
        self.keyboard = Controller()

    def detect_hand_gestures(self):
        if not self.cap.isOpened():
            print("Error: Unable to open camera.")
            return

        while True:
            ret, img = self.cap.read()
            if not ret:
                print("Error: Unable to capture frame.")
                break

            hands, img = self.detector.findHands(img)

            if hands:
                finger = self.detector.fingersUp(hands[0])
                self.process_hand_gestures(finger)
            else:
                self.release_keys()

            cv2.imshow("Hand Gestures", img)
            if cv2.waitKey(1) == ord("q"):
                break

        cv2.destroyAllWindows()
        self.cap.release()

    def process_hand_gestures(self, finger):
        # Process hand gestures and control keyboard
        if finger == [0, 0, 0, 0, 0]:  # No fingers up
            self.keyboard.press('s')
            self.release_keys()
        elif finger == [1, 1, 1, 1, 1]:  # All fingers up
            self.keyboard.press('w')
            self.release_keys()

        elif finger == [0, 0, 1, 0, 0]:  # Middle finger up
            self.keyboard.press('a')
            self.keyboard.release('d')
            self.keyboard.release(Key.shift)
        elif finger == [1, 0, 0, 0, 0]:  # Thumb up
            self.keyboard.press('d')
            self.release_keys()
        elif finger == [0, 1, 0, 0, 1]:  # Index and pinky fingers up
            self.keyboard.press(Key.shift)
        elif finger == [0, 1, 1, 1, 0]:  # Index and ring fingers up
            self.keyboard.press('f')
            self.release_keys()
            time.sleep(0.5)

    def release_keys(self):
        # Release all pressed keys
        self.keyboard.release('w')
        self.keyboard.release('a')
        self.keyboard.release('s')
        self.keyboard.release('d')
        self.keyboard.release('f')
        self.keyboard.release(Key.shift)

if __name__ == "__main__":
    controller = HandGestureController()
    controller.detect_hand_gestures()
