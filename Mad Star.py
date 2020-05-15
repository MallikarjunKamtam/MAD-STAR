import turtle
import random
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Turtle")
skk = turtle.Turtle()
wn.setup(width=800, height=600)
new = turtle.Turtle()
while True:
    wn.update()
    skk.pendown()
    skk.speed(0)
    skk.color("white")
    skk.forward(random.randint(0, 250))
    skk.right(random.randint(0, 360))
    skk.goto(10, 10)

    wn.update()
    new.pendown()
    new.speed(0)
    new.color("green")
    new.forward(120)
    new.right(random.randint(55, 120))
