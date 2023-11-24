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

# n = int(input())
# arr = map(int, input().split())
# if 2 <= n <= 10:
#     for i in range(2,n):
#         if arr[i] < arr[i+1]:
#             print(arr)

from typing import List

class Solution:
    a = [1]
    b = 0
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        a = nums[1]
        b = nums[2]
        for i in range (1,len(nums)+1):
            if a + b != target:
                a += 1