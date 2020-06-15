import cv2
import numpy as np
import re
from matplotlib import pyplot as plt
from sklearn.neural_network import MLPClassifier


lista_archivos = open('lista_entrenadora.txt','r')
contador = 0
for linea in lista_archivos:
    if contador==0:
        datos_imagenes = np.load(linea.rstrip())
    else:
        sample_actual = np.load(linea.rstrip())
        datos_imagenes = np.vstack((datos_imagenes,sample_actual))
    contador = contador+1
lista_archivos.close()

n_samples, n_first_layer = datos_imagenes.shape
etiquetas_imagenes = np.zeros((n_samples,))
ind = 0
lista_etiquetas = open('lista_etiquetas.txt','r')
for linea in lista_etiquetas:
    etiquetas_imagenes[ind] = float(linea.rstrip())
    ind = ind+1

lista_etiquetas.close()

print 'hola'