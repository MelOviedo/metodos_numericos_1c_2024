#Si R² es cercano a 1,entonces los puntos están muy alineados y podemos decir que están casi perfectamente alineados.
#Si R² es cercano a 0, entonces los puntos no están alineados y la regresión lineal no es un buen modelo para esos datos.
#Un valor intermedio de R² indica que los puntos tienen cierto grado de alineación, pero no es perfecta.

import numpy as np

def cargarValores(n,eje):
    valores = []
    print(f"Cargando Valores de {eje}")
    for i in range(n): 
        valores.append(int(input(f"Ingrese {i+1}° valor: ")))
    return valores

#Cálculo de Cuadrados Mínimos
def calculoDePendienteYOrdenada(x,y):  
    n = len(x)
    sumX = np.sum(x)
    sumY = np.sum(y)
    sumXY = np.sum(x*y)
    sumXCuadrados = np.sum(x**2)
    # cálculo de la pendiente (a) y la ordenada al origen (b)
    m = (n*sumXY-sumX*sumY) / (n*sumXCuadrados-sumX**2)
    b = (sumY-m*sumX) / n

    e=np.sum((y-b-m*x)**2)
    st=np.sum((y-(y/n))**2)
    r_2=(st-e)/st

    return m, b,e,r_2

n = int(input("Ingrese la cantidad de puntos desea analizar: "))

x=np.array(cargarValores(n,"X"))
y=np.array(cargarValores(n,"Y"))

print("Tabla de Valores de x:", x)
print("Tabla de Valores de y:", y)

a,b,e,r_2= calculoDePendienteYOrdenada(x, y) #Calculo de Cuadrados Mínimos
print("Pendiente:", a)
print("Ordenada al origen:", b)
print("Error:",e)
print("Valor de R^2:",r_2)  
