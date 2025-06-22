## Método Biseccón
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