'''Ejercicio Trisección 

Durante la cursada se implementó el método de bisección que consta en dividir un intervalo en 2 subintervalos, en cada iteración elije uno de los subintervalos que contenga la raíz. 

En este caso se le pide al alumno que divida el intervalo en 3 subintervalos, y en cada iteración elija uno de los 3 subintervalos que contenga una raíz. 

* Implementar el Método de Trisección para aproximar raíces. 
* Usar dos condición de parada análoga a la del método de bisección.

'''
#Biblotecas a implementar
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols
from sympy import lambdify
from sympy import sympify


                                    #Funciones utilizadas en el código
def sign(f,y,z):
    return f(y)*f(z)

def graphic(xr,f):
    #Grafico de la incion e Indico el punto
    xpts=np.linspace(-10,10, 400)    #regresa un vector en numpy dormado por n numeros con los mismos espacios
    plt.plot(xpts,f(xpts))
    plt.title("Gráfica de la función")
    plt.axhline(color="black")
    plt.axvline(color="black")
    plt.scatter(xr,0,c="red")
    plt.annotate(round(xr,9),xy=(xr,0.5))
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True,which="both")
    plt.ylim([-15,15])
    plt.show()

def graphicElse(a,b,f):
    print("")
    print("La función ingresada no tiene una raíz en el intercalo de "+ "x= "+str(a)+"a x= " +str(b))
    print("Ingresar otros valores iniciales")
          
    #Grafica
    xpts=np.linspace(-10,10,400)    #regresa un vector en numpy dormado por n numeros con los mismos espacios
    plt.plot(xpts,f(xpts))
    plt.title("Gráfica de la función")
    plt.axhline(color="black")
    plt.axvline(color="black")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True,which="both")
    plt.ylim([-15,15])
    plt.show() 

                                    #Inicio del código

print("{:^60}".format("Método de Trisección"))   #Centra el encabezado

x=symbols('x')      #indico que x va a ser una variable simbolica que se usara en la función
expr_str = input("Ingresa una función continua: ")
fn=sympify(expr_str)    #aca el usuario ingresa la funcion, sympify transforma la parte simbolica
f=lambdify(x,fn)    #Nos permite evaluar la función que le damos de entrada


#Inicializacion de variables
#suponiendo siempre que a<b
a=float(input("Valor inicial de a: "))  #Ingresa primer extremo
b=float(input("Valor inicial de b: "))  #Ingresa segundo extremo

i=0 #contador
pasosLimite=int(input("Ingrese el limite de pasos a analizar: "))
ep=float(input("Criterio de frenada (epsilon): "))     #Criterio de tolerancia o umbral de error



if f(a)*f(b)<0:     #Para saber si todavía hay al menos una raíz en ese intervalo
    #Imprime Encabezado de la tabla
    print("\n")
    print("{:^16} {:^16} {:^16} {:^16} {:^16} {:^16} ".format("i","a [B. Inf]","c","d","b [B. Sup]","xr"))

    while (b-a)>=ep and pasosLimite>i:      #Mientras que el error aproximado sea mayor al critico
        delta =(b-a)/3  #resta los limites y los dividide entre 3 =>tamaño del tercio del intervalo

        #Sub intervalos
        c = a + delta
        d = b - delta
        xr = (c + d) / 2  # este es el nuevo punto estimado de la raíz

        #Valores de la tabla
        print("{:^16} {:^16f} {:^16f} {:^16f} {:^16f} {:^16f}".format(i,a,c,d,b,xr))

        #cambia el criterio -> actualiza los extremos
        if sign(f,a,c)<=0:        
            b=c
        elif sign(f,d,c)<=0:
            a=c
            b=d
        elif sign(f,b,d)<=0:
            a=d
        else:
            print("No se detecta cambio de signo en los subintervalos.")
            break
        i+=1
   
    print("\n")
    xr_final = (a + b) / 2  # Mejor estimación final de la raíz
    print("El valor de x es: ",round(xr_final,9))

    graphic(xr_final,f)

else:   #f(a)*f(b)>=0       Es decir no hay una raíz en el intervalo o la función no posee raíces reales
    graphicElse(a,b,f)

