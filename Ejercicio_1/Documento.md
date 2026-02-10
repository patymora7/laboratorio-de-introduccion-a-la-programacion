Python con entorno virtual (muy básico)
1. Verificar Python

Abrir la terminal y escribir:

py --version

2. Crear carpeta

Crear una carpeta llamada:

python_practica


Abrirla en Visual Studio Code.

3. Crear entorno virtual

En la terminal de VS Code:

py -m venv env

4. Activar entorno
env\Scripts\activate


Debe aparecer:

(env)

5. Instalar NumPy
pip install numpy

6. Probar

Crear main.py y escribir:

import numpy as np
print(np.array([1, 2, 3]))


Ejecutar:

python main.py

