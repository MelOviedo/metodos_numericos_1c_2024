import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols
from sympy import lambdify
from sympy import sympify

print("{:^60}".format("Método de Bisección")) 

x=symbols('x')      #indico que x va a ser una variable simbolica que se usara en la función
fn=sympify(input("Ingresa una función continua: "))    #aca el usuario ingresa la funcion, sympify transforma la parte simbolica
f=lambdify(x,fn)    #Evalua la funcion de entraa

#Inicializacion de variables
#suponiendo siempre que a<b
a=float(input("Valor inicial de a: "))  #Ingresa primer extremo
b=float(input("Valor inicial de b: "))  #Ingresa segundo extremo
crit=float(input("Criterio de frenada: "))  #Criterio de tolerancia
i=0 #contador
ea=abs(b-a) #variable de error absoluto         #lo tenia en 1
xAnterior=0     #Indiar la variable de x anterior

#Criterio inicial para verificar si la solucion esta en el intervalo seleccionado
if f(a)*f(b)<0:     #Para saber si todavía hay al menos una raíz en ese intervalo
    #Imprime Encabezado de la tabla
    print("\n")
    print("{:^10} {:^10} {:^10} {:^10} {:^10}".format("i","a","b","xr","ea(%)"))

    while ea>crit:      #Mientras que el error aproximado sea mayor al critico, va a calcular el punto medio
        xr=(a+b)/2  #suma los limites y los dividide entre 2 =>punto medio del intervalo
        ea=abs((xr-xAnterior)/xr)   #Error aproximado -> valor calculado-anterior entre el valor calculado

        if f(xr)<0:         #cambia el criterio -> actualiza los extremos
            a=xr
        else:
            b=xr

        xAnterior=xr

        #Valores de la tabla
        print("{:^10} {:^10f} {:^10f} {:^10f} {:^10}".format(i,a,b,xr,round(ea*100,9)))
        i+=1
   
    print("\n")
    print("El valor de x es: ",round(xr,9),"con un error de ",round(ea*100,9),"%")

    #Grafico de la incion e Indico el punto
    xpts=np.linspace(-10,10)    #regresa un vector en numpy dormado por n numeros con los mismos espacios
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

else:   #f(a)*f(b)>=0       Es decir no hay una raíz en el intervalo o la función no posee raíces reales

    print("")
    print("La funcion no tuene una raiz en el intercalo de "+ "x= "+str(a)+"a x= " +str(b))
    print("Ingresar otros valores iniciales")
          
    #Grafica
    xpts=np.linspace(-10,10)    #regresa un vector en numpy dormado por n numeros con los mismos espacios
    plt.plot(xpts,f(xpts))
    plt.title("Gráfica de la función")
    plt.axhline(color="black")
    plt.axvline(color="black")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True,which="both")
    plt.ylim([-15,15])
    plt.show() 