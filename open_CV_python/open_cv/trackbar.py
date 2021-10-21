# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 18:43:03 2020

@author: Divija Ayala
"""

import cv2
import numpy as np

def nothing(x):
    print(x)


img=np.zeros((512,512,3),np.uint8)

cv2.namedWindow('IMAGE')


cv2.createTrackbar('B', 'IMAGE', 0, 255, nothing)
cv2.createTrackbar('G', 'IMAGE', 0, 255, nothing)
cv2.createTrackbar('R', 'IMAGE', 0, 255, nothing)


cv2.imshow('IMAGE',img)

cv2.waitKey(0) 
cv2.destroyAllWindows()