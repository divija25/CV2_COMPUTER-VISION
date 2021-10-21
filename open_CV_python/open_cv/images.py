# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 10:41:07 2020

@author: Divija Ayala
"""

import cv2
img=cv2.imread("C:\\Users\\divija\\Pictures\\just_do_it.jpg",0)
cv2.imshow('image',img)

k=cv2.waitKey(0)
if k==ord('s'):
    cv2.imwrite('cv_image.jpg',img)
    cv2.destroyAllWindows()
else:
    cv2.destroyAllWindows()