# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 07:14:25 2020

@author: Divija Ayala
"""

import cv2
import numpy as np


while(1):
    frame=cv2.imread('ball.jpg')
    
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # define range of blue color in HSV
    lower_blue=np.array([110,50,50])
    upper_blue=np.array([130,255,255])
    
    # Threshold the HSV image to get only blue colors
    masks=cv2.inRange(hsv, lower_blue, upper_blue)
    
    result=cv2.bitwise_and(frame, frame,mask=masks)
    
    cv2.imshow('frames',frame)
    cv2.imshow('masks',masks)
    cv2.imshow('result',result)
    
    k=cv2.waitKey(0)
    if k==ord('q'):
        break
    
cv2.destroyAllWindows()