#Crear una lista
lista = list(["hola","Jose",16])

#Devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#Agregar un elementos a la lista
lista.append("Random")

#Agregar un elemento a la lista en un indice especifico
lista.insert(2,True)

#Agregar varios elementos a la lista
lista.extend(["Si","Pepe"])

#Eliminar un elemento de la lista (por su indice)
#Si pones -1 elimina el ultimo elemento de la lista, -2 antepenultimo,etc.
lista.pop(0)

#Remueve un elemento por su valor
lista.remove("Jose")

#Elimina todos los elementos de la lista
#lista.clear()

#Ordena la lista de menor a mayor (No puede contener str) 
#lista.sort(inverse=True) lo ordena en reverso
lista.sort()

#Invierte los elementos de una lista
lista.reverse()

#Buscar un elemento completo en una lista (Por indice)
elemento_encontrado = lista.index(16)


print(elemento_encontrado)