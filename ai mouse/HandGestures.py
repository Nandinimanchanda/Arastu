import cv2  
import mediapipe
import pyautogui

capture= mediapipe.solutions.hands.Hands()
drawing=mediapipe.solutions.drawing_utils
camera = cv2.VideoCapture(0)
screen_width,screen_height=pyautogui.size()
X1 = Y1 = X2 = Y2 = 0
while True:
    ret,image=camera.read()
    imag_height,imag_width, _ = image.shape
    image=cv2.flip(image,1)
    rgbImage=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    output=capture.process(rgbImage)
    all_hand=output.multi_hand_landmarks
    if all_hand:
        for hand in all_hand:
            one_hand_landmark=hand.landmark
            for id , lm in enumerate(one_hand_landmark):
                x=int(lm.x * imag_width)
                y=int(lm.y * imag_height)
                # print(x,y)
                if id == 8:
                    mouse_X=int(screen_width / imag_width * x)
                    mouse_Y=int(screen_height / imag_height * y)
                    cv2.circle(image,(x,y),3,(0,255,255))
                    pyautogui.moveTo(mouse_X,mouse_Y)
                    X1=x
                    Y1=y
                if id == 12:
                    X2=x
                    Y2=y
                    cv2.circle(image,(x,y),3,(0,255,255))
        dist=Y2-Y1
        print(dist)
        if dist < 23:
            pyautogui.click()
    cv2.imshow("Hand Movement",image)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()