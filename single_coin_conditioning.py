import cv2
import re
from matplotlib import pyplot as plt
import numpy as np
from auxs import *


#nombre archivo con la imagen a procesar
imagen_dir = 'C:\\Users\\Raymon\\Documents\\Universidad\\Primavera_2018\\EL5202 - Laboratorio de Sistemas Digitales\\Proyecto\\imgs\\moneda_10_pesos\\an_45gc.png'


imagen = cv2.imread(imagen_dir.rstrip(),0)                           #imagen abierta en escala de grises
clahe = cv2.createCLAHE(clipLimit=40, tileGridSize=(17,17))     #ecualizador de histograma
imagen = clahe.apply(imagen)                                    #ecualizacion de histograma

#graficar la moneda histograma ecualizada
plt.figure()
plt.imshow(imagen,cmap='gray')
plt.show()

#guardar
cv2.imwrite('C:\\Users\\Raymon\\Desktop\\moneda_histeq.png',imagen)


tamanio = imagen.shape                                          #tamano imagen
h = tamanio[0]                                                  #altura
w = tamanio[1]                                                  #ancho

#centros de la imagen
centro_X = w/2
centro_Y = h/2

#radio
radio = min(centro_X,centro_Y)

#binarizacion de la imagen
for i in xrange(h):
    for j in xrange(w):
        if not esta_en_el_circulo(i,j,centro_X,centro_Y,radio):
            imagen[i][j] = 255
        else:
            if imagen[i][j] >= 127: imagen[i][j] = 255
            else: imagen[i][j] = 0

#graficar moneda binarizada
plt.figure()
plt.imshow(imagen,cmap='gray')
plt.show()

#guardar
cv2.imwrite('C:\\Users\\Raymon\\Desktop\\moneda_binarizada.png',imagen)

#reescalamiento
w_target = 125
escala = 1.0*w_target/w
img = cv2.resize(imagen,None,fx=escala,fy=escala,interpolation=cv2.INTER_AREA)

#graficar moneda reescalada
plt.figure()
plt.imshow(img,cmap='gray')
plt.show()

#guardar
cv2.imwrite('C:\\Users\\Raymon\\Desktop\\moneda_encogida.png',img)

w,h = img.shape
centro_X, centro_Y = w/2, h/2
esi_x = centro_X-40
esi_y = centro_Y-40

imagen_recortada = img[esi_x:esi_x+81,esi_y:esi_y+81]

#graficar moneda recortada
plt.figure()
plt.imshow(imagen_recortada,cmap='gray')
plt.show()

#guardar
cv2.imwrite('C:\\Users\\Raymon\\Desktop\\moneda_recortada.png',imagen_recortada)

TP_x, TP_y = imagen_recortada.shape
S = 256
D = TP_x*TP_y/S


fnl_img = np.zeros((16,16))
k = 0
for i in xrange(16):
    for j in xrange(16):
        sum_i = 0
        for k in xrange(5):
            for l in xrange(5):
                sum_i += imagen_recortada[5*i+k][5*j+l]
        fnl_img[i][j] = 1.0*sum_i/D/256

plt.figure()
plt.imshow(fnl_img,cmap='gray')
plt.show()

#guardar
cv2.imwrite('C:\\Users\\Raymon\\Desktop\\moneda_conv.png',fnl_img)







