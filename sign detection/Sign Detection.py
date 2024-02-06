import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import tensorflow
import math
import time

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector=HandDetector(maxHands=1)
Classifer=Classifier("D:\python 3.8\projects\sign recogniton2\Model\keras_model.h5","D:\python 3.8\projects\sign recogniton2\Model\labels.txt")


offset=20
imageSize=300

folder = "Data\A"
counter=0

labels=["A","C","HELLO","HOW ARE YOU","YES","I AM FINE"]
labels2=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
while True:
    success,image=cap.read()
    image=cv2.flip(image,1)
    imageOutput=image.copy()
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
            predection,index=Classifer.getPrediction(imageWhite)
            print(predection,index)

        else:
            const=imageSize/w
            calheight=math.ceil(const*h)
            imageResize=cv2.resize(imageCrop,(imageSize,calheight))
            imageCropshape=imageResize.shape
            heightGape=math.ceil((imageSize-calheight)/2)

            imageWhite[heightGape:calheight+heightGape,:]=imageResize
            predection,index=Classifer.getPrediction(imageWhite)

        cv2.rectangle(imageOutput,(x-offset+10,y-offset-50),(x-offset+100,y-offset-50+50),(255,255,0),cv2.FILLED)
        cv2.putText(imageOutput,labels[index],(x+15,y-30),cv2.FONT_HERSHEY_COMPLEX,1.7,(255,0,0),2)
        cv2.rectangle(imageOutput,(x-offset,y-offset),(x+w+offset,y+h+offset),(255,255,0),4)


        cv2.imshow("image Crop" , imageWhite)
    cv2.imshow("image",imageOutput)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    
    cv2.waitKey(1)