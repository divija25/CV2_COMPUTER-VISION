# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 13:05:13 2020

@author: Divija Ayala
"""

import cv2
cap=cv2.VideoCapture(0)#default camera

while (True):
    check,frame=cap.read()
    
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('gray',gray)
    
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()