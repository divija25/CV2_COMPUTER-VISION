# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 08:36:30 2021
@author: Divija Ayala
"""


''' You can consider histogram as a graph or plot, which gives you an overall idea 
about the intensity distribution of an image. It is a plot with pixel values
 (ranging from 0 to 255, not always) in X-axis and corresponding number of pixels
 in the image on Y-axis.'''
 
#Left region of histogram shows the amount of darker pixels in image and 
#right region shows the amount of brighter pixels.i

import cv2
from matplotlib import pyplot as plt
import numpy as np

#img=np.zeros((200,200),np.uint8)   #black image
img=cv2.imread("opencv_logo.png")
#cv2.rectangle(img, (0,100), (200,200), 255,-1)
#cv2.imshow("image",img)

b,g,r=cv2.split(img)
cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)
#plt.hist(img.ravel(),256,[0,256])

plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])  #bgr plot
plt.hist(r.ravel(),256,[0,256])


'''ravel function flattens the array
#2-bins-subpart
#3-range of pixels'''
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()



