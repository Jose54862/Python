n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    i += 1  
if i == n:  #No se ha encontrado ningun módulo = 0
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")
    
# def esPrimo(n):
#     for i in range(2,n//2+1):
#         if (not (n % i)):
#             return 0
#     return 1
    
# numPrimos = 0
 
# for i in range(2,250001):
#     numPrimos += esPrimo(i)

# print(str(numPrimos))