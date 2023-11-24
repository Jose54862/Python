#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
# asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# print(asignaturas)


#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
# asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# for asignatura in asignaturas:
#     print(f"Yo estudio {asignatura}")


#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
# asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# notas = []
# for asignatura in asignaturas:
#     while True:
#         nota = input(f"Cuál es tu nota en {asignatura}: ")
#         if 0 <= float(nota) <= 10:
#             notas.append(nota)
#             break
#         else:
#             print("Introduzca un valor numérico del 0 al 10")

# for numero in range(len(asignaturas)):
#     print(f"En {asignaturas[numero]} has sacado un {notas[numero]}")


#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
# awarded = []
# for i in range(6):
#     awarded.append(int(input("Introduce un número ganador: ")))
# awarded.sort()
# print("Los números ganadores son " + str(awarded))


#Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numeros.reverse()
# for numero in numeros:
#     print(numero,end=", ")


#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
# subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# passed = []
# for subject in subjects:
#     score = 2
#     if score >= 5:
#         passed.append(subject)
# for subject in passed:
#     subjects.remove(subject)
# print("Tienes que repetir " + str(subjects))


#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# for i in range(len(alphabet), 1, -1):
#     if i % 3 == 0:
#         alphabet.pop(i-1)
# print(alphabet)

#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
word = input("Introduce una palabra: ")
reversed_word = word
word = list(word)
reversed_word = list(reversed_word)
reversed_word.reverse()
while True:
    if word == reversed_word:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")
        if word != reversed_word % 4:
            printed_word = input("Número incorrecto.Introduzca de nuevo")
        