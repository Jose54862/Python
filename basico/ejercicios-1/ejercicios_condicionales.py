#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
#numero = int(input("Introduzca un número entero para verificar si es par o impar: "))
#if numero % 2 == 0:
#    print(f"El número {numero} es par")
#else:
#    print(f"El número {numero} es impar")


#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
# edad = input("Introduzca su edad: ")
# if edad.isnumeric():
#     edad = int(edad)
#     if edad > 16:
#         ingresos = input("Introduzca sus ingresos: ")
#         if ingresos.isnumeric():
#             ingresos = float()
#             if ingresos >= 1000:
#                 print("Debes de tributar.")
#             else:
#                 print("No tienes que tributar.")
#         else:
#             print("Introduzca un valor numérico.")
#     else:
#         print("No tienes que tributar.")
# else:
#     print("Introduzca un valor numérico.")


#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
# nombre = input("Introduzca su nombre: ")
# if nombre.isalpha():
#     sexo = input("Introduzca su sexo (hombre o mujer): ").lower()
    
#     if sexo == "mujer":
#         if nombre[0].lower() < "m":
#             print("Estás en el grupo A")
#         else:
#             print("Estás en el grupo B")
#     elif sexo == "hombre":
#         if nombre[0].lower() > "n":
#             print("Estás en el grupo A")
#         else:
#             print("Estás en el grupo B")
#     else:
#         print("Introduzca un sexo válido (hombre o mujer)")
# else:
#     print("Introduzca un nombre sin espacios ni números.")


#Renta	Tipo impositivo
# Menos de 10000€	5%
# Entre 10000€ y 20000€	15%
# Entre 20000€ y 35000€	20%
# Entre 35000€ y 60000€	30%
# Más de 60000€	45%
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
# renta_anual = input("¿Cuál es su renta anual?: ")
# if renta_anual.isnumeric() and int(renta_anual) >= 0:
#     renta_anual = int(renta_anual)
#     if renta_anual < 10000:
#         tipo_impositivo = 5
#     elif 10000 <= renta_anual <= 20000:
#         tipo_impositivo = 15
#     elif 20000 < renta_anual <= 35000:
#         tipo_impositivo = 20
#     elif 35000 < renta_anual <= 60000:
#         tipo_impositivo = 30
#     else:
#         tipo_impositivo = 45
#     print("Su tipo impositivo es del " + str(tipo_impositivo) + "%")
# else:
#     print("Error.Introduzca un valor numérico mayor o igual que 0.")


#En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
# Nivel	Puntuación
# Inaceptable	0.0
# Aceptable  	0.4
# Meritorio 	0.6 o más
# puntuacion = (input("Introduzca su puntuacion: "))
# if puntuacion.replace(".","").isnumeric() and float(puntuacion) >= 0:
#     puntuacion = float(puntuacion)
#     if 0 <= puntuacion < 0.4:
#         rendimiento = "inaceptable"
#     elif 0.4 < puntuacion < 0.6:
#         rendimiento = "aceptable"
#     else:
#         rendimiento = "meritorio"
#     print(f"Su nivel de rendimiento es {rendimiento} y la cantidad de dinero que recibirá usted es de {puntuacion*2400}€ ")
# else:
#     print("Introduzca un valor numérico mayor o igual que 0.")


#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
# edad = input("Introduzca su edad: ")
# if edad.isnumeric() and int(edad) >= 0:
#     edad = int(edad)
#     if edad < 4:
#         precio = "gratis"
#     elif 4 <= edad <= 18:
#         precio = "5€"
#     else:
#         precio = "10€"
#     print(f"Su precio de entrada es {precio}")
# else:
#     print("Error.Por favor introduzca un valor numérico natural positivo.")



















