import cv2
import numpy
from matplotlib import pyplot as plt
import os.path


img = cv2.imread("C:\\Users\\Raymon\\Documents\\Universidad\\Primavera_2018\\EL5202 - Laboratorio de Sistemas Digitales\\Proyecto\\imgs\\moneda_10_pesos\\an_15g.jpg",0)

clahe = cv2.createCLAHE(clipLimit=40, tileGridSize=(25,25))
cl1 = clahe.apply(img)

plt.imshow(cl1,cmap='gray')
plt.show()

cl1 = cv2.medianBlur(cl1,31)

plt.imshow(cl1,cmap='gray')
plt.show()

darkest = cl1.min()
brightest = cl1.max()
print darkest
print brightest

thrs1 = darkest+(0.15)*(brightest-darkest)
thrs2 = darkest+(0.4)*(brightest-darkest)

edges = cv2.Canny(cl1,thrs1,thrs2,101,L2gradient=False)

print thrs1
print thrs2




plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Imagen original'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges,cmap='gray')
plt.title('Despues de Canny'), plt.xticks([]), plt.yticks([])
plt.show()
