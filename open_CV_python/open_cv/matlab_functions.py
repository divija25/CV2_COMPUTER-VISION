# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 08:29:25 2021

@author: Divija Ayala
"""

import cv2
from matplotlib import pyplot as plt

img=cv2.imread('gradient.png',0)

img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

_,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
_,th2=cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_,th3=cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_,th4=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)

titles=['binary','binary_inv','tozero','trunc']
images=[th1,th2,th3,th4]
for i in range(4):
    plt.subplot(2,2,1+i),plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    

plt.show()