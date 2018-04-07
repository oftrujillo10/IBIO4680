import os
import cv2
import numpy as np
import scipy.io as sio

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from time import time

ruta1 = 'img/Datos/train/'

a = os.listdir(ruta1)
b = sorted(a)

c = np.ones(20)
labels = []

for n in range(25):
	d = c*n
	labels = np.concatenate((labels, d))

y = labels

X = sio.loadmat('Train.mat')
X = X['X']

T = sio.loadmat('Test.mat')
T = T['T']

inicial = time()

neigh = KNeighborsClassifier(n_neighbors=25)
neigh.fit(X, y)

r = []

for n in range(len(T)):
	e = neigh.predict([T[n]])
	r = np.concatenate((r, e))

sio.savemat('KNC.mat', {'r': r})

random_forest = RandomForestClassifier(n_estimators=80, max_depth=15, random_state=10)
random_forest.fit(X, y)

s = []

for n in range(len(T)):
        f = random_forest.predict([T[n]])
        s = np.concatenate((s,f))

sio.savemat('RFC.mat', {'s': s})

final = time()

ejecucion = final - inicial

print (ejecucion)
