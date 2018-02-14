#!/usr/bin/env python

import wget
import numpy as np
import tarfile
import os.path as path
import os
import random
from PIL import Image
import scipy.misc as sc
from scipy import misc
import scipy.io as sio
from time import time

tiempo_inicial = time()

# Se descarga la base de datos

if not path.exists('BSR_bsds500.tgz'):
	url = 'http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/BSR/BSR_bsds500.tgz'
	wget.download(url)

# Se descomprime el archivo

if not path.exists('BSR'):
	tar = tarfile.open('BSR_bsds500.tgz')
	tar.extractall()
	tar.close()

ruta1 = os.getcwd() + '/BSR/BSDS500/data/images/test'
ruta2 = os.getcwd() + '/BSR/BSDS500/data/groundTruth/test'
contenido = os.listdir(ruta1)

# Se buscan 8 imagenes aleatorias al igual que sus anotaciones

for i in range(8):
  a = random.choice(contenido)
  b = a.replace('.jpg','.mat')
  im = Image.open(ruta1 + '/'  +  a)
  an = sio.loadmat(ruta2 + '/'  +  b)
  anr1 = an['groundTruth'][0][0]['Boundaries'][0][0]
  anr2 = an['groundTruth'][0][0]['Segmentation'][0][0]
  ant1 = anr1.astype('int')
  ant2 = anr2.astype('int')

  if i == 0:
   c = sc.imresize(im, [100, 100])
   d1 = sc.imresize(ant1, [100, 100])
   d2 = sc.imresize(ant2, [100, 100])
  else:
   imn = sc.imresize(im, [100, 100])
   ann1 = sc.imresize(ant1, [100, 100])
   ann2 = sc.imresize(ant2, [100, 100])
   c = np.concatenate((c, imn), axis=1)
   d1 = np.concatenate((d1, ann1), axis=1)
   d2 = np.concatenate((d2, ann2), axis=1)

# Se arman las imagenes de tres canales para concatenar

bn = np.zeros((100 ,800, 3))
bn[:, :, 0] = d1
bn[:, :, 1] = d1
bn[:, :, 2] = d1

sn = np.zeros((100 ,800, 3))
sn[:, :, 0] = d2
sn[:, :, 1] = d2
sn[:, :, 2] = d2

# Se guarda la imagen resultante

f = np.concatenate((c, bn, sn), axis=0)
misc.imsave('resultado.png', f)

tiempo_final = time()
tiempo_ejecucion = tiempo_final - tiempo_inicial

print 'El tiempo de ejecucion fue:',tiempo_ejecucion
