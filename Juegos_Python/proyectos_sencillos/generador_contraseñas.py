import random
import math
import os
import re
import sys

print("========================")
print("Generador de contraseñas")
print("========================")

letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&€¡¿?0123456789"

numero = input("¿Cuántas contraseñas quieres generar?: ")
numero = int(numero)

longitud = input("¿Qué longitud quieres que tengan tus contraseñas?: ")
longitud = int(longitud)

print("\nAquí tienes tus contraseñas: ")
for i in range(numero):
    contraseñas = ""
    for j in range(longitud):
        contraseñas += random.choice(letras)
    print(f"Tu contraseña nº {i+1} es: {contraseñas}")
