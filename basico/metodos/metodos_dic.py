diccionario = {
    "nombre" : "renzhe",
    "apellidos" : "ye ren",
    "edad" : 16
}

#Muestra las claves
claves = diccionario.keys()

#Obtener un elemento con get() (no lanza excepción,si no encuentra nada el programa continua)
valor_de_edad = diccionario.get("edad")

#Elimina todo del diccionario
#diccionario.clear()

#Elimina un elemento del diccionario
diccionario.pop("apellidos")

#Obtener un elemento dic_items iterable
diccionario_iterable = diccionario.items()


print(diccionario_iterable)