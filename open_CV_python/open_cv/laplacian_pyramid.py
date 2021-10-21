# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 13:36:16 2021

@author: Divija Ayala
"""

import cv2
img=cv2.imread('smarties.png')
layer=img.copy()
#Since Laplacian is a high pass filter, so at each level of this
# pyramid, we will get an edge image as an output

# Laplacian of a level is obtained by subtracting that level in 
#Gaussian Pyramid and expanded version of its upper level in Gaussian Pyramid.

#create a gaussian pyramid
gaussian_pyr=[layer]
for i in range(6):
    layer=cv2.pyrDown(layer)
    gaussian_pyr.append(layer)
    #cv2.imshow(str(i),layer)

layer=gaussian_pyr[5]
#cv2.imshow('upper level gaussian pyr',layer)
laplacian_pyr=[layer]

for i in range(5,0,-1):
    size = (gaussian_pyr[i - 1].shape[1], gaussian_pyr[i - 1].shape[0])
    gaussian_extended=cv2.pyrUp(gaussian_pyr[i],dstsize=size)
    Laplacian=cv2.subtract(gaussian_pyr[i-1], gaussian_extended)
    laplacian_pyr.append(Laplacian)
    cv2.imshow(str(i),Laplacian)

#cv2.imshow('original',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

   