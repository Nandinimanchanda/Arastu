import cv2
import mediapipe as mp
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import pyautogui
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
#etector = HandDetector(detectionCon=0.8, maxHands=1)

screen_width, screen_height = pyautogui.size()
index_y = 0
resultText=""
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()
def Draw(x,y,text):
    cv2.rectangle(frame,(x,y),(x+100,y+100),(255,0,255),cv2.FILLED)
    cv2.putText(frame,text,(x+15,y+80),cv2.FONT_HERSHEY_PLAIN,5,(255,255,255),5)

while True:
    # Read a frame from the camera
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    
    Draw(100,100,"Q")
    Draw(210,100,"W")
    Draw(320,100,"E")
    Draw(430,100,"R")
    Draw(540,100,"T")
    Draw(650,100,"Y")
    Draw(760,100,"U")
    Draw(870,100,"I")
    Draw(980,100,"O")
    Draw(1090,100,"P")
    

    
    Draw(140,220,"A")
    Draw(250,220,"S")
    Draw(360,220,"D")
    Draw(470,220,"F")
    Draw(580,220,"G")
    Draw(690,220,"H")
    Draw(800,220,"J")
    Draw(910,220,"K")
    Draw(1020,220,"L")
    
    Draw(210,340,"Z")
    Draw(320,340,"X")
    Draw(430,340,"C")
    Draw(540,340,"V")
    Draw(650,340,"B")
    Draw(760,340,"N")
    Draw(870,340,"M")
    Draw(980, 340, "Backspace")
    cv2.rectangle(frame,(980,340),(1080,440),(255,0,255),cv2.FILLED)
    cv2.putText(frame,"Back",(980+15,340+80),cv2.FONT_HERSHEY_PLAIN,5,(255,255,255),5)
    
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                if id == 8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y

                if id == 12:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    print('outside', abs(index_y - thumb_y))
                    if abs(index_y - thumb_y) < 20:
                        if 100< x <200 and 100<y<200 :
                            resultText=resultText+"Q"
                            pyautogui.sleep(0.5)   
                        elif 210<x<310 and 100<y<200 : 
                          resultText=resultText+"W"
                          pyautogui.sleep(0.5)
                        elif 320<x<420 and 100<y<200 : 
                          resultText=resultText+"E"
                          pyautogui.sleep(0.5)
                        elif 430<x<530 and 100<y<200 : 
                          resultText=resultText+"R"
                          pyautogui.sleep(0.5)
                        elif 540<x<640 and 100<y<200 : 
                          resultText=resultText+"T"
                          pyautogui.sleep(0.5)
                        elif 650<x<750 and 100<y<200 : 
                          resultText=resultText+"Y"
                          pyautogui.sleep(0.5)
                        elif 760<x<860 and 100<y<200 :
                          resultText=resultText+"U"
                          pyautogui.sleep(0.5)
                        elif 870<x<970 and 100<y<200 : 
                          resultText=resultText+"I"
                          pyautogui.sleep(0.5)
                        elif 980<x<1080 and 100<y<200 : 
                          resultText=resultText+"O"
                          pyautogui.sleep(0.5)
                        elif 1090<x<1190 and 100<y<200 : 
                          resultText=resultText+"P"
                          pyautogui.sleep(0.5)
                        elif 140<x<240 and 220<y<320 : 
                          resultText=resultText+"A"
                          pyautogui.sleep(0.5)
                        elif 250<x<350 and 220<y<320 : 
                          resultText=resultText+"S"
                          pyautogui.sleep(0.5)
                        elif 360<x<460 and 220<y<320 : 
                          resultText=resultText+"D"
                          pyautogui.sleep(0.5)
                        elif 470<x<570 and 220<y<320 : 
                          resultText=resultText+"F"
                          pyautogui.sleep(0.5)
                        elif 580<x<680 and 220<y<320 : 
                          resultText=resultText+"G"
                          pyautogui.sleep(0.5)
                        elif 690<x<790 and 220<y<320 : 
                          resultText=resultText+"H"
                          pyautogui.sleep(0.5)
                        elif 800<x<900 and 220<y<320 : 
                          resultText=resultText+"J"
                          pyautogui.sleep(0.5)
                        elif 910<x<1010 and 220<y<320 : 
                          resultText=resultText+"K"
                          pyautogui.sleep(0.5)
                        elif 1020<x<1120 and 220<y<320 : 
                          resultText=resultText+"L"
                          pyautogui.sleep(0.5)
                        elif 210<x<310 and 340<y<440 : 
                          resultText=resultText+"Z"
                          pyautogui.sleep(0.5)
                        elif 320<x<420 and 340<y<440 : 
                          resultText=resultText+"X"
                          pyautogui.sleep(0.5)
                        elif 430<x<530 and 340<y<440 : 
                          resultText=resultText+"C"
                          pyautogui.sleep(0.5)
                        elif 540<x<640 and 340<y<440 : 
                          resultText=resultText+"V"
                          pyautogui.sleep(0.5)
                        elif 650<x<750 and 340<y<440 : 
                          resultText=resultText+"B"
                          pyautogui.sleep(0.5)
                        elif 760<x<860 and 340<y<440 : 
                          resultText=resultText+"N"
                          pyautogui.sleep(0.5)
                        elif 870<x<970 and 340<y<440 : 
                          resultText=resultText+"M"
                          pyautogui.sleep(0.5)
                        elif 980 < x < 1080 and 340 < y < 440:
                          resultText = resultText[:-1]
                          pyautogui.press('backspace')
                          pyautogui.sleep(0.5)

                    elif abs(index_y - thumb_y) < 100:
                        pass
                      #  pyautogui.moveTo(index_x, index_y)    
    cv2.rectangle(frame,(100,460),(900,560),(255,0,255),cv2.FILLED) 
    cv2.putText(frame,resultText,(115,540),cv2.FONT_HERSHEY_PLAIN,5,(255,255,255),5) 
                         
    cv2.imshow('Virtual Keyboard', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    #cv2.resizeWindow('Virtual Keyboard', 1500, 1200)

    cv2.waitKey(1)