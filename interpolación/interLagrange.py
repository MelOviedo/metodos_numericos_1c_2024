def lagrangeInterpolacionLineal(x, x0, x1, y0, y1):
    """
    para aproximar el valor de y en un punto x
    utilizando los puntos (x0, y0) y (x1, y1).
    """
    #calculo los polinomios base
    L0 = (x - x1) / (x0 - x1)
    L1 = (x - x0) / (x1 - x0)
  
    y = y0 * L0 + y1 * L1   #interpolacion lineal de Lagrange
    
    return y


#ejemplo 
x0, y0 = 1.0, 2.0     #(x0, f(x0))
x1, y1 = 3.0, 4.0     #(x1, f(x1))
xInterpolate = 2.5   #punto donde se desea interpolar

yInterpolated = lagrangeInterpolacionLineal(xInterpolate, x0, x1, y0, y1)

print(f"Para x = {xInterpolate}, y = {yInterpolated}")