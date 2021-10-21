# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 13:33:24 2020

@author: Divija Ayala
"""

import cv2
img=cv2.imread("C:\\Users\\divija\\Pictures\\just_do_it.jpg",0)

img=cv2.line(img,(100,100),(10,250),(255,255,0),10)
#total 5 paramters
#1-target image
#2,3--coordinates
#4-colour in bgr format
#5-thickness

img=cv2.circle(img, (300,300), 50, (255,255,0),-1)
#2-centre
#3-radius

img=cv2.rectangle(img, (150,50), (250,250), (255,255,0),-1)

#adding text
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, 'dv', (150,150), font, 10, (255,255,0),10,cv2.LINE_AA)
#3-coordinates
#5-fontsize
#7-thickness
#8-linetype

cv2.imshow('figure',img)
cv2.waitKey(0)
cv2.destroyAllWindows()