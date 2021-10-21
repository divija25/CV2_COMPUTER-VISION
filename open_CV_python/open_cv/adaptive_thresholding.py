# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 07:14:59 2021

@author: Divija Ayala
"""

import cv2

img=cv2.imread('sudoko.png',0)
#calculate the threshold for a small regions of the image. 
#So we get different thresholds for different regions of the same image
# and it gives us better results for images with varying illumination.

_,th1=cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

th2=cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
#cv2.ADAPTIVE_THRESH_MEAN_C : threshold value is the mean of neighbourhood area.

#cv2.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted sum of neighbourhood values where weights are a gaussian window.
th3=cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

#Block Size - It decides the size of neighbourhood area.

#C - It is just a constant which is subtracted from the mean or weighted mean calculated.

cv2.imshow('th1',th1)
cv2.imshow('th2',th2)
cv2.imshow('th3',th3)

cv2.waitKey(0)
cv2.destroyAllWindows()