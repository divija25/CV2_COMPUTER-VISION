# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 14:19:34 2021

@author: Divija Ayala
"""

import cv2
import numpy as np

cap=cv2.VideoCapture(0)
width=800
height=600

cap.set(3,width)
cap.set(4,height)
status,frame1=cap.read()
status,frame2=cap.read()
    
#cv2.imshow("frame1",frame1)
cv2.imshow("frame2",frame2)
while cap.isOpened():
    
    
    difference=cv2.absdiff(frame1, frame2)
    #cv2.imshow("diff",difference)
    
    
    gray=cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("gray",gray)
    
    blur=cv2.GaussianBlur(gray, (21,21), 0)
    #cv2.imshow("blur",blur)
    
    _,thresh=cv2.threshold(blur, 25, 255, cv2.THRESH_BINARY)
    #cv2.imshow("threshold",thresh)
    
    kernel=np.ones((3,3),np.uint8)
    dilated=cv2.dilate(thresh,kernel,iterations=5)
    #cv2.imshow("dilation",dilated)
    
    erosion=cv2.erode(dilated,kernel,iterations=5)
    #cv2.imshow("erosion",erosion)
    
    contours,_=cv2.findContours(erosion.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        if cv2.contourArea(contour)<1000:
            continue
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame1, (x,y), (x+w,y+h), (0,255,0),3)
        cv2.putText(frame1, "status:{}".format("movement"), (20,20), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0),2)
    cv2.imshow("contours",frame1)
     
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
    
    frame1=frame2
    status,frame2=cap.read()
    
cv2.destroyAllWindows()
cap.release()