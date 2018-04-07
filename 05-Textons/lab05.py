import sys
import os
import cv2
import numpy as np
import scipy.io as sio

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from time import time

sys.path.append('lib/python')

inicio = time()

#Create a filter bank with deafult params
from fbCreate import fbCreate
fb = fbCreate()

#Load sample images from disk

ruta1 = 'img/Datos/train/'

a = os.listdir(ruta1)
b = sorted(a)

train = []

for n in range(len(b)):
        f = cv2.imread(ruta1 + b[n], 0)
        f = cv2.resize(f, (200, 200))
        train.append(f)

#Set number of clusters
k = 50

#Apply filterbank to sample image
from fbRun import fbRun

g = np.hstack((train[0],train[1]))

for n in range(len(train)-2):
        g = np.hstack((g,train[n+2]))

filterResponses = fbRun(fb,g)

#Computer textons from filter
from computeTextons import computeTextons
map, textons = computeTextons(filterResponses, k)

#Load more images

ruta2 = 'img/Datos/test/'

a = os.listdir(ruta2)
b = sorted(a)

test = []

for n in range(len(b)):
        e = cv2.imread(ruta2 + b[n], 0)
        e = cv2.resize(e, (200, 200))
        test.append(e)

#Calculate texton representation with current texton dictionary
from assignTextons import assignTextons

tmapTrain = []

for n in range(len(train)):
	r = assignTextons(fbRun(fb,train[n]),textons.transpose())
	tmapTrain.append(r)

tmapTest = []

for n in range(len(test)):
        z = assignTextons(fbRun(fb,test[n]),textons.transpose())
        tmapTest.append(z)

final = time()

#Check the euclidean distances between the histograms and convince yourself that the images of the goats are closer because they have similar texture pattern

# --> Can you tell why we need to create a histogram before measuring the distance? <---

def histc(X, bins):
    import numpy as np
    map_to_bins = np.digitize(X,bins)
    r = np.zeros(bins.shape)
    for i in map_to_bins:
        r[i-1] += 1
    return np.array(r)


X = []

for n in range(len(tmapTrain)):
	D1 = np.linalg.norm(histc(tmapTrain[n].flatten(), np.arange(k))/tmapTrain[n].size)
	X.append([D1])

sio.savemat('Train.mat', {'X': X})

T = []

for n in range(len(tmapTest)):
	D2 = np.linalg.norm(histc(tmapTest[n].flatten(), np.arange(k))/tmapTest[n].size)
	T.append([D2])

sio.savemat('Test.mat', {'T': T})

ejecucion = final - inicio

print (ejecucion)
