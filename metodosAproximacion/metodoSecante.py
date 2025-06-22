import sympy as sp
x=sp.symbols('x')      #indico que x va a ser una variable simbolica que se usara en la función
fn=sp.sympify(input("Ingresa una función continua: "))    #aca el usuario ingresa la funcion, sympify transforma la parte simbolica
f=sp.lambdify(x,fn)    #Evalua la funcion de entraa

print("{:^60}".format("Método de la Secante"))   #Centra el encabezado

#Inicializacion de variables
x_1=float(input("Valor inicial de X_1: "))  #Ingresa primer extremo
Xo=float(input("Valor inicial de Xo: "))  #Ingresa segundo extremo
crit=float(input("Criterio de frenada: "))  #Criterio de tolerancia
iterMax=int(input("Ingrese la cantidad de iteraciones Máximas"))
iter=0 #contador
xAnterior=xr=Xo

print("{:^10} {:^15} {:^15} {:^15} {:^15}".format("i","x_1","X0","xr","ea(%)"))
print("{:^10} {:^15f} {:^15f}".format(iter,x_1,xr))

while iter<iterMax:
    xr=(xAnterior-(f(xAnterior)*(x_1-xAnterior)/(f(x_1)-f(xAnterior))))
    if(xr!= 0):
        ea=abs((xr-xAnterior)/xr)*100
    iter+=1
    print("{:^10} {:^15f} {:^15f} {:^15f} {:^15f}".format(iter,round(x_1,9),round(xAnterior,9),round(xr,9),round(ea,9))) 
    x_1=xAnterior
    xAnterior=xr
    if ea<crit:
        break
    
print("\n")
print("El valor de xr es: ",round(xr,9),"con un error de ",round(ea,9),"%")