import sys
import math

sys.set_int_max_str_digits(999999999)
#Escribir una función que reciba un número entero positivo y devuelva su factorial.
# def factorial(numero):
#     if numero == 0 or numero == 1:
#         return 1
#     else:
#         resultado = 1
#         for i in range(2, numero + 1):
#             resultado *= i
#         return resultado

# numero = 954499
# resultado = factorial(numero)
# print(f"El factorial de {numero} es {resultado}")


#Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
# def circle_area(radio):
#     pi = math.pi
#     return pi*radio**2

# def cilinder_volume(radio, altura):
#     return circle_area(radio)*altura

# print(cilinder_volume(3,5))


#Escribir una función que reciba una muestra de números en una lista y devuelva su media.
# def media(*m):
#     numero_total = 0
#     for i in m:
#         numero_total += i
#     media_numero = numero_total/len(m)
#     print(media_numero)

# media(1,2,3,400)


#Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
def cuadrado_numeros(c):
    list = []
    for i in c:
        list.append(i**2)
    return list
        
print(cuadrado_numeros([1,2,3,5,15.6]))


