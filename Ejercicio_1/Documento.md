
**ENTORNO VIRTUAL**

---

# primer paso : Python con entorno virtual en Visual Studio Code

En esta práctica se usará **Python** dentro de **Visual Studio Code** y se trabajará con un **entorno virtual**, el cual ayuda a mantener las librerías ordenadas por proyecto.


---

## 1. Tener Python instalado

Antes de usar Visual Studio Code, es necesario tener **Python instalado en la computadora**.

1. Abrir **CMD o PowerShell**.
2. Escribir:

```bash
py --version
```
<img width="410" height="538" alt="Captura de pantalla 2026-02-10 114238" src="https://github.com/user-attachments/assets/28dba962-a251-43ff-949e-ed353867282f" />

Si aparece una versión de Python, significa que Python está instalado correctamente.

---

## 2. Crear la carpeta del proyecto

1. Crear una carpeta llamada:

```text
python_entorno
```

2. Abrir **Visual Studio Code**.
3. Seleccionar **File > Open Folder** y abrir la carpeta creada.
4. <img width="367" height="535" alt="image" src="https://github.com/user-attachments/assets/acd413e1-947e-4e19-b932-cad1ec4d81f2" />


---

## 3. ¿Qué es un entorno virtual?

Un **entorno virtual** es un espacio separado donde se instalan las librerías que usa un proyecto.
Esto evita que las librerías de un proyecto afecten a otros.

---

## 4. Crear el entorno virtual en Visual Studio Code

1. Abrir la terminal integrada desde **Terminal > New Terminal**.
2. En la terminal escribir:
3. <img width="524" height="552" alt="image" src="https://github.com/user-attachments/assets/366f10eb-b6ce-499e-887e-e83cb94ae430" />


```bash
py -m venv env
```

Se creará una carpeta llamada `env` dentro del proyecto.
<img width="964" height="316" alt="Captura de pantalla 2026-02-10 114706" src="https://github.com/user-attachments/assets/941c7d83-cce0-4c65-84ad-ab1037d23888" />


---

## 5. Activar el entorno virtual

En la misma terminal escribir:

```bash
env\Scripts\activate
```

Cuando el entorno esté activo, aparecerá `(env)` al inicio de la línea.
<img width="902" height="460" alt="image" src="https://github.com/user-attachments/assets/c103a171-428a-475b-b538-b438e97ffa5e" />


---

## 6. Usar el entorno en Visual Studio Code

Visual Studio Code detectará el entorno automáticamente.
Si pide seleccionar intérprete, elegir el que diga **Python (env)**.

---

## 7. Instalar una librería de prueba

Con el entorno activo:

```bash
pip install numpy
```

---

## 8. Probar que funciona

1. Crear un archivo llamado `main.py`.
2. Escribir:

```python
import numpy as np
np. (al poner np. en el archivo te va a mostrar todas las funciones disponibles del paquete)
<img width="937" height="605" alt="image" src="https://github.com/user-attachments/assets/87a3e791-bd64-4146-a651-14d0c3b5027a" />

```

3. Ejecutar:

```bash
python main.py
```

Si imprime los números, el entorno virtual está funcionando correctamente.

---

## En conclusion son pasos para poder hacer un entorno virtual en visual code 




