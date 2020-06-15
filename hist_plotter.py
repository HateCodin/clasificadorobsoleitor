#Script para la graficar los histograma de una lista de imagenes en el archivo hits_plotter_list
import cv2
from matplotlib import pyplot as plt

file_hndl = open('hist_plotter_list.txt','r')
for line in file_hndl:
    imagen = cv2.imread(line.rstrip(),0)
    histograma = cv2.calcHist(imagen,[0],None,[256],[0,256])

    plt.figure()
    plt.plot(histograma)
    plt.show()

file_hndl.close()