from auxs import *
from matplotlib import pyplot as plt
import cv2
from sklearn.externals import joblib
import copy
import picamera


clf = joblib.load('red_entrenada.sav')
camara = picamera.PiCamera()
clahe = cv2.createCLAHE(clipLimit=40, tileGridSize=(17, 17))  # ecualizador de histograma

while True:
    in_cmd = raw_input('Comando? (0:clasificar, 1:detener)')
    if in_cmd==1: break
    camara.start_preview()
    in_cmd = raw_input()
    if in_cmd==1: break
    camara.capture('img.jpg')
    camara.stop_preview()
    imagen = cv2.imread('img.jpg',0)
    plt.figure()
    plt.imshow(imagen, cmap='gray')
    plt.title('linea 12')
    plt.show()
    imagen = clahe.apply(imagen)  # ecualizacion de histograma
    plt.figure()
    plt.imshow(imagen, cmap='gray')
    plt.title('linea 17')
    plt.show()
    imagen2 = copy.copy(imagen)
    imagen2 = cv2.medianBlur(imagen2, 7)

    circ = hough(imagen2, 1, 80, 40, 120, 73, 165)
    cv2.circle(imagen2, (circ[0], circ[1]), circ[2], (255, 0, 0), 3)
    plt.figure()
    plt.imshow(imagen2, cmap='gray')
    plt.title('linea 28')
    plt.show()

    h, w = imagen.shape

    # centros de la imagen
    centro_X = circ[1]
    centro_Y = circ[0]

    # radio
    radio = circ[2]

    # binarizacion de la imagen
    for i in xrange(h):
        for j in xrange(w):
            if not esta_en_el_circulo(i, j, centro_X, centro_Y, radio):
                imagen[i][j] = 255
            else:
                if imagen[i][j] >= 127:
                    imagen[i][j] = 255
                else:
                    imagen[i][j] = 0

    # graficar moneda binarizada
    plt.figure()
    plt.imshow(imagen, cmap='gray')
    plt.title('linea 49')
    plt.show()

    imagen = encuadra(imagen, circ)

    # graficar moneda encuadrada
    plt.figure()
    plt.imshow(imagen, cmap='gray')
    plt.title('linea 60')
    plt.show()

    h, w = imagen.shape
    # reescalamiento
    w_target = 125
    escala = 1.0 * w_target / w
    img = cv2.resize(imagen, None, fx=escala, fy=escala, interpolation=cv2.INTER_AREA)

    # graficar moneda reescalada
    plt.figure()
    plt.imshow(img, cmap='gray')
    plt.title('linea 71')
    plt.show()

    w, h = img.shape
    centro_X, centro_Y = w / 2, h / 2
    esi_x = centro_X - 40
    esi_y = centro_Y - 40

    imagen_recortada = img[esi_x:esi_x + 81, esi_y:esi_y + 81]

    # graficar moneda recortada
    plt.figure()
    plt.imshow(imagen_recortada, cmap='gray')
    plt.title('linea 84')
    plt.show()

    TP_x, TP_y = imagen_recortada.shape
    S = 256
    D = TP_x * TP_y / S

    fnl_img = np.zeros((16, 16))
    k = 0
    for i in xrange(16):
        for j in xrange(16):
            sum_i = 0
            for k in xrange(5):
                for l in xrange(5):
                    sum_i += imagen_recortada[5 * i + k][5 * j + l]
            fnl_img[i][j] = 1.0 * sum_i / D / 256

    plt.figure()
    plt.imshow(fnl_img, cmap='gray')
    plt.title('linea 104')
    plt.show()

    input_layer = fnl_img.flatten('F')

    print clf.predict(input_layer.reshape(1, -1))
