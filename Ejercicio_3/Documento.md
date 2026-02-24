# 🖥️ Explicación del Programa – Control de Acceso

## 📌 Introducción

El siguiente programa simula un sistema básico de inicio de sesión.
Su función principal es validar un usuario y una contraseña,
permitiendo únicamente tres intentos antes de bloquear el acceso.

Este tipo de estructura es común en sistemas reales para proteger información.

---

# 🔎 Desarrollo del Programa

## 1️⃣ Variable de control

Se crea la variable:

intentos = 0

Esta variable sirve para contar cuántas veces el usuario se equivoca.

---

## 2️⃣ Ciclo de repetición

Se utiliza:

while intentos < 3

Este ciclo permite que el programa se repita hasta que:
- El usuario ingrese correctamente los datos.
- O se alcancen los 3 intentos máximos.

---

## 3️⃣ Entrada de datos

Se utiliza la función `input()` para pedir:
- Usuario
- Contraseña

Esto permite que el usuario escriba sus datos desde el teclado.

---

## 4️⃣ Validaciones del usuario

El programa verifica que:
- El usuario no esté vacío.
- No contenga espacios.

Si no cumple estas condiciones, se suma un intento.

---

## 5️⃣ Validaciones de la contraseña

El sistema revisa que:
- Tenga mínimo 8 caracteres.
- No sea solo números.
- No sea solo letras.

Estas reglas ayudan a que la contraseña sea más segura.

---

## 6️⃣ Verificación de credenciales

El programa compara los datos ingresados con los datos correctos:

Usuario: admin  
Contraseña: Admin2026  

Si coinciden, muestra "Acceso permitido" y termina el ciclo.

---

## 7️⃣ Control de intentos

Cada vez que el usuario comete un error:
- Se suma 1 a la variable `intentos`.
- Se muestran los intentos restantes.

Si los intentos llegan a 3, el programa finaliza.

---

# ✅ Conclusión

Este programa demuestra el uso de:

- Variables para almacenar información.
- Estructuras condicionales (`if`, `elif`) para validar datos.
- Ciclos (`while`) para repetir procesos.
- Control de intentos para limitar accesos.

En conclusión, es un ejemplo práctico de cómo implementar un sistema básico de autenticación en Python, aplicando estructuras fundamentales de programación.
