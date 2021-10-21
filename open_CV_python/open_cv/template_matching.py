# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 11:04:08 2021

@author: Divija Ayala
"""

'''It is basically a method for searching and finding the location of a template image in a larger image.
The idea here is to find identical regions of an image that match a template we provide, giving a threshold
The threshold depends on the accuracy with which we want to detect the template in the source image.
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

rgb_img=