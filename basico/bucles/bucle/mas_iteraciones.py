frutas = ["platano","manzana","ciruela,","pera","naranja","granada","durazno"]
cadena = "Hola Jose"
numeros = [2,5,8,10]

#Evitar que se coma una granada con la secuencia continue
# for fruta in frutas:
#     if fruta == "granada":
#         continue
#     print(f"Me voy a comer una {fruta}")
    
#Evitar que el bucle siga ejecutandose (el else tampoco se ejecuta)
for fruta in frutas:
    print(f"Me voy a comer una {fruta}")
    if fruta == "pera ":
        break

#Recorrer una cadena de texto
for letra in cadena:
    print(letra)
    
#For en una sola linea de codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)




