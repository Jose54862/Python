#Crear una funcion simple
def saludar():
    print("Hola como estas?")

#Ejecutar la funcion simple
saludar()

#Crear una funcion que tenga parametros
def saludar(nombre):
    print(f"Hola {nombre} como estas?")
    
saludar("Jose")

#Crear funcion que nos devuelva valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0]) #Toma la primera cifra
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    print(contraseña)
    
crear_contraseña_random(8)
    