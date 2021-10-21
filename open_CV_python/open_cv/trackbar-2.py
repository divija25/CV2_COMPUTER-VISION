# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 18:56:33 2020

@author: Divija Ayala
"""

import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')

def nothing(x):
    print(x)

switch='0 : OFF \n1 : ON'
cv2.createTrackbar('switch', 'image', 0, 1, nothing)

cv2.createTrackbar('B', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('R', 'image', 0, 255, nothing)
while (1):
    
    cv2.imshow('image',img)
    k=cv2.waitKey(1) & 0xFF
    if k==ord('q'):
        break
    
    b=cv2.getTrackbarPos('B', 'image')
    g=cv2.getTrackbarPos('G', 'image')
    r=cv2.getTrackbarPos('R', 'image')
    s=cv2.getTrackbarPos('switch', 'image')
    if s==1:
        img[:]=[b,g,r]
    else:
        img[:]=0
     
cv2.destroyAllWindows()
