## Interpolación  
Sirve para estimar valores intermedios entre dats definidso por puntos.

---
#### Interpolacion Lineal  
$$f_1(x) = f(x_0) +  \frac{f(x_1) - f(x_0)}{x_1 - x_0}$$

[Script Interpolación Lineal.](./interpolacion.md)

--- 
#### Interpolación de Langrange  
Es una refrmulación del polinomio de Newton que evita el cálculo de las diferencias divididas.
#### Versión Lineal
$$f_1(x) = \frac{x - x_1}{x_0 - x_1}\cdot f(x_0) +  \frac{x - x_0}{x_1 - x_0}\cdot f(x_1)$$
#### Versión Segundo Grado
$$f_2(x) = \frac{(x - x_1)\cdot (x - x_2)}{(x_0 - x_1) \cdot (x_0 - x_2)}\cdot f(x_0) +  \frac{(x - x_0)\cdot (x - x_2)}{(x_1 - x_0)\cdot (x_1 - x_2)}\cdot f(x_1) + \frac{(x - x_0)\cdot (x - x_1)}{(x_2 - x_0)\cdot (x_2 - x_1)}\cdot f(x_2)$$

[Script Interpolación de Lagrange versión Lineal.](./interLagrange.py)