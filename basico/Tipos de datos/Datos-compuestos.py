#Guardar varios datos

lista = ["Jose",17,False,"Quizas o tal vez"]
tupla = ("Jose",17,False,"Quizas o tal vez") #tupla no se pueden modificar los valores

#Sirve
lista[3] = "Pues no"

#No sirve
# tupla[3] = "Pues no"

#print(lista[3])

#crear un conjunto (set)(no se accede a elementos por indice, no almacena datos por duplicado)
conjunto = {"Jose",17,False,"Quizas o tal vez"}

#print(conjunto) -> Funciona
#print(conjunto[2]) -> No funciona

#crear un diccionario (dict) (la estructura es key : value y separado con comas)
diccionario = {
    'nombre' : "Jose",
    'apellidos' : "Ye Ren",
    "s programar" : False,
    "altura" : 1.82
}

print(diccionario["nombre"])