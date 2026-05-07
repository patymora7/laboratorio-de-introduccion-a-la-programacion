# Scanner Neon - Explicación Paso a Paso

# Introducción

Este proyecto consiste en crear un escáner de códigos QR y códigos de barras usando Python con Flask y JavaScript.

La aplicación utiliza la cámara del dispositivo para detectar códigos y mostrar el resultado en pantalla.

También puede abrir enlaces automáticamente si el código contiene una URL.

---

# Paso 1 - Importar Flask

Primero se importa Flask y render_template_string.

```python
from flask import Flask, render_template_string
```

## ¿Qué hace?

- `Flask` crea el servidor web
- `render_template_string` permite mostrar HTML directamente desde Python

---

# Paso 2 - Crear la aplicación Flask

```python
app = Flask(__name__)
```

## ¿Qué hace?

Aquí se crea la aplicación principal.

La variable `app` será el servidor que ejecutará el proyecto.

---

# Paso 3 - Crear el HTML

```python
HTML = """
...
"""
```

## ¿Qué hace?

Se guarda todo el código HTML dentro de una variable llamada `HTML`.

Dentro de esta variable también se incluye:

- CSS
- JavaScript
- Diseño visual

---

# Paso 4 - Crear la estructura de la página

Dentro del HTML se crea:

```html
<div class="container">
```

## ¿Qué hace?

Es el contenedor principal donde se muestran:

- El título
- La cámara
- El resultado
- El botón

---

# Paso 5 - Agregar el video de la cámara

```html
<video id="video" autoplay playsinline></video>
```

## ¿Qué hace?

Este elemento muestra la cámara en tiempo real.

### Atributos

- `autoplay` → inicia automáticamente
- `playsinline` → evita pantalla completa en celular

---

# Paso 6 - Agregar el resultado

```html
<div class="resultado" id="resultado">
    Iniciando cámara...
</div>
```

## ¿Qué hace?

Aquí aparecerá el código detectado.

Por ejemplo:

```text
Resultado:
7501031311309
```

---

# Paso 7 - Agregar el botón

```html
<button class="btn" onclick="reiniciar()">
    Reiniciar escáner
</button>
```

## ¿Qué hace?

Este botón limpia el resultado anterior para volver a escanear.

---

# Paso 8 - Importar ZXing

```html
<script src="https://unpkg.com/@zxing/library@latest"></script>
```

## ¿Qué hace?

Importa la librería ZXing.

ZXing es la encargada de leer:

- QR
- Código de barras

---

# Paso 9 - Crear el lector

```javascript
const codeReader = new ZXing.BrowserMultiFormatReader();
```

## ¿Qué hace?

Crea el lector que analizará la cámara buscando códigos.

---

# Paso 10 - Obtener elementos HTML

```javascript
const video = document.getElementById("video");
const resultado = document.getElementById("resultado");
```

## ¿Qué hace?

Conecta JavaScript con los elementos HTML.

- `video` → cámara
- `resultado` → texto mostrado

---

# Paso 11 - Variable lastResult

```javascript
let lastResult = "";
```

## ¿Qué hace?

Guarda el último código detectado.

Esto evita que el mismo código se repita muchas veces.

---

# Paso 12 - Crear función iniciar()

```javascript
async function iniciar(){
```

## ¿Qué hace?

Esta función inicia la cámara y el escaneo.

---

# Paso 13 - Activar cámara

```javascript
await codeReader.decodeFromConstraints(
```

## ¿Qué hace?

Inicia el lector usando la cámara del dispositivo.

---

# Paso 14 - Usar cámara trasera

```javascript
facingMode:{ ideal:"environment" }
```

## ¿Qué hace?

Intenta usar la cámara trasera del celular.

---

# Paso 15 - Detectar códigos

```javascript
if(result){
```

## ¿Qué hace?

Verifica si se detectó un código.

---

# Paso 16 - Evitar repetidos

```javascript
if(result.text !== lastResult){
```

## ¿Qué hace?

Compara el código nuevo con el anterior.

Si es diferente:

- Lo muestra
- Reproduce sonido
- Guarda el resultado

---

# Paso 17 - Mostrar resultado

```javascript
resultado.innerHTML = `
    <b>Resultado:</b><br><br>
    ${result.text}
`;
```

## ¿Qué hace?

Muestra el contenido del código en pantalla.

---

# Paso 18 - Reproducir sonido

```javascript
new Audio(
    "https://actions.google.com/sounds/v1/cartoon/clang_and_wobble.ogg"
).play();
```

## ¿Qué hace?

Reproduce un sonido cuando se detecta un código.

---

# Paso 19 - Abrir enlaces automáticamente

```javascript
if(result.text.startsWith("http")){
```

## ¿Qué hace?

Verifica si el resultado es un enlace.

Si empieza con:

```text
http
```

entonces abre la página automáticamente.

---

# Paso 20 - Manejo de errores

```javascript
catch(error){
```

## ¿Qué hace?

Detecta errores si:

- La cámara no funciona
- El navegador bloquea permisos
- El dispositivo no tiene cámara

---

# Paso 21 - Función reiniciar()

```javascript
function reiniciar(){
```

## ¿Qué hace?

Limpia el resultado anterior para volver a escanear.

---

# Paso 22 - Iniciar automáticamente

```javascript
iniciar();
```

## ¿Qué hace?

Ejecuta el escáner automáticamente al abrir la página.

---

# Paso 23 - Crear ruta Flask

```python
@app.route("/")
def home():
```

## ¿Qué hace?

Define la página principal.

Cuando alguien entra a:

```text
/
```

se mostrará el HTML.

---

# Paso 24 - Mostrar HTML

```python
return render_template_string(HTML)
```

## ¿Qué hace?

Envía el HTML al navegador.

---

# Paso 25 - Ejecutar servidor

```python
app.run(debug=True, host="0.0.0.0", port=5000)
```

## ¿Qué hace?

Inicia el servidor Flask.

### Parámetros

- `debug=True`
  - muestra errores automáticamente

- `host="0.0.0.0"`
  - permite abrir desde otros dispositivos

- `port=5000`
  - usa el puerto 5000

---

# Cómo ejecutar el proyecto

## Instalar Flask

```bash
pip install flask
```

---

## Ejecutar

```bash
python app.py
```

---

# Abrir en navegador

## Computadora

```text
http://127.0.0.1:5000
```

---

## Celular

Buscar la IP con:

```bash
ipconfig
```

Luego abrir:

```text
http://TU-IP:5000
```

Ejemplo:

```text
http://192.168.1.5:5000
```

---

# Características del diseño

El proyecto usa:

- Fondo oscuro
- Diseño neon
- Glassmorphism
- Animaciones
- Responsive design

---

# Tecnologías utilizadas

- Python
- Flask
- HTML
- CSS
- JavaScript
- ZXing

---

# Autor

Edgar Estrella

```
