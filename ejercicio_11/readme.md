📸 Scanner Neon: QR & Barcode Reader
Scanner Neon es una aplicación web moderna y minimalista desarrollada con Flask y ZXing JS. Permite escanear códigos QR y códigos de barras en tiempo real utilizando la cámara del dispositivo, con una interfaz futurista optimizada para móviles.

✨ Características Principales
Interfaz Neon: Diseño basado en Glassmorphism con efectos de escaneo animados.

Escaneo en Tiempo Real: Detección instantánea de múltiples formatos gracias a @zxing/library.

Optimización Móvil: Configurado para utilizar la cámara trasera del dispositivo (facingMode: environment).

Acciones Inteligentes:

Reproducción de sonido al detectar un código.

Apertura automática de enlaces si el resultado es una URL.

Sin dependencias pesadas: Todo el procesamiento de imagen ocurre en el cliente (navegador).

🛠️ Tecnologías Utilizadas
Backend: Flask (Python) para servir la aplicación.

Frontend: HTML5, CSS3 (Animaciones personalizadas) y JavaScript.

Librería de Escaneo: ZXing JS para la decodificación de imágenes.

Estilo: Glassmorphism & Neon Design.

🚀 Instalación y Uso
Sigue estos pasos para ejecutar el proyecto localmente:

1. Clonar el repositorio
Bash
git clone https://github.com/tu-usuario/scanner-neon.git
cd scanner-neon
2. Instalar Flask
Asegúrate de tener Python instalado y luego ejecuta:

Bash
pip install flask
3. Ejecutar la aplicación
Bash
python app.py
4. Acceder al Scanner
Abre tu navegador y dirígete a:

Local: [http://127.0.0.1:5000](http://127.0.0.1:5000)

Desde tu móvil: http://<TU_IP_LOCAL>:5000 (Asegúrate de estar en la misma red Wi-Fi).

[!IMPORTANT]

Para que la cámara funcione en dispositivos móviles externos, la mayoría de los navegadores requieren una conexión HTTPS o que el servidor corra en localhost.

📋 Estructura del Código
El proyecto se autogestiona en un solo archivo principal por simplicidad:

app.py: Contiene la lógica del servidor Flask y el template HTML embebido.

ZXing Library: Se carga vía CDN para evitar configuraciones complejas de Node.js.

JavaScript iniciar(): Configura las restricciones de video y maneja la lógica de decodificación cíclica.

🎨 Personalización del Diseño
El efecto de la línea de escaneo se logra mediante una animación CSS sencilla pero efectiva:

CSS
@keyframes scan {
    0% { top: 0; }
    100% { top: 100%; }
}
Puedes cambiar el color principal reemplazando el valor #00ffaa (Neon Green) por cualquier otro color hexadecimal en el bloque <style>.

📄 Licencia
Este proyecto está bajo la Licencia MIT. ¡Siéntete libre de usarlo y mejorarlo!

Desarrollado con ❤️ por [Tu Nombre/Alias]</TU_IP_LOCAL>
