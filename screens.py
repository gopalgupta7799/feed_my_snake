import turtle
from random import random
def arenaSetup():  # Builds Arena for the Snake
    turtle.tracer(0)
    turtle.hideturtle()
    turtle.shape('turtle')
    turtle.shapesize(2, 2, 4)
    r, g, b = random(), random(), random()  # random colors for Arena
    turtle.color((r, g, b), (1 - r, 1 - g, 1 - b))
    turtle.pensize(10)
    turtle.penup()
    turtle.goto(-495, 295)
    turtle.speed(10)
    turtle.showturtle()
    turtle.pendown()
    turtle.begin_fill()
    turtle.tracer(1)
    for i in range(2):
        turtle.forward(495 * 2 + 1)
        turtle.right(90)
        turtle.stamp()
        turtle.forward(531)
        turtle.right(90)
        turtle.stamp()
    turtle.end_fill()


def introWindow(name):  # Introduction of the Game
    turtle.up()
    turtle.hideturtle()
    turtle.goto(-300, 100)
    turtle.write(f"Hey {name}! Welcome to", align="left",
                 font=("Times New Roman", 25))
    turtle.goto(0, 0)
    turtle.write("Feed my Snake", align="center",
                 font=("Times New Roman", 60, "bold"))
    turtle.goto(300, -50)
    turtle.write("Game", align="right", font=("Times New Roman", 25))
    turtle.goto(450, -200)
    turtle.write("Press Enter to Play......", align="right",
                 font=("Times New Roman", 20, "italic"))
