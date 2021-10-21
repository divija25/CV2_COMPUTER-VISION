# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 10:36:00 2020

@author: Divija Ayala
"""

import cv2
cap=cv2.VideoCapture(0)#default laptop camera

fourcc=cv2.VideoWriter_fourcc('X','V','I', 'D')
#FourCC is a 4-byte code used to specify the video codec
out=cv2.VideoWriter("outt.avi",fourcc,20.0,(640,480)) 
#20-frames per sec 
#(640,480) size tuple

while(True):
    check,frame=cap.read()  
    #capturing frame by frame  
    #check is a bool value
    
    out.write(frame)
    
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("pic",gray)
    
    if cv2.waitKey(1)==ord("q"):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
        