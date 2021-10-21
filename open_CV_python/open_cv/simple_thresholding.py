# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 10:03:56 2020

@author: Divija Ayala
"""

import cv2

# If pixel value is greater than a threshold value,
# it is assigned one value (may be white), 
#else it is assigned another value (may be black).

img=cv2.imread('gradient.png',0) #should be a gray scale image
_,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#Second argument is the threshold value which is used to classify the pixel values.
#Third argument is the maxVal which represents the value to be given if pixel value is more than (sometimes less than) the threshold value.

_,th2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
_,th3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
_,th4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)


cv2.imshow('image',img)
cv2.imshow('th1',th1)
cv2.imshow('th2',th2)
cv2.imshow('th3',th3)
cv2.imshow('th4',th4)

cv2.waitKey(0)
cv2.destroyAllWindows()
