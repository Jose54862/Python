import pygame
import turtle
import time
import random
import pandas

pygame.init()

posponer = 0.08

#Marcador
score = 0
high_score = 0

#Configurar la ventana
wd = turtle.Screen()
wd.title("Snake")
wd.bgcolor("black")  #Color de fondo de pantalla
wd.setup(width = 600,height = 600)
wd.tracer(0)

#Cabeza serpiente
cabeza = turtle.Turtle()
cabeza.speed(1)
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()  #Quita el rastro que deja al andar
cabeza.goto(0,0)  #Posicion que inicia
cabeza.direction = "stop"

#Comida
comida = turtle.Turtle()
comida.speed(1)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

#Cuerpo de la serpiente
segmentos = []

#Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0    High Score: 0", align = "center", font = ("Courier", 24,"normal"))

#Funciones
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def derecha():
    cabeza.direction = "right"
def izquierda():
    cabeza.direction = "left"



def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
        
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
        
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)
        
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

#Teclado
wd.listen() #Conectar teclado?
wd.onkeypress(arriba, "Up")
wd.onkeypress(arriba, "W")
wd.onkeypress(abajo, "Down")
wd.onkeypress(derecha, "Right")
wd.onkeypress(izquierda, "Left")


while True:
    wd.update()
    
    #Colisiones bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -290 or cabeza.ycor() > 280 or cabeza.ycor() < -290:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"
        
        #Esconder los segmentos
        for segmento in segmentos:
            segmento.goto(1000,1000)
    
        #Limpiar lista de segmentos
        segmentos.clear()
        
        #Resetear marcador
        score = 0
        texto.clear()
        texto.write("Score: {}    High Score: {}".format(score, high_score), align = "center", font = ("Courier", 24,"normal"))
    
    if cabeza.distance(comida) < 30:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)
        
        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(1)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("grey")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)
        
        #Aumentar marcador
        score += 10
        
        if score > high_score:
            high_score =  score
        
        texto.clear()
        texto.write("Score: {}    High Score: {}".format(score, high_score), align = "center", font = ("Courier", 24,"normal"))

    #Mover el cuerpo de la serpiente
    totalSeg = len(segmentos)
    for index in range(totalSeg -1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)
    
    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)
    
    mov()   
    
    #Colisiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"
            
            #Esconder los segmentos
            for segmento in segmentos:
                segmento.goto(1000,1000)
                
            segmentos.clear()
    
    
    time.sleep(posponer)