numeros = [1, 2, 3, 5, 7, 10, 14]
#def es_par(num):
#     if (num % 2 == 1):
#         return True

numeros_pares = filter(lambda numero:numero%2 == 0, numeros)
print(list(numeros_pares))

