import cv2
import numpy as np,sys
import os

image1 = os.getcwd() + '/Imgs/cat.jpg'
image2 = os.getcwd() + '/Imgs/baby.jpg'

A = cv2.imread(image1,0)
B = cv2.imread(image2,0)

x,y = 500,500

A = cv2.resize(A, (x,y))
B = cv2.resize(B, (x,y))

# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in xrange(4):
    G = cv2.pyrDown(G)
    gpA.append(G)

# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in xrange(4):
    G = cv2.pyrDown(G)
    gpB.append(G)

# generate Laplacian Pyramid for A
lpA = [gpA[4]]
for i in xrange(4,0,-1):
    GE = cv2.pyrUp(gpA[i])
    L = cv2.subtract(cv2.resize(gpA[i-1],GE.shape),GE)
    lpA.append(L)

# generate Laplacian Pyramid for B
lpB = [gpB[4]]
for i in xrange(4,0,-1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(cv2.resize(gpB[i-1],GE.shape),GE)
    lpB.append(L)

# Now add left and right halves of images in each level
LS = []
for la,lb in zip(lpA,lpB):
    rows,cols = la.shape
    ls = np.hstack((la[:,0:cols/2], lb[:,cols/2:]))
    LS.append(ls)

# now reconstruct
ls_ = LS[0]
for i in xrange(1,4):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, cv2.resize(LS[i],ls_.shape))

# image with direct connecting each half
real = np.hstack((A[:,:cols/2],B[:,cols/2:]))

cv2.imwrite('Pyramid_blending2.jpg',ls_)
cv2.imwrite('Direct_blending.jpg',real)
