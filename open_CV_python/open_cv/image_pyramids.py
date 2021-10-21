# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 11:31:00 2021

@author: Divija Ayala
"""

# set of images with different resolution are called Image Pyramids 
#(because when they are kept in a stack with biggest image at bottom
# and smallest image at top look like a pyramid).

#There are two kinds of Image Pyramids.
# 1) Gaussian Pyramid and 2) Laplacian Pyramids

import cv2
#from matplotlib import pyplot as plt

img=cv2.imread("smarties.png")
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

lower_resolution=cv2.pyrDown(img)
lower_resolution2=cv2.pyrDown(lower_resolution)

#higher_resolution is not equal to img, because once you decrease 
#the resolution, you loose the information.
higher_resolution=cv2.pyrUp(lower_resolution)


cv2.imshow('original',img)
cv2.imshow('lower_resolution',lower_resolution)
cv2.imshow('lower_resolution2',lower_resolution2)
cv2.imshow('higher_resolution',higher_resolution)

cv2.waitKey(0)
cv2.destroyAllWindows()

