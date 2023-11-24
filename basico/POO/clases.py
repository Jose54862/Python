class Personaje:
    def  __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre #Sustitye el atributo por el que se le de
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        
    def atributos(self):
        print("\n", self.nombre, ":", sep="")
        print("-Fuerza:", self.fuerza)
        print("-Inteligencia:",self.inteligencia)
        print("-Defensa:", self.defensa)
        print("-Vida:", self.vida)
        
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
        
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto.")
        
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("La vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()
            

class Guerrero(Personaje): #Hereda de Personaje
    def  __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):  #Para añadir un nuevo metodo necesitas llamar los anteriores
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)  #Da los atributos de la superclase
        self.espada = espada
        
    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) MataKrakens, daño 8. (2) Filo Infinito, daño 10.\n"))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Error. Elige entre (1) y (2)")
            
    def atributos(self):  #Añade el atributo espada
        super().atributos()
        print("-Espada:", self.espada)
        
    def daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa
    

class Mago(Personaje):
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro
        
    def atributos(self):
        super().atributos()
        print("-Libro:", self.libro)
        
    def daño(self, enemigo):
        return self.inteligencia * self.libro - enemigo.defensa

personaje_1 = Personaje("Jose54862", 20, 15, 10, 100)
guts = Guerrero("Guts", 20, 15, 10, 100, 5)
personaje_2 = Mago("Megumin", 20, 10, 10, 100, 5)

def combate(jugador_1, jugador_2):
    turno = 1
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", jugador_1.nombre, ":", sep="")
        jugador_1.atacar(jugador_2)
        print(">>> Acción de ", jugador_2.nombre, ":", sep="")
        jugador_2.atacar(jugador_1)
        turno += 1
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")
        
combate(personaje_1, personaje_2)


