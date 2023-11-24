#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
#nombre = input("¿Cuál es tu nombre?: ")
#numero = input("Introduzca un numero entero: ")
#print((f"{nombre} \n") * int(numero))

#Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
#nombre = input("Introduzca su nombre completo: ")
#print(nombre.upper())
#print(nombre.lower())
#print(nombre.capitalize())

#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
#nombre = input("Introduzca su nombre: ")
#print(f"{nombre.upper()} tiene {len(nombre)} letras.")

#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
#numero_telefono = input("Introduzca un numero de telefono con el formato +34-913724710-56: ")
#print(f"El número de teléfono es {numero_telefono[4:-3]}")

#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
#frase = input("Introduzca una frase para revertir: ")
#print(frase[::-1])

#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
#frase = input("Introduzca una frase: ")
#vocal = input("Introduzca una vocal en minúscula: ")
#print(frase.replace(vocal,vocal.upper()))

#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
#correo_electronico = input("Introduzca su correo electrónico: ")
#nuevo_correo = input(f"Su nuevo correo es: {correo_electronico[:correo_electronico.find("@")]}@ceu.es")

#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
#precio_producto = input("Escriba el precio de un producto con dos decimales: ")
#precio_separado = precio_producto.split(".")
#print(f"El producto vale {precio_separado[0]}€ y {precio_separado[1]} céntimos.")

#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
#productos_total = input("Escribe los productos de la cesta de la compra,separados por comas: ")
#print(productos_total.replace(",","\n"))



















