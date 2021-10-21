# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 08:56:28 2021

@author: Divija Ayala
"""
#5steps
#1)noise reduction
#2)gradient calculation
#3)non-maximum suppression
#4)double threshold
#5)edge tracking by hysteresis
import cv2
from matplotlib import pyplot as plt

img=cv2.imread("sudoko.png",0)

#Edges are the points in an image where the image brightness changes 
#sharply or has discontinuities
#Edges are different from contours as they are not related to objects
# rather they signify the changes in pixel values of an image

#cv2.Canny(image, threshold1, threshold2)
canny=cv2.Canny(img, 100, 200)

images=[img,canny]
titles=['image','canny']

for i in range(2):
    plt.subplot(1,2,1+i),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
plt.show()