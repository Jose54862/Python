import time

def cuenta_regresiva(t):
    while t:
        mins, secs = divmod(t, 60)
        temporizador = "{:02d} {:02d}".format(mins, secs)
        print(temporizador, end="\r")
        time.sleep(1)
        t -= 1
        
    print("Completado!")
t = input("Introduzca el tiempo en segundos: ")
cuenta_regresiva(int(t))