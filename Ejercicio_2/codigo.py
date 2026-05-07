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
