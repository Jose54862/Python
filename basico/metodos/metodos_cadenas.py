cadena1 = "157"
cadena2 = "Tengo 16 años"

#para hacer una funcion es dato.metodo()

#convierte a mayuscula
mayusc = cadena1.upper()

#convierte a minuscula
minusc = cadena1.lower()

#primera letra en mayuscula
primer_letra_mayusc = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_find = cadena1.find("a")    #Te dice la posición de lo que buscas (0-9)

#buscamos una cadena en otra cadena, si no hay coincidencias lanza una excepción
#busqueda_index = cadena1.index("a")

#si es numerico, devuelve True, sino devuelve False
es_numerico = cadena1.isnumeric()

#si es alfanumerico, devuelve True, sino devuelve False
es_alfanumerico = cadena1.isalpha() #contiene SOLO letras y sin espacios


es_digito = cadena1.isdigit()

#contar coincidencias de una cadena en otra cadena, devuelve la cantidad de veces que coincida
contar_coincidencias = cadena1.count("o")

#contar cuantos caracteres tiene una cadena
contar_caracteres = len(cadena2)

#verificar si una cadena empieza con otra cadena dada, si es asi devuelve True
empieza_con = cadena1.startswith("H")

#verificar si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con = cadena1.endswith("se")

#remplaza un pedazo de la cadena dada, por otra dada
cadena_nueva = cadena1.replace("Jose","Pepe")

#separar cadenas con la cadena que le demos
cadena_separada = cadena1.split(" ")

#Eliminar una parte de una cadena
eliminar_pedazo = cadena1[2:-3] #Esto elimina las dos primeras letras y las 3 ultimas

#print(cadena_separada[2])

print(contar_caracteres)