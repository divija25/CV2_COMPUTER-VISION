# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 16:04:37 2020

@author: Divija Ayala
"""

import cv2
import datetime
cap=cv2.VideoCapture(0) #defaullt cam

while(True):
    check,frame=cap.read()
    
    text=str(datetime.datetime.now())
    font=cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame, text, (10,50), font, 1, (255,0,0),1,cv2.LINE_AA)
    
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF== ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()