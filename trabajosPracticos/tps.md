# Trabajos Prácticos  
Se realizaron dos trabajos Prácticos durante la cursada
1. Método de Aproximación de Raíces - Trisección
2. Cuadrados Mínimos y Regresion Lineal 

## Método de Aproximación de Raíces - Trisección
Al igual que el método de bisección es un método cerrado, que requiere de un intervalo en el cual esté atrapada la raíz de una función continua. En cada iteración, el intervalo se divide en tres subintervalos de igual longitud.  

#### $$[a, b] \rightarrow [a, c],\ [c, d],\ [d, b]$$  

donde:  
#### $$c = a + \frac{b - a}{3}, \quad d = b - \frac{b - a}{3}$$  

Se evalúa la función en los puntos $a, c, d$ y $b$, y se determina en cuál de los tres subintervalos ocurre un cambio de signo, es decir, debe cumplirse  

#### $$f(x_i) \cdot f(x_{i+1}) < 0$$  

Esto indica que la raíz se encuentra dentro de ese subintervalo. Luego, se actualiza el intervalo para conservar solo ese segmento, y el proceso se repite.

El algoritmo se detiene cuando:
* El tamaño del intervalo es menor a un valor de tolerancia ϵϵ, o
* Se alcanza un número máximo de iteraciones.

[Script del método de Trisección](./methodTrisection.py)

## Cuadrados Mínimos y Regresion Lineal 
[Script de Ejercicio de Cuadrados Mínimos y Regresion Lineal](./CuadradosMinimosYRegresionLineal.ipynb)
