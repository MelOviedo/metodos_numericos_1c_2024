import sympy as sp

print("{:^60}".format("Método de Newton"))   #Centra el encabezado

x=sp.symbols('x')      #indico que x va a ser una variable simbolica que se usara en la función
fn=sp.sympify(input("Ingresa una función continua: "))    #aca el usuario ingresa la funcion, sympify transforma la parte simbolica
f_p=sp.diff(fn,x)
f=sp.Lambda(x,fn)    #Evalua la funcion de entraa
fp=sp.Lambda(x,f_p)

#Inicializacion de variables
xr=float(input("Valor inicial de X0: "))  
crit=float(input("Criterio de frenada: "))  #Criterio de tolerancia
iterMax=int(input("Ingrese la cantidad de iteraciones Máximas"))

iter=0 #contador
print("{:^10} {:^15} {:^15} {:^15}".format("i","X0","xr","ea(%)"))
print("{:^10} {:^15f}".format(iter,xr))
while iter<iterMax:
    xAnterior=xr
    xr=(xAnterior-(f(xAnterior)/fp(xAnterior)))
    iter+=1
    if(xr!= 0):
        ea=abs((xr-xAnterior)/xr)*100
    print("{:^10} {:^15f} {:^15f} {:^15f}".format(iter,round(xAnterior,9),round(xr,9),round(ea,9))) 
    if ea<crit:
        break
    
print("\n")
print("El valor de xr es: ",round(xr,9),"con un error de ",round(ea,9),"%")