import turtle


#ventana
ventana = turtle.Screen()
ventana.title("pong")
ventana.bgcolor("black") # coor de fondo
ventana.setup(width= 800, height=600) # tamano
ventana.tracer(0) # para que la animacion corra fluida


# marcador
marcadorA = 0
marcadorB = 0

#jugador A
jugadorA = turtle.Turtle()
jugadorA.speed(0)
jugadorA.shape("square") # forma cuadrada
jugadorA.color("white")
jugadorA.penup() #para evitar linea al mover (opcional)
jugadorA.goto(-350,0) # cordena pa la posicion del cuadrado
jugadorA.shapesize(stretch_wid=5, stretch_len=1) # cambiar el cuadrado a rectangulo 

#Jugador B
jugadorB = turtle.Turtle()
jugadorB.speed(0)
jugadorB.shape("square")
jugadorB.color("white")
jugadorB.penup()
jugadorB.goto(350,0)
jugadorB.shapesize(stretch_wid=5, stretch_len=1) 

# pelota
pelota = turtle.Turtle()
pelota.speed(6)
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0,0) # osea en el centro aunque por defecto me lo centra
pelota.dx = 0.5
pelota.dy = 0.5
pelota.dx = -1  # mover pelota
pelota.dy = -1


# linea del centro
division = turtle.Turtle()
division.color("white")
division.goto(0,400)
division.goto(0,-400)


#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)



# funciones 
# A
def jugadorA_UP():
    y = jugadorA.ycor()
    y += 20
    jugadorA.sety(y)

def jugadorA_Down():
    y = jugadorA.ycor()
    y -= 20
    jugadorA.sety(y)


def jugadorB_UP():
    y = jugadorB.ycor()
    y += 20
    jugadorB.sety(y)

def jugadorB_Down():
    y = jugadorB.ycor()
    y -= 20
    jugadorB.sety(y)

# coectrar teclado
ventana.listen()
ventana.onkeypress(jugadorA_UP, "w")
ventana.onkeypress(jugadorA_Down, "s")
ventana.onkeypress(jugadorB_UP, "Up") # up flecca ariba del teclado
ventana.onkeypress(jugadorB_Down, "Down") # up flecha abajo

# bucle pricipal donde ba a correr el juego
# donde el motor del juego va a hir corriendo
while True:
    ventana.update()
    
    # mover pelota 
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    #BORDES
    if pelota.ycor() >290:
        pelota.dy *= -1
    if pelota.ycor() < -290:
        pelota.dy *= -1


    # bordes derecha/izquierda
    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcadorA += 1
        pen.clear()
        pen.write("jugadorA: {}  jugadorB: {}".format(marcadorA,marcadorB ),align='center', font=('Courier', 24, "normal"))

    if pelota.xcor() < -390:
        pelota.goto(0,0)
        pelota.dx *= -1
        marcadorB += 1
        pen.clear()
        pen.write("jugadorA: {}  jugadorB: {}".format(marcadorA,marcadorB ),align='center', font=('Courier', 24, "normal"))


    # choque de barra a pelota
    if ((pelota.xcor() > 340 and pelota.xcor() < 350 )
           and (pelota.ycor() < jugadorB.ycor() + 50
           and pelota.ycor() > jugadorB.ycor() -50)):
        pelota.dx *= -1

    if ((pelota.xcor() < -340 and pelota.xcor() < -350 )
           and (pelota.ycor() < jugadorA.ycor() + 50
           and pelota.ycor() > jugadorA.ycor() -50)):
        pelota.dx *= -1
    





ventana.mainloop() 