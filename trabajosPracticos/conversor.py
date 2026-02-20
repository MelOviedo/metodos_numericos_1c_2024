'''
Correr con:
          python trabajosPracticos/conversor.py
'''
import subprocess
import sys

def conversor(cmd):
  result = subprocess.run(cmd, shell=True)
  
  if result.returncode != 0:
    print(f"❌ Error al ejecutar: {cmd}")
    sys.exit(result.returncode)

  print("\nEl script se ejecutó correctamente.")


def main():
  print("{:^60}".format("Conversor de formatos con jupytext"))
  print("1. Convertir .py a .ipynb")
  print("2. Convertir .ipynb a .py")
  
  opcion = int(input("Ingrese una opción: "))

  match opcion:
    case 1:
      comando= "jupytext --set-formats py,ipynb trabajosPracticos/cuadradosMinimosYRegresionLineal.py"
      conversor(comando)

    case 2:
      comando= "jupytext --set-formats ipynb,py trabajosPracticos/cuadradosMinimosYRegresionLineal.ipynb"
      conversor(comando)

if __name__ == "__main__":
  main()