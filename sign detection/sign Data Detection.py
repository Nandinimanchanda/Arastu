import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

cap = cv2.VideoCapture(0)
detector=HandDetector(maxHands=1)

offset=20
imageSize=300

folder = "D:\python 3.8\projects\sign recogniton2\Data\L"
counter=0

while True:
    success,image=cap.read()
    image=cv2.flip(image,1)
    hands,image=detector.findHands(image)
    if hands:
        hand=hands[0]
        x,y,w,h=hand['bbox']


        imageWhite=np.ones((imageSize,imageSize,3),np.uint8)*255

        imageCrop=image[y-offset:y+h+offset,x-offset:x+w+offset]

        imageCropshape=imageCrop.shape
        aspectratio=h/w
        if aspectratio > 1:
            const=imageSize/h
            calwidth=math.ceil(const*w)
            imageResize=cv2.resize(imageCrop,(calwidth,imageSize))
            imageCropshape=imageResize.shape
            widthGape=math.ceil((imageSize-calwidth)/2)

            imageWhite[:,widthGape:calwidth+widthGape]=imageResize
        else:
            const=imageSize/w
            calheight=math.ceil(const*h)
            imageResize=cv2.resize(imageCrop,(imageSize,calheight))
            imageCropshape=imageResize.shape
            heightGape=math.ceil((imageSize-calheight)/2)

            imageWhite[heightGape:calheight+heightGape,:]=imageResize
        


        cv2.imshow("image Crop" , imageWhite)
    cv2.imshow("image",image)
    key=cv2.waitKey(1)
    if key == ord("s"):
        counter+=1
        cv2.imwrite(f"{folder}\{time.time()}.jpg",imageWhite)
        print(counter)