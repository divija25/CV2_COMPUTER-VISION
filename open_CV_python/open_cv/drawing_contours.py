# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 16:08:25 2021

@author: Divija Ayala
"""

#curve joining all the continuous points (along the boundary),
# having same color or intensity

#Contours are essentially the shapes of objects in an image.
import cv2
img=cv2.imread("opencv_logo.png")
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_,thresh=cv2.threshold(gray, 120, 255,0)

'''contours is a Python list of all the contours in the image. Each individual contour
# is a Numpy array of (x,y) coordinates of boundary points of the object.'''
contours,hierarchy=cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#first one is source image, 
#second is contour retrieval mode,
# third is contour approximation method.

print("number of contours=" + str(len(contours)))

#cv2.drawContours(image, contours, contourIdx, color)
cv2.drawContours(img, contours, -1, (0,255,255),3)

cv2.imshow("image",img)
cv2.imshow("gray",gray)
cv2.imshow("thresh",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()