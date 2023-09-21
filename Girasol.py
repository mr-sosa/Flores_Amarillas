import math
import turtle
import colorsys

# Configuración inicial
turtle.bgcolor("light sky blue")
turtle.shape("turtle")
turtle.speed(0)
turtle.fillcolor("brown")

# Dibuja el tallo
turtle.penup()
turtle.goto(0, -300)
turtle.pendown()
turtle.setheading(90)
turtle.color("green")
turtle.fillcolor("green")  # Cambia el color del tallo a verde
turtle.begin_fill()
turtle.forward(300)
turtle.left(90)
turtle.forward(20)
turtle.left(90)
turtle.forward(300)
turtle.end_fill()

# Dibujar el girasol
h = 0
turtle.penup()
turtle.goto(-40, 0)
turtle.pendown()
for i in range(16):
    for j in range(18):
        turtle.color("yellow")  # Todos los pétalos son amarillos
        h += 0.005
        turtle.rt(90)
        turtle.circle(150 - j * 6, 90)
        turtle.lt(90)
        turtle.circle(150 - j * 6, 90)
        turtle.rt(180)
    turtle.circle(40, 24)

# Cambia el color del centro del girasol a café más claro (RGB: 139, 69, 19)
turtle.penup()
turtle.goto(0, -180)
turtle.color("black")
turtle.fillcolor("#8B4513")  # Café más claro
turtle.begin_fill()
turtle.circle(0)
turtle.end_fill()

# Código del girasol (el que proporcionaste)
phi = 137.508 * (math.pi / 180.0)
for i in range(160):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(i * 137.508)
    turtle.pendown()
    if i < 160:
        turtle.stamp()
    
# Escribe "Te Amitos" en la parte superior del girasol
turtle.penup()
turtle.goto(0, 250)  # Ajusta la posición vertical según sea necesario
turtle.color("yellow")  # Color del texto
turtle.write("Te amitos mi solecito ♥️", align="center", font=("Alex Brush", 30, "bold"))

# Escribe "La fecha" en la parte inferior del girasol
turtle.penup()
turtle.goto(250, -300)  # Ajusta la posición vertical según sea necesario
turtle.color("black")  # Color del texto
turtle.write("Septiembre 21, 2023", align="center", font=("Alex Brush", 15))

# Oculta el cursor de la tortuga antes de salir
turtle.hideturtle()

# Cierra la ventana al hacer clic
turtle.exitonclick()
