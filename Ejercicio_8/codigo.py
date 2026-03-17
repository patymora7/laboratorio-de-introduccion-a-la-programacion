def palabra10():
    x = input("dame la palabra: ")
    for i in range(10):
        print(x)

def edad():
    x = int(input("Dame tu edad: "))
    for i in range(1, x, 1):
        print(i)

def numeros_impares():
    x = int(input("Dame el numero mayor del rango: "))
    for i in range(1, x, 2):
        print(i)

def cuenta_regresiva():
    x = int(input("Dame el numero: "))
    for i in range(x, -1, -1):
        print(i)

def inversion():
    x = int(input("Cantidad a invertir: "))
    y = int(input("Dame el porcentaje del interes anual: "))
    z = int(input("Dame el numero de años: "))
    total = 0

    for i in range (z):
        total = total + x + (x*(y/100))

        print(total)

def triangulo():
    x = int(input("Dame el numero de filas: "))
    for i in range (x+1):
        print("*"*i)

def tablas():
    for i in range(1, 11):
        for j in range(1, 11):
            res = i * j
            print(i,"x",j,"=",res)

def triangulo_raro():
    n = int(input("Ingresa un número: "))

    num = 1

    for i in range(n):
        fila = ""
    
        j = num
        while j >= 1:
            fila = fila + str(j) + " "
            j = j - 2
    
        print(fila)
    
        num = num + 2

def contraseña():
    x = "contraseña"

    while True:
        y = input("Dame la contraseña: ")
        if x == y:
            print("Contraseña correcta!!")
            break
        else:
            print("contraseña incorrecta")

def primo():

    num = int(input("Ingresa un número: "))

    es_primo = True

    if num <= 1:
        es_primo = False
    else:
        for i in range(2, num):
            if num % i == 0:
                es_primo = False

    if es_primo:
        print("Es primo")
    else:
        print("No es primo")

def revez():
    palabra = input("Ingresa una palabra: ")

    for i in range(len(palabra)-1, -1, -1):
        print(palabra[i])

def veces_letra():

    frase = input("Ingresa una frase: ")
    letra = input("Ingresa una letra: ")

    contador = 0

    for i in frase:
        if i == letra:
            contador = contador + 1

    print("Se repite:", contador)

def finish():
    texto = input("Escribe algo: ")

    while texto != "salir":
        print(texto)
        texto = input("Escribe algo: ")

    print("Programa terminado")

opcion = int(input("Dame el numero de opcion: "))

match opcion:
    case 1:
        palabra10()
    case 2:
        edad()
    case 3:
        numeros_impares()
    case 4:
        cuenta_regresiva()
    case 5:
        inversion()
    case 6:
        triangulo()
    case 7:
        tablas()
    case 8:
        triangulo_raro()
    case 9:
        contraseña()
    case 10:
        primo()
    case 11:
        revez()
    case 12:
        veces_letra()
    case 13:
        finish()

    case _:
        print("Opcion invalida")

    

