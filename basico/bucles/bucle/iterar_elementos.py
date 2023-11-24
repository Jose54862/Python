animales = ["gato","perro","loro","cocodrilo"]
numeros = [3,57,12,63]

#Recorrer la lista animales
for animal in animales:
    print(f"Ahora la variable animal es igual a {animal}")
    
#Recorrer la lista numeros y multiplicar cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)
    
#Iterar dos listas del mismo tamaño al mismo tiempo
for numero,animal in zip(animales,numeros):
    print(f"Recorriendo lista 1: {numero}")
    print(f"Recorriendo lista 2: {animal}")
    
    
#Recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice} y el valor es: {valor}")

#Usar el else
for numero in numeros:
    print(f"Ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("El bucle ha terminado.")

#  for num in range(10,20):
#      print(num)
