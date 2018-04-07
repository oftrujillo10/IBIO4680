#!/usr/bin/env python

import cv2
import numpy as np
import os
from scipy import misc

image1 = os.getcwd() + '/Imgs/cat.jpg'
image2 = os.getcwd() + '/Imgs/baby.jpg'

s,z = 500, 500

Cat = cv2.imread(image1,0)
Cat = cv2.resize(Cat, (s,z))
fcat = np.fft.fft2(Cat)
fscat = np.fft.fftshift(fcat)

Baby = cv2.imread(image2,0)
Baby = cv2.resize(Baby, (s,z))
fbaby = np.fft.fft2(Baby)
fsbaby = np.fft.fftshift(fbaby)

a = 2
x,y = Cat.shape
crow,ccol = x/2 , y/2
fscat[crow-a:crow+a, ccol-a:ccol+a] = 0

b = 15
m = np.zeros((x,y))
m[crow-b:crow+b, ccol-b:ccol+b] = 1

fsbaby = fsbaby*m

f_iscat = np.fft.ifftshift(fscat)
img_cat = np.fft.ifft2(f_iscat)
img_cat = np.abs(img_cat)

f_isbaby = np.fft.ifftshift(fsbaby)
img_baby = np.fft.ifft2(f_isbaby)
img_baby = np.abs(img_baby)

Hybrid = img_baby + img_cat

misc.imsave('hybrid_fft2.png', Hybrid)

I = cv2.resize(Hybrid, (200,200))
I1 = cv2.resize(cv2.pyrDown(I), (200,200))
I2 = cv2.resize(cv2.pyrDown(I1), (200,200))
I3 = cv2.resize(cv2.pyrDown(I2), (200,200))
I4 = cv2.resize(cv2.pyrDown(I3), (200,200))

f = np.concatenate((I,I1,I2,I3,I4),axis=1)

misc.imsave('Pyramid_fft2.png', f)
