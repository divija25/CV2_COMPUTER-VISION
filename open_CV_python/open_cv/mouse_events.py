# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 07:19:34 2020

@author: Divija Ayala
"""
import cv2

def click_events(events,x,y,flags,param):
    if events==cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        font=cv2.FONT_HERSHEY_COMPLEX
        text=str(x)+" "+str(y)
        cv2.putText(img, text, (x,y), font, 0.5, (0,255,0),1,cv2.LINE_AA)
        cv2.imshow('image',img)
        
    if events==cv2.EVENT_RBUTTONDBLCLK:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        font=cv2.FONT_HERSHEY_COMPLEX
        text=str(blue)+" "+str(green)+" "+str(red)
        cv2.putText(img, text, (x,y), font, 0.5, (0,255,0),1,cv2.LINE_AA)
        cv2.imshow('image',img)
        
        
        
img=cv2.imread("gradient.png",-1)
#-1 unchanged
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_events)

cv2.waitKey(0) 
cv2.destroyAllWindows()