from auxs import *
from matplotlib import pyplot as plt
import cv2


imagen = cv2.imread("C:\\Users\\Raymon\\Documents\\Universidad\\Primavera_2018\\EL5202 - Laboratorio de Sistemas Digitales\\Proyecto\\imgs\\moneda_100_pesos\\an_15g.jpg",0)
plt.figure()
plt.imshow(imagen,cmap='gray')
plt.show()
circ = hough(imagen,1,80,40,35,50,180)
cv2.circle(imagen,(circ[0],circ[1]),circ[2],(255,0,0),3)
plt.figure()
plt.imshow(imagen,cmap='gray')
plt.show()
imagen_encuadrada = encuadra(imagen,circ)
plt.figure()
plt.imshow(imagen_encuadrada,cmap='gray')
plt.show()