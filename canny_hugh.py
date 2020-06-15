import cv2
from matplotlib import pyplot as plt
import numpy as np
from auxs import *

img = cv2.imread("C:\\Users\\Raymon\\Documents\\Universidad\\Primavera_2018\\EL5202 - Laboratorio de Sistemas Digitales\\Proyecto\\imgs\\moneda_100_pesos\\an_90gc.png",0)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

clahe = cv2.createCLAHE(clipLimit=19, tileGridSize=(18,18))
cl1 = clahe.apply(img)

plt.imshow(cl1,cmap='gray')
plt.show()

cl1 = cv2.medianBlur(cl1,7)

plt.imshow(cl1,cmap='gray')
plt.show()

darkest = cl1.min()
brightest = cl1.max()
print darkest
print brightest

thrs1 = darkest+(0.25)*(brightest-darkest)
thrs2 = darkest+(0.4)*(brightest-darkest)

#p1: imagen, p2: umbral menor, p3: umbral mayor, p4: tamanio sobel, p5: usar dradiente exacto o approximado (default
# aproximado Flase)
edges = cv2.Canny(cl1,thrs1,thrs2,3,L2gradient=True)




plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(200*edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()

circles = hough(cl1,1,80,40,60,50,180)
#circles = cv2.HoughCircles(cl1,cv2.HOUGH_GRADIENT,1,80,
                            #param1=40,param2=60,minRadius=50,maxRadius=180)

circles = np.uint16(np.around(circles))

    # draw the outer circle
cv2.circle(cimg,(circles[0],circles[1]),circles[2],(0,255,0),2)
    # draw the center of the circle
cv2.circle(cimg,(circles[0],circles[1]),2,(0,0,255),3)

plt.imshow(cimg,cmap='gray')
plt.show()
cv2.imshow('detected circles',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
