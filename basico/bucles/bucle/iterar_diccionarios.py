diccionario = {
    "nombre" : "Jose",
    "apellido" : "Ye",
    "edad" : 16
}

#Recorrer diccionario para obtener las claves
for key in diccionario:
    key
    print(f"La clave es : {key}")   
    
#Recorrer diccionario con items() para obtener la clave y el valor
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"La clave es : {key} y el valor es {value}.")