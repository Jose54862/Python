#Crear un diccionario con dict()
diccionario = dict(nombre="Jose",apellido="Ye")

#Las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["Jose,","rancio"]):"jajaja"}

#Crear un diccionario con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(["nombre","apellido"])

#Crear un diccionario con fromkeys() cambiando el valor por defecto a "No se"
diccionario = dict.fromkeys(["nombre","apellido"],"No se")


print(diccionario)