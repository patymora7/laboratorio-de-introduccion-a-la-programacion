# Explicación del Programa 

## Esto se utilizara para crear un control de acceso 
 
## Primer paso
Se empiezan creando la variable:

```
intentos=0
```

Esta variable que utilizaremos servira para contar cuántas veces el usuario se equivoca.


## Segundo paso

```
while (intentos<3):
```
este se pondrá para iniciar un bucle, un bucle es una orden para que se repita mientras los intentos sean menores a 3 


## Tercer paso 

se utilizara input:
- Usuario
- Contraseña

```
usuario = input("usuario: ")
contraseña = input("contraseña: ")
```

Esto permitara que el usuario escriba sus datos desde el teclado.

## Cuarto paso

con estas comillas ("") se dara la orden de que el usuario no este vacio y que no se contengan espacios 

Si no cumple estas condiciones, se suma un intento.


```
 if usuario =="":
        print("usuario vacio")
        intentos += 1
```

## Quinto paso 
 esto se pondrá para dar el orden de que no se permitirán espacios ya que chr(32) en el código ascci significa espacio
 
```
 elif usuario == chr(32)
```

## sexto paso 
esto se pondrá por  len se utilizara para contar los caracteres agregando la que la contraseña tengas menos de 8 caracteres

```
 elif len(contraseña) < 8:
        print("la contraseña es minima a 8 carecteres")
        intentos += 1
```



## septimo paso 
El isdigit es utilizado para que se verifique que todos números pero no será valida puros números

```
elif contraseña.isdigit():
        print("la contraseña no puede ser solo numeros")
        intentos += 1
```

## octavo paso 
Este verificara si todos son letras en caso de que sea será invalida en el siguiente 

```
elif contraseña.isalpha():
        print("la contraseña no puede ser solo letras")
        intentos += 1
```
## noveno paso
el and se pondrá para que ambas condiciones se cumplan ya que admin y Admin2026 será el usuario y contraseña correctos después se pondrá break para cerrar el bucle que iniciamos con while después de cerrar el bucle 

```
elif usuario =="admin" and contraseña == "Admin2026":
        print("acceso permitido")
        break
```
## decimo paso
Este bloque sirve para controlar los errores y limitar el acceso a solo 3 intentos.
```
 else:
        intentos +=1

    print("acceso denegado, intentos restantes:", 3-intentos )
```

# Conclusión

Este programa permite controlar el acceso con usuario y contraseña ,Usando condiciones y un contador para limitar los intentos a solo tres 
También verifica que la contraseña cumpla con reglas básicas de seguridad tambien para saber ciclos, validaciones y condiciones 
