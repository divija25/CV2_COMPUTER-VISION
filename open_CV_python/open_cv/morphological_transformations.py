# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 19:05:29 2021

@author: Divija Ayala
"""
# normally performed on binary images
#It needs two inputs, one is our original image,
# second one is called structuring element or kernel
# which decides the nature of operation.
import cv2
from matplotlib import pyplot as plt
import numpy as np

img=cv2.imread("smarties.png",0)
#img=cv2.imread("j.png",0)
img1=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# matplot requires img in rgb 

_,mask=cv2.threshold(img1, 220, 255, cv2.THRESH_BINARY_INV)
kernel=np.ones((5,5),np.uint8)

#A pixel in the original image will be considered 1 only if all the pixels under the kernel is 1, otherwise it is eroded (made to zero).
#all the pixels near boundary will be discarded depending upon the size of kernel. 
erosion=cv2.erode(mask, kernel,iterations=1)

#It is just opposite of erosion. Here, a pixel element is ‘1’
# if atleast one pixel under the kernel is ‘1’
dilation=cv2.dilate(mask,kernel,iterations=2)

#Opening is just another name of erosion followed by dilation
opening=cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

#Closing is reverse of Opening, Dilation followed by Erosion.
closing=cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

#it is the difference between dilation and erosion of an image.
#The result will look like the outline of the object.
gradient=cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)

images=[img1,mask,erosion,dilation,opening,closing,gradient] 
titles=['original','mask','erosion','dilation','opening','closing','gradient']

for i in range(7):
    plt.subplot(3,3,1+i),plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()