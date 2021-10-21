# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 07:34:15 2021

@author: Divija Ayala
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("sudoko.png",0)

#If you want to detect both edges, keep the output datatype to some higher forms,
# like cv2.CV_16S, cv2.CV_64F etc, take its absolute value and
# then convert back to cv2.CV_8U(uint8)
lap=cv2.Laplacian(img, cv2.CV_64F,ksize=3)
lap=np.uint8(np.absolute(lap))

#Sobel operators is a joint Gausssian smoothing plus differentiation 
#operation, so it is more resistant to noise. You can specify the
# direction of derivatives to be taken, vertical or horizontal
# by the arguments
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=-1)
sobelx=np.uint8(np.absolute(sobelx))

sobely=cv2.Sobel(img, cv2.CV_64F, 0, 1,ksize=-1)
sobely=np.uint8(np.absolute(sobely))

sobel_combined=cv2.bitwise_or(sobelx, sobely)

titles=['image','laplacian','sobelx','sobely','sobel_combined']
images=[img,lap,sobelx,sobely,sobel_combined]

for i in range(5):
    plt.subplot(2,3,1+i),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()