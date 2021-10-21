# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 19:25:37 2021

@author: Divija Ayala
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("sudoko.png")
img1=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)#matplot rgb format

#using the averaging kernel for image smoothening
kernel=np.ones((5,5),np.float32)/25

#filter2D(src, ddepth, kernel)
dst=cv2.filter2D(img1, -1, kernel)

#simply takes the average of all the pixels under kernel area
# and replaces the central element with this average
#cv2.blur(src, ksize)
averaging=cv2.blur(img1, (5,5))

#instead of a box filter consisting of equal filter coefficients,
# a Gaussian kernel is used
#cv2.GaussianBlur(src, ksize, sigmaX)
gaussian_blur=cv2.GaussianBlur(img1, (5,5), 0)

#computes the median of all the pixels under the kernel window and
# the central pixel is replaced with this median value. 
#This is highly effective in removing salt-and-pepper noise
#cv2.medianBlur(src, ksize)
median_blur=cv2.medianBlur(img1, 5)

#A bilateral filter is used for smoothening images and reducing noise,
# while preserving edges
#d: Diameter of each pixel neighborhood.
#sigmaColor: Value of \sigma in the color space.
# The greater the value, the colors farther to each other will start to get mixed.
#sigmaColor: Value of \sigma in the coordinate space. 
#The greater its value, the more further pixels will mix together, given that their colors lie within the sigmaColor range.
bilateral_filter=cv2.bilateralFilter(img,9,75,75)

titles=['original','2D convolution','average','gaussian','median','bilateral_filter']
images=[img1,dst,averaging,gaussian_blur,median_blur,bilateral_filter]

for i in range(6):
    plt.subplot(2,3,1+i),plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
plt.imshow()
    