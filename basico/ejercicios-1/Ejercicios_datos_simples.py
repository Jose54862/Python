#Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
#print("¡Hola Mundo!")

#Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
#nombre = "¿Hola Mundo!"
#print(nombre)

#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
#nombre =  input("¿Cuál es tu nombre?: ")
#print("¡Hola " + nombre + "!")

#Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética 
#print(((3+2)/(2*5))**2)

#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
#horas_trabajadas = float(input("¿Cuantas horas has trabajado?: "))
#paga_hora = float(input("¿Cuánto ganas por hora?: "))
#total = horas_trabajadas * paga_hora
#print("Has ganado: ",total,"$")

#Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:
#numero = float(input("introduzca un numero: "))
#suma = numero*((numero + 1)/2)
#print(suma)

#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
#peso = input("Introduzca su peso (en kg): ")
#altura = input("Introduzca su altura (en metros): ")
#indice_masa_corporal = round(float(peso) / float(altura)**2,2)
#print("Tu índice de masa corporal es: " + str(indice_masa_corporal))

#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
#n = input("Introduzca un número: ")
#m = input("Introduzca otro número: ")
#print("El cociente es " + str(int(n) // int(m)) + " y el resto es " + str((int(n)) % int(m)))

#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión
#cantidad = input("¿Cuánto dinero quieres invertir?: ")
#interes_anual = input("¿Cuál es el interés anual?: ")
#numero_años = input("¿Cuántos años quieres invertir?: ")
#print("Dentro de " + numero_años + " años  tendrás " + str(round(float(cantidad) * (float(interes_anual)/100 + 1)**int(numero_años), 2)))

#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
#peso_payaso = 112
#peso_muñeca = 75
#payasos = int(input("Introduce el número de payasos a enviar: "))
#muñecas = int(input("Introduce el número de muñecas a enviar: "))
#peso_total = peso_payaso * payasos + peso_muñeca * muñecas
#print(f"El peso total del paquete es de {peso_total} kg")

#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
#dinero_depositado = input("Introduzca el dinero depositado: ")
#dinero_primer_año = round(float(dinero_depositado)*1.04,2)
#dinero_segundo_año = round(dinero_primer_año*1.04,2)
#dinero_tercer_año = round(dinero_segundo_año*1.04,2)
#print(f"En el primer año tendrás {dinero_primer_año} $.")
#print(f"En el segundo año tendrás {dinero_segundo_año} $.")
#print(f"En el tercer año tendrás {dinero_tercer_año} $.")

pan_dia = float(3.49)
pan_no_dia = round(3.49 * 0.4,2)
numero_barras = int(input("Número de barras vendidas que no son del día: "))
precio_total = pan_no_dia * numero_barras
print(f"El precio habitual de una barra de pan es de 3.49$ y por no ser fresca se hace un descuento del 60%.El coste final es de {precio_total}$")
