import random

def adivinar(x):
    numero = 0
    numero_random = random.randint(1,x)
    while numero != numero_random:
        numero = input(f"Adivina el numero del 1 al {x}: ")
        numero = str(numero)
        if numero.isnumeric():
            numero = int(numero)
            if numero > numero_random:
                print("El numero es mas bajo.")
            elif numero < numero_random:
                print("El numero es mas alto.")
        else:
            print("Error.Introduzca un valor valido.")
    print("Felicidades, lo has adivinado!")


def adivinar_ordenador(x):
    bajo = 1
    alto = x
    feedback = ""
    while feedback != "c":
        feedback = ""
        if bajo != alto:
            adivinar = random.randint(bajo,alto)
        else:
            adivinar = bajo
        feedback = input(f"Es el {adivinar} alto (a), bajo (b) o es correcto (c): ")
        if feedback.lower() == "a":
            alto = adivinar - 1
        elif feedback.lower() == "b":
            bajo = adivinar + 1
    print(f"He acertado! Tu número era el {adivinar}.")
    

adivinar(10)

    