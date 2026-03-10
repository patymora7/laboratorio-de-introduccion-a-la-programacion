intentos=0
while (intentos<3):
    usuario = input("usuario: ")
    contraseña = input("contraseña: ")
    if usuario =="":
        print("usuario vacio")
        intentos += 1
    elif usuario==chr(32):
        print("espacios no permitidos")    
        intentos += 1
    elif len(contraseña) < 8:
        print("la contraseña es minima a 8 carecteres")
        intentos += 1
    elif contraseña.isdigit():
        print("la contraseña no puede ser solo numeros")
        intentos += 1
    elif contraseña.isalpha():
        print("la contraseña no puede ser solo letras")
        intentos += 1
    elif usuario =="admin" and contraseña == "Admin2026":
        print("acceso permitido")
        acceso=1
    else:
        intentos +=1
    print("acceso denegado, intentos restantes:", 3-intentos )
    
    while acceso== 1: 
        print("1. clasificar número")
        print("2. categoria de edad y permisos")
        print("3. calcular tarifa final")
        print("4.cerrar sesion")
        print("5. salir") 
        opcion = input ("selecciona una opcion")
        if opcion == "1": 
            print("clasificar número ")
            x=int(input("ingresar un numero"))
            type(x) == int
            if x==0:
                print("el numero es igual a cero")
            elif x < 0:
                print("el numero es negativo")
            elif x > 0:
                print("el numero es positivo ")
            if x%2==0:
                print("es par")
            else:
                print("es impar")
    
        elif opcion  == "2":
            print("categoria de edad y permisos")
            edad=int(input("ingresa edad"))
            type(edad) == int
            if 0 <= edad <=120:
                identificación = input("cuenta con identificacion oficial s/n") 
                licencia = input("cuenta con licencia de conducir s/n")
            if 0 <= edad <=12:
                    print("adentro de la niñez")
            else:
                13 <= edad <=17
                print("Entra dentro de la adolescencia")
            if 18<= edad <=64:
                    print("entra dentro de la adultez")
            else:
                65<= edad <= 120
                print("entra en adulto mayor")
            if edad >=13:
                print("pueden registrarse")
            elif edad >= 18:
                  print("puedes registrarse sin tutor")
            elif edad < 18:
                print("puedes registrarse con tutor")
            elif edad >=18:
                print("puede conducir")
            elif  edad>= 21:
                print("acceso a servicio premium")
                
        elif opcion == "3":
             print("Calculando la tarifa final...")

        elif seleccion == "4":
                print("salir")
            break

        elif seleccion == "5":
    break
         break
