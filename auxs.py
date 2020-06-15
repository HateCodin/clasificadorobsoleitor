import numpy as np
import cv2

#distancia euclideana
def dist(x1,y1,x2,y2):
    return np.sqrt((y2-y1)**2+(x2-x1)**2)


#dice si el  punto (x,y) pertenece a el circululo de centro (a,b) y radio r
def esta_en_el_circulo(x,y,a,b,r):
    return dist(x,y,a,b)<=r


def hough(imagen,ratio,minDist,parametro1,parametro2,minRad,maxRad):
    # p1: imagen, p2: metodo (solo hay uno), p3: razon entre la resolucion de la imagen y el acumulador,
    # p4: dist minima entre centros, p5: umbral superior al detector canny (el menor es la mitad),
    # p6: umbral de deteccion de centros, mientras menor es, mas se detectan, p7: radio minimo,
    # p8: radio maximo
    circunferencia = cv2.HoughCircles(imagen,cv2.HOUGH_GRADIENT,ratio,minDist,param1=parametro1,param2=parametro2,minRadius=minRad,maxRadius=maxRad)
    while circunferencia is None:
        parametro2 = parametro2-1;
        circunferencia = cv2.HoughCircles(imagen,cv2.HOUGH_GRADIENT,ratio,minDist,param1=parametro1,param2=parametro2,minRadius=minRad,maxRadius=maxRad)
    circunferencia = np.uint16(np.around(circunferencia[0,0,::]))
    return circunferencia

def encuadra(imagen, circunferencia):
    ulc_x = circunferencia[0]-circunferencia[2]                 #coordenada x de la upper left corner
    ulc_y = circunferencia[1]-circunferencia[2]                 #coordenada y de la upper left corner
    lrc_x = circunferencia[0]+circunferencia[2]                 #coordenada x de la lower right corner
    lrc_y = circunferencia[1]+circunferencia[2]                 #coordenada y de la lower right corner

    return imagen[ulc_y:lrc_y:1, ulc_x:lrc_x:1]