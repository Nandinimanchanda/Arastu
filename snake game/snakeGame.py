import math
import random
import cv2
import numpy as np
import cvzone
from cvzone.HandTrackingModule import HandDetector

class SnakeGameClass():
    def __init__(self, pathFood):
        self.points = []
        self.lengths = []
        self.currentLength = 0
        self.allowedLength = 150
        self.previousHead = 0, 0

        self.imgFood = cv2.imread(pathFood, cv2.IMREAD_UNCHANGED)
        self.hFood, self.wFood, _ = self.imgFood.shape
        self.foodPoint = 0, 0
        self.randomFoodLocation()

        self.score = 0
        self.gameOver = False

    def randomFoodLocation(self):
        self.foodPoint = random.randint(100, 1000), random.randint(100, 600)

    def update(self, frameMain, currentHead):
        if self.gameOver:
            cvzone.putTextRect(frameMain, "Game Over", [300, 400], scale=7, thickness=5, offset=20)
            cvzone.putTextRect(frameMain, f'Your Score: {self.score}', [300, 550], scale=7, thickness=5, offset=20)
        else:
            px, py = self.previousHead
            cx, cy = currentHead

            self.points.append([cx, cy])
            distance = math.hypot(cx - px, cy - py)
            self.lengths.append(distance)
            self.currentLength += distance
            self.previousHead = cx, cy

            # Length reductions
            if self.currentLength > self.allowedLength:
                for i, length in enumerate(self.lengths):
                    self.currentLength -= length
                    self.lengths.pop(i)
                    self.points.pop(i)
                    if self.currentLength < self.allowedLength:
                        break

            # Check if snake ate the food
            rx, ry = self.foodPoint
            if rx - self.wFood // 2 < cx < rx + self.wFood // 2 and \
                    ry - self.hFood // 2 < cy < ry + self.hFood // 2:
                self.randomFoodLocation()
                self.allowedLength += 50
                self.score += 1
                print(self.score)

            # Check for collisions
            pts = np.array(self.points[:-2], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(frameMain, [pts], False, (0, 200, 0), 3)

            # Draw snake
            if self.points:
                for i, point in enumerate(self.points):
                    if i != 0:
                        cv2.line(frameMain, self.points[i - 1], self.points[i], (0, 0, 255), 20)
                cv2.circle(frameMain, self.points[-1], 20, (200, 0, 200), cv2.FILLED)

            cvzone.putTextRect(frameMain, f'Score: {self.score}', [50, 80], scale=3, thickness=3, offset=10)

            # Draw food
            rx, ry = self.foodPoint
            frameMain = cvzone.overlayPNG(frameMain, self.imgFood, (rx - self.wFood // 2, ry - self.hFood // 2))

            # Check for collisions
            pts = np.array(self.points[:-2], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(frameMain, [pts], False, (0, 200, 0), 3)
            minDist = cv2.pointPolygonTest(pts, (cx, cy), True)
            print(minDist)

            if -1 <= minDist <= 1:
                print("hit")
                self.gameOver = True
                self.points = []
                self.lengths = []
                self.currentLength = 0
                self.allowedLength = 150
                self.previousHead = 0, 0
                self.randomFoodLocation()
                

        return frameMain

# Open the default camera (camera index 0)
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8, maxHands=1)

game = SnakeGameClass("D:\\python 3.8\\projects\\Donut.png")

# Check if the camera was opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hands, frame = detector.findHands(frame, flipType=False)

    if hands:
        lmList = hands[0]['lmList']
        pointIndex = lmList[8][0:2]
        frame = game.update(frame, pointIndex)

    # Check if the frame was read successfully
    if not ret:
        print("Error: Could not read frame.")
        break

    # Display the frame
    cv2.imshow("Camera", frame)

    # Check for key events
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('n'):
        # Start a new game
        game.gameOver = False
        game.points = []
        game.lengths = []
        game.currentLength = 0
        game.allowedLength = 150
        game.previousHead = 0, 0
        game.randomFoodLocation()
        game.score = 0
    

# Release the camera capture object and close the window
cap.release()
cv2.destroyAllWindows()
