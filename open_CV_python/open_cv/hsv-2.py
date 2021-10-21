# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 07:39:46 2020

@author: Divija Ayala
"""
import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('tracking')
cap=cv2.VideoCapture(0)
cv2.createTrackbar('LH', 'tracking', 0, 255, nothing)
cv2.createTrackbar('LS', 'tracking', 0, 255, nothing)
cv2.createTrackbar('LV', 'tracking', 0, 255, nothing)
cv2.createTrackbar('UH', 'tracking', 255, 255, nothing)
cv2.createTrackbar('US', 'tracking', 255, 255, nothing)
cv2.createTrackbar('UV', 'tracking', 255, 255, nothing)

while(1):
    #frame=cv2.imread('ball.jpg')
    check,frame=cap.read()
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    l_h=cv2.getTrackbarPos('LH', 'tracking')
    l_s=cv2.getTrackbarPos('LS', 'tracking')
    l_v=cv2.getTrackbarPos('LV', 'tracking')
    u_h=cv2.getTrackbarPos('UH', 'tracking')
    u_s=cv2.getTrackbarPos('US', 'tracking')
    u_v=cv2.getTrackbarPos('UV', 'tracking')
    
    lower_range=np.array([l_h,l_s,l_v])
    upper_range=np.array([u_h,u_s,u_v])
    
    masks=cv2.inRange(hsv,lower_range,upper_range)
    
    result=cv2.bitwise_and(frame,frame,mask=masks)
    
    cv2.imshow('frame',frame)
    cv2.imshow('masks',masks)
    cv2.imshow('result',result)
    
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    