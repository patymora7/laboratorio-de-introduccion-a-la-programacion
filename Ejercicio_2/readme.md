# 🔢 Conversión de Decimal a Binario, Octal y Hexadecimal en Python

# 🎯 Objetivo del Programa

El objetivo de este programa es convertir un número decimal ingresado por el usuario a:

- 🔹 Binario (base 2)
- 🔹 Octal (base 8)
- 🔹 Hexadecimal (base 16)

Utilizando operaciones matemáticas, ciclos y condicionales en Python 🐍.

---

# ⚙️ ¿Cómo funciona el programa?

El programa utiliza el método de:

- ➗ Divisiones sucesivas
- 🔁 Obtención de residuos

Cada residuo representa un dígito del nuevo sistema numérico.

---

# 💻 Código Completo

```python
numero = int(input("Ingresa un número: "))
original = numero

# -------- Binario --------
binario = ""

if numero == 0:
    binario = "0"
else:
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2

print("Binario:", binario)

# -------- Octal --------
numero = original
octal = ""
digitos = "01234567"

if numero == 0:
    octal = "0"
else:
    while numero > 0:
        residuo = numero % 8
        octal = digitos[residuo] + octal
        numero = numero // 8

print("Octal:", octal)

# -------- Hexadecimal --------
numero = original
hexadecimal = ""
digitos = "0123456789ABCDEF"

if numero == 0:
    hexadecimal = "0"
else:
    while numero > 0:
        residuo = numero % 16
        hexadecimal = digitos[residuo] + hexadecimal
        numero = numero // 16

print("Hexadecimal:", hexadecimal)
```

---

# 📝 Explicación Paso a Paso

# ✅ PASO 1: Pedir el número

```python
numero = int(input("Ingresa un número: "))
```

## 📌 ¿Qué hace?

Primero el programa pide al usuario un número.

### ✨ Ejemplo:

```python
25
```

El número se guarda en la variable:

```python
numero = 25
```

---

# ✅ PASO 2: Guardar una copia

```python
original = numero
```

## 📌 ¿Por qué?

Porque después el valor de `numero` irá cambiando durante las conversiones.

Entonces guardamos el valor original para reutilizarlo 🔄.

---

# 🔵 CONVERSIÓN A BINARIO

# ✅ PASO 3: Crear una variable vacía

```python
binario = ""
```

Aquí se guardará el resultado binario 💾.

---

# ✅ PASO 4: Verificar si el número es 0

```python
if numero == 0:
    binario = "0"
```

Si el usuario escribe:

```python
0
```

El resultado binario también será:

```python
0
```

---

# ✅ PASO 5: Iniciar el ciclo while

```python
while numero > 0:
```

El ciclo se repetirá mientras el número sea mayor que cero 🔁.

---

# ✅ PASO 6: Obtener el residuo

```python
residuo = numero % 2
```

## 📌 ¿Qué hace `%`?

Obtiene el residuo de una división.

### ✨ Ejemplo:

```python
25 % 2 = 1
```

Ese residuo es un dígito binario 🔢.

---

# ✅ PASO 7: Guardar el residuo

```python
binario = str(residuo) + binario
```

## 📌 ¿Por qué se agrega al inicio?

Porque los residuos salen al revés ↩️.

---

# ✅ PASO 8: Dividir el número

```python
numero = numero // 2
```

## 📌 ¿Qué hace `//`?

Hace división entera.

### ✨ Ejemplo:

```python
25 // 2 = 12
```

---

# ✅ PASO 9: Repetir el proceso

El ciclo vuelve a ejecutarse 🔁.

---

# 📘 Ejemplo Completo Binario

## 🔢 Número:

```python
25
```

| ➗ División | 📌 Residuo |
|---|---|
| 25 ÷ 2 | 1 |
| 12 ÷ 2 | 0 |
| 6 ÷ 2 | 0 |
| 3 ÷ 2 | 1 |
| 1 ÷ 2 | 1 |

📖 Leyendo los residuos de abajo hacia arriba:

```python
11001
```

---

# ✅ Resultado Binario

```python
print("Binario:", binario)
```

### 🖥️ Salida:

```python
Binario: 11001
```

---

# 🟣 CONVERSIÓN A OCTAL

# ✅ PASO 10: Recuperar el número original

```python
numero = original
```

Se vuelve a usar el número inicial 🔄.

---

# ✅ PASO 11: Crear variables

```python
octal = ""
digitos = "01234567"
```

La cadena contiene los números válidos del sistema octal 🔢.

---

# ✅ PASO 12: Obtener residuo con base 8

```python
residuo = numero % 8
```

### ✨ Ejemplo:

```python
25 % 8 = 1
```

---

# ✅ PASO 13: Guardar el dígito

```python
octal = digitos[residuo] + octal
```

---

# ✅ PASO 14: Dividir entre 8

```python
numero = numero // 8
```

---

# 📘 Ejemplo Completo Octal

| ➗ División | 📌 Residuo |
|---|---|
| 25 ÷ 8 | 1 |
| 3 ÷ 8 | 3 |

📖 Leyendo de abajo hacia arriba:

```python
31
```

---

# ✅ Resultado Octal

```python
print("Octal:", octal)
```

### 🖥️ Salida:

```python
Octal: 31
```

---

# 🟠 CONVERSIÓN A HEXADECIMAL

# ✅ PASO 15: Reiniciar el número

```python
numero = original
```

---

# ✅ PASO 16: Crear variables

```python
hexadecimal = ""
digitos = "0123456789ABCDEF"
```

📌 En hexadecimal se usan números y letras:

| 🔢 Decimal | 🔠 Hexadecimal |
|---|---|
| 10 | A |
| 11 | B |
| 12 | C |
| 13 | D |
| 14 | E |
| 15 | F |

---

# ✅ PASO 17: Obtener residuo con base 16

```python
residuo = numero % 16
```

---

# ✅ PASO 18: Buscar el carácter hexadecimal

```python
hexadecimal = digitos[residuo] + hexadecimal
```

---

# ✅ PASO 19: Dividir entre 16

```python
numero = numero // 16
```

---

# 📘 Ejemplo Completo Hexadecimal

| ➗ División | 📌 Residuo |
|---|---|
| 25 ÷ 16 | 9 |
| 1 ÷ 16 | 1 |

📖 Leyendo de abajo hacia arriba:

```python
19
```

---

# ✅ Resultado Hexadecimal

```python
print("Hexadecimal:", hexadecimal)
```

### 🖥️ Salida:

```python
Hexadecimal: 19
```

---

# 🎉 Resultado Final

Si el usuario escribe:

```python
25
```

El programa mostrará:

```python
Binario: 11001
Octal: 31
Hexadecimal: 19
```

---

# 📚 Conceptos Utilizados

- 🧠 Variables
- ⌨️ `input()`
- 🔢 `int()`
- 🔁 `while`
- ✅ `if`
- ➗ Operador `%`
- ✂️ División entera `//`
- 📝 Manejo de cadenas
- 🔄 Conversión de bases numéricas

---

# 🏁 Conclusión

Este programa permite comprender cómo funcionan las conversiones entre sistemas numéricos utilizando operaciones matemáticas básicas y lógica de programación 🐍✨.
