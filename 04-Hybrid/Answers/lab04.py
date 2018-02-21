#!/usr/bin/env python

import cv2
import os
from scipy import misc
import numpy as np

image1 = os.getcwd() + '/Imgs/baby.jpg'
image2 = os.getcwd() + '/Imgs/cat.jpg'

Baby = cv2.imread(image1,0)
Cat = cv2.imread(image2,0)

x,y = 500,500

Baby = cv2.resize(Baby, (x,y))
Cat = cv2.resize(Cat, (x,y))

BabyBlur = cv2.GaussianBlur(Baby, (35,35), 0)
CatBlur = cv2.GaussianBlur(Cat, (45,45), 0)

High = Cat - CatBlur

Hybrid = High + BabyBlur

misc.imsave('Hybrid_filter.png', Hybrid)

I = cv2.resize(Hybrid, (200,200))
I1 = cv2.resize(cv2.pyrDown(I), (200,200))
I2 = cv2.resize(cv2.pyrDown(I1), (200,200))
I3 = cv2.resize(cv2.pyrDown(I2), (200,200))
I4 = cv2.resize(cv2.pyrDown(I3), (200,200))

f = np.concatenate((I,I1,I2,I3,I4),axis=1)

misc.imsave('Pyramid.png', f)
