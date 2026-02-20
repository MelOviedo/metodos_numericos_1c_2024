# <center>Métodos Numéricos 1°C 2024
Contenidos y algunos ejercicios de Métodos Numéricos UNSAM 1°C-2024

## Contenido
0. [Métodos de Aproximación de Raíces](./metodosAproximacion/metodosAproximacion.md)
1. [Matrices y Sistemas Lineales](./matricesSistLineales/matricesYSistemasLineales.md)
2. [Interpolación](./interpolación/interpolacion.md)
3. [Trabajos Prácticos](./trabajosPracticos/tps.md)

## Entorno
### Linux/MacOS
1. Generar un entorno virtual:
```
python3 -m venv .venv
```
2. Activar el entorno virtual:
```bash
source .venv/bin/activate
```
3. Una vez activado el entorno virtual, instalar las dependencias:
```bash
pip install -r requirements.txt
```
4. Ingresar al entorno virtual cada vez que se quiera trabajar en el proyecto:
```bash
source .venv/bin/activate
```

---
### Windows
1. Creo El entorno
```powershell
python -m venv .venv
# Si no funciona
py -m venv .venv
```

2. Activo el entorno
```powershell
.\.venv\Scripts\Activate
```
Si te tira error de ejecución de scripts, ejecutá primero
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Luego...
```powershell
.\.venv\Scripts\Activate
```

3. Actualizo el pip
```powershell
python -m pip install --upgrade pip
```

4. Instalo los requerimientos
```powershell
pip install -r requirements.txt
```

5. Ingresar al entorno virtual cada vez que se quiera trabajar en el proyecto:
```bash
.\.venv\Scripts\Activate
```