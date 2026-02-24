# Explicación del Programa 

## esto se utilizara para crear un control de acceso 

## paso a paso 

Se empiezan creando la variable:

intentos = 0

Esta variable que utilizaremos servira para contar cuántas veces el usuario se equivoca.


## siguiente paso

Se utiliza:

while intentos < 3
este se pondrá para iniciar un bucle, un bucle es una orden para que se repita mientras los intentos sean menores a 3 


## tercer paso 

se utilizara input:
- Usuario
- Contraseña

Esto permitara que el usuario escriba sus datos desde el teclado.
´´´input
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
