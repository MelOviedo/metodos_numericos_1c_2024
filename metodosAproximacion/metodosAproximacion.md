# Métodos de Aproximación de Raíces
1. Método de Bisección
2. Método de Newton Rawson
3. Método de la Secante

## Método Bisección
* Método cerrado.  
* La función a analizar debe ser *CONTINUA* en el intervalo considerado.  
* Requiere un intervalo $[X_l ; X_u]$
    * $X_u \rightarrow$ borde inferior
    * $X_l\rightarrow$  borde superior  
* Este método siempre convege siempre y cuando $f(X_u)f(X_l)<0$  
Esto indica que al menos hay una raíz en el intervalo (Corolario de Bolzano).  
* Se debe ingresar una tolerancia o error aceptable, que define el criterio de parada.  
* Cantidad máxima de iteraciones, para evitar ciclos infinitos.  
* Si el intervalo inicial es muy grande, el método puede tardar más en converger, pero no diverge. Simplemente será menos eficiente.  

[Script del método de Bisección](./metodoBiseccion.py)

## Método Newton-Raphson  
* Es un método abierto, no requiere que la raíz esté encerrada en un intervalo.  
* Es un método rápido y eficiente, con convergencia cuadrática si la estimación inicial es buena y la función es suficientemente suave (derivable).
* Puede divergir si la estimación inicial $x_0$​ está muy lejos de la raíz, si la derivada se anula cerca del punto, o si la función no es bien comportada.  
* Suele ser útil primero aplicar un método cerrado (como bisección) para obtener una buena aproximación inicial, y luego pasar a Newton-Raphson para mejorar la precisión rápidamente.
* No requiere la condición $f(x_l​) \cdot f(x_u​) < 0$ como los métodos cerrados, ya que no trabaja sobre un intervalo sino sobre un solo punto inicial.
* Requiere que la función sea derivable en el intervalo de análisis.

[Script del método de Newton-Raphson](./metodoNewton.py)