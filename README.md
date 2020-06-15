# ClasificadorObsoleitor

## Acerca del proyecto

	Un clasificador automático de monedas chilenas usando una red neuronal multicapa. Este proyecto fue realizado en el contexto de una asignatura para la universidad con el objetivo de aprender de manera práctica sobre inteligencia computacional. Este trabajo se basa en un paper de Khashman et. al. (ver referencias) y utiliza un perceptrón multicapa como motor del sistema inteligente.


## El hardware

### Estructura mecánica
	Usando la vieja y confiable fuente de inspiración (plagio) de Youtube, se copia un mecanismo para extraer de a una las monedas desde un recipiente. Como primera aproximación se prototipa con cartón. Esto es lo que se denomina la etapa 1. A continuación esta la etapada 2 que consiste en dos discos concéntricos que permite posicionar la moneda frente a la cámara. Por último se tiene la tercera etapa que consiste en un rampa orientable.

### Electrónica

	* Raspberry Pi 3
	* Arduino Uno
	* Cámara Raspberry Pi 2
### Extras

	* Micro servos 9g
	* Mucho cartón
	* Silicona caliente


## El software

	El código que corre en el raspberry pi es programado en python usando las librerías de sci-kit learn, y lo que corre en el arduino se usa el IDE de arduino y librerias de servo motores.
