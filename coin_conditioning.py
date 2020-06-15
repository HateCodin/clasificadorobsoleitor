import cv2
import re
from matplotlib import pyplot as plt
import numpy as np

#distancia euclideana
def dist(x1,y1,x2,y2):
    return np.sqrt((y2-y1)**2+(x2-x1)**2)

#dice si el  punto (x,y) pertenece a el circululo de centro (a,b) y radio r
def esta_en_el_circulo(x,y,a,b,r):
    return dist(x,y,a,b)<=r




#archivo con las imagenes a procesar
lista_imagenes = open('img_list.txt','r')


for linea in lista_imagenes:
    imagen = cv2.imread(linea.rstrip(),0)                           #imagen abierta en escala de grises
    clahe = cv2.createCLAHE(clipLimit=40, tileGridSize=(17,17))     #ecualizador de histograma
    imagen = clahe.apply(imagen)                                    #ecualizacion de histograma


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



    arr_str = re.split('\\\\',linea)
    nombre = arr_str[-1]

    #reescalamiento
    w_target = 125
    escala = 1.0*w_target/w
    img = cv2.resize(imagen,None,fx=escala,fy=escala,interpolation=cv2.INTER_AREA)


    w,h = img.shape
    centro_X, centro_Y = w/2, h/2
    esi_x = centro_X-40
    esi_y = centro_Y-40

    imagen_recortada = img[esi_x:esi_x+81,esi_y:esi_y+81]

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

    plt.imshow(fnl_img,cmap='gray')
    plt.show()

    out_img_name = arr_str[-1].replace('.png','_procesado.png')
    out_array_name = arr_str[-1].replace('.png','_vectorizado')
    out_img_path = linea.replace(arr_str[-1],out_img_name)
    out_array_path = linea.replace(arr_str[-1],out_array_name)
    cv2.imwrite(out_img_path.rstrip(),fnl_img)

    input_layer = fnl_img.flatten('F')
    np.save(out_array_path.rstrip(),input_layer)



lista_imagenes.close()