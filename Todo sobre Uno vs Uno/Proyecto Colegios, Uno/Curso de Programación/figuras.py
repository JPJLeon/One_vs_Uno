##### Figuras para Taller de Programacion #####

import turtle
def cuadrado(turtle):
    for i in range(4):
        turtle.fd(100)
        turtle.right(90)

def triangulo(turtle):
    turtle.left(60)
    turtle.fd(100)
    turtle.right(120)
    turtle.fd(100)
    turtle.right(120)
    turtle.fd(100)
    
def circulo(turtle):
    turtle.speed(0)
    for i in range(360):
        turtle.fd(1)
        turtle.left(1)
    turtle.speed(6)
