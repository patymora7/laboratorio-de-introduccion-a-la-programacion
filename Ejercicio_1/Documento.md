# ENTORNO VIRTUAL CON PYTHON

En esta práctica se configurará un espacio de trabajo en Python usando Visual Studio Code y un entorno virtual.

-Paso 1. Editor de código

Para programar se utilizará Visual Studio Code, el cual debe estar instalado previamente desde su sitio oficial.

Paso 2. Carpeta de trabajo

Crear una carpeta nueva en Documentos.

Asignarle el nombre: Practica_Python.

Paso 3. Abrir el proyecto

Abrir Visual Studio Code.

Seleccionar Open Folder.

Abrir la carpeta Practica_Python.

Paso 4. Preparar el entorno virtual

Abrir la terminal desde el menú Terminal.

Escribir el siguiente comando para crear el entorno:

python -m venv entorno


Activar el entorno con:

entorno\Scripts\activate


Cuando esté activo, se verá el nombre del entorno al inicio de la terminal.

Paso 5. Probar Python

Crear un archivo llamado prueba.py.

Instalar la librería necesaria:

pip install numpy


Escribir el siguiente código:

import numpy as np

datos = np.array([10, 20, 30])
print(datos)

Paso 6. Cierre de la práctica

El entorno virtual permite trabajar de forma ordenada y evitar problemas entre proyectos.
Esta configuración será utilizada en prácticas posteriores.

