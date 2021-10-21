# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 09:17:24 2021

@author: Divija Ayala
"""

#cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])

'''
#channels : given in square brackets. It the index of channel for which we calculate
 histogram. For example, if input is grayscale image, its value is [0]. For color image,
 you can pass [0],[1] or [2] to calculate histogram of blue,green or red channel respectively.

#mask : mask image. To find histogram of full image, it is given as “None”.
 But if you want to find histogram of particular region of image, 
 you have to create a mask image for that and give it as mask. (I will show an example later.)

#histSize : this represents our BIN count. Need to be given in square brackets.
 For full scale, we pass [256].

#ranges : this is our RANGE. Normally, it is [0,256].'''

import cv2
from matplotlib import pyplot as plt

img=cv2.imread("opencv_logo.png",0)

hist=cv2.calcHist(img, [0], None, [256], [0,256])
plt.plot(hist)
plt.show()