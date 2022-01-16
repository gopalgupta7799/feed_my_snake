import turtle
from random import randrange
def createSnake():
    snake = turtle.Turtle()
    snake.hideturtle()
    snake.shape('square')
    snake.shapesize(1.1)
    snake.color('black')
    snake.penup()
    snake.goto(0,0)
    snake.direction = 'stop'
    return snake

def createFood():
    food = turtle.Turtle()
    food.shape('circle')
    food.color('red')
    food.penup()
    food.goto(randrange(-480, 480, 20), randrange(-220, 280, 20))
    return food

def createScoring():
    scoring = turtle.Turtle()
    scoring.color("black")
    scoring.penup()
    scoring.hideturtle()
    scoring.goto(420,320)
    return scoring

def createBodyPart():
    newBodyPart = turtle.Turtle()
    newBodyPart.speed(0)
    newBodyPart.shape('square')
    newBodyPart.color('black')
    newBodyPart.penup()
    return newBodyPart
