#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
# palabra = input("Introduzca una palabra: ")
# for numero in range(10):
#     print(palabra)


#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
# edad = int(input("Introduzca su edad: "))
# for i in range(1,edad+1):
#     print(f"Ha cumplido {i} años.")
    

#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
# numero = input("Introduzca un numero entero positivo: ")
# if numero.isnumeric():
#     for i in range(1,int(numero)+1):
#         if i % 2 != 0:
#             print(i,end=(", "))
# else:
#     print("Error.Introduzca un valor numérico entero positivo.")


#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
# numero = int(input("Introduzca un número entero positivo: "))
# for i in range(numero, -1, -1):
#     print(i,end=", ")


#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
# cantidad = str(input("Introduzca una cantidad a invertir: "))
# interes_anual = str(input("Introduzca el interés anual: "))
# numero_años = str(input("Introduzca el numero de años que quiere invertir: "))
# if cantidad.isnumeric() and interes_anual.isnumeric() <= 100 and numero_años.isnumeric():
#     cantidad = int(cantidad)
#     interes_anual = float(interes_anual)
#     numero_años = int(numero_años)
#     for n in range(1,numero_años+1):
#         cantidad = cantidad + (cantidad * interes_anual / 100)
#         print(f"Tendrá {cantidad:.2f}€ en el año {n}")


#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
# numero = int(input("Introduzca la altura del triángulo: "))
# for i in range(1,numero+1):
#     print("*"*int(i))


#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
#Que fumada es esta no entiendo nada por favor saquenme de aqui.
# for i in range(1, 11):
#     for j in range(1, 11):
#         resultado = i * j
#         print(resultado, end="\t")
#     print()


#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
# numero = int(input("Introduzca la altura del triángulo: "))

# for i in range(1, numero + 1, 2):
#     for j in range(i, 0, -2):
#         print(j, end=" ")
#     print()
        
        
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
# contraseña_correcta = "1234"
# contraseña_introducida = input("Introduzca la contraseña: ")
# while contraseña_introducida != contraseña_correcta:
#     print("Incorrecto.")
#     contraseña_introducida = input("Introduzca la contraseña: ")
# else:
#     print("Iniciando sesion...")


#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
# palabra = input("Introduzca una palabra: ")
# numero_letras = len(palabra)
# for i in range(numero_letras-1,-1,-1):
#     letra = palabra[i]
#     posicion_letra = i
#     print(f"{letra}")


#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
# frase = str(input("Introduzca una frase: ")).lower()
# letra = str(input("Introduzca una letra para que se muestre la cantidad de veces que aparece: ")).lower()
# numero_veces = 0

# if not frase.isnumeric():
#     for i in frase:
#         if i == letra:
#             numero_veces += 1
#     print(f"La letra {letra} aparece {numero_veces} veces en la frase {frase}.")
# else:
#     print("Introduzca una frase sin números.")


#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
# eco = ("")
# while eco != "salir":
#     eco = input()
#     print(eco)
    
    

