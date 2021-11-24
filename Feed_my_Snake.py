import turtle
import time
from random import random, randrange
print('hello')
def arenaSetup(): # Builds Arena for the Snake
    turtle.tracer(0)
    turtle.hideturtle()
    turtle.shape('turtle')
    turtle.shapesize(2, 2, 4)
    r, g, b = random(), random(), random() # random colors for Arena
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

def introWindow(name): # Introduction of the Game
    turtle.up()
    turtle.hideturtle()
    turtle.goto(-300, 100)
    turtle.write(f"Hey {name}! Welcome to", align="left", font=("Times New Roman", 25))
    turtle.goto(0, 0)
    turtle.write("Feed my Snake", align="center", font=("Times New Roman", 60, "bold"))
    turtle.goto(300, -50)
    turtle.write("Game", align="right", font=("Times New Roman", 25))   
    turtle.goto(450, -200)
    turtle.write("Press Enter to Play......", align="right", font=("Times New Roman", 20, "italic"))

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

def moveUp():
    global snake
    if snake.direction != "down":
        snake.direction = "up"

def moveDown():
    global snake
    if snake.direction != "up":
        snake.direction = "down"

def moveLeft():
    global snake
    if snake.direction != "right":
        snake.direction = "left"

def moveRight():
    global snake
    if snake.direction != "left":
        snake.direction = "right"

def moveSnakeHead(snake):
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)


def moveTheSnake(snake, snakeBody, snakeLength):
    for i in range(snakeLength-1,0,-1): # Loop to move body parts other than 0th indexed part and head
        xOfAheadPart = snakeBody[i-1].xcor()
        yOfAheadPart = snakeBody[i-1].ycor()
        snakeBody[i].goto(xOfAheadPart, yOfAheadPart)                 
    if snakeLength > 0: # Move 0th indexed part
        xOfAheadPart = snake.xcor()
        yOfAheadPart = snake.ycor()
        snakeBody[0].goto(xOfAheadPart, yOfAheadPart)
    moveSnakeHead(snake) # Move the Head

def createBodyPart():
    newBodyPart = turtle.Turtle()
    newBodyPart.speed(0)
    newBodyPart.shape('square')
    newBodyPart.color('black')
    newBodyPart.penup()
    return newBodyPart


def play():
    turtle.tracer(0)
    global sc, snake
    score = 0
    ended = False
    snakeBody = []
    snakeLength = 0
    speedDecider = 0.11 # Changes the speed of snake by decreasing loop sleep
    snake.showturtle()
    food = createFood()
    scoring = createScoring()
    scoring.write("Score:", align="center", font=("Courier",24,"bold"))
    
    sc.onkeypress(moveUp, "Up")
    sc.onkeypress(moveDown, "Down")
    sc.onkeypress(moveLeft, "Left")
    sc.onkeypress(moveRight, "Right")
    
    while True:
        sc.update()
        if snake.distance(food) == 0: # Check if snake ate food
            score += 1 # Firstly, Update the Score
            scoring.clear()
            scoring.write("Score:{}".format(score),align="center",font=("Courier",24,"bold"))
            newBodyPart = createBodyPart() # Secondly, create and add body part to snake
            snakeBody.append(newBodyPart)
            snakeLength += 1
            speedDecider -= 0.001 # Thirdly, Increase Speed
            food.goto(randrange(-480, 480, 20), randrange(-220, 280, 20)) # At Last, Create new food for Snake
            i=0
            while i < snakeLength: # Check whether food is not on snake
                while snake.distance(food) == 0 or snakeBody[i].distance(food) == 0:
                    food.goto(randrange(-480, 480, 20), randrange(-220, 280, 20))
                    i = 0
                else:
                    i += 1
        moveTheSnake(snake, snakeBody, snakeLength)
        if snake.xcor() == 500 or snake.xcor() == -500 or snake.ycor() == 300 or snake.ycor() == -240:
            time.sleep(1)
            scoring.goto(0,0)
            scoring.write("   GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))      
            break
        for part in snakeBody:
            if part.distance(snake) == 0:
                time.sleep(1)
                scoring.goto(0,0)
                scoring.write("    GAME OVER \n Your Score is {}".format(score),align="center",font=("Courier",30,"bold"))
                ended = True
                break
        if ended == True:
            break
        time.sleep(speedDecider)



def onceEnterOnly():
    global isEnterPressed
    if isEnterPressed == False:
        isEnterPressed = True
        arenaSetup()
        play()



isEnterPressed = False

sc = turtle.Screen() # Setting up Turtle Window
sc.title('Feed my Snake')
sc.setup(width = 1.0, height = 1.0)
sc.bgcolor(random(), random(), random())

name = None
while name == None or name == '':
    name = turtle.textinput('Player Name Input', 'Enter Player Name').upper()

arenaSetup() # Builds arena for the Snake
introWindow(name) # Introduction of the Game

snake = createSnake()

sc.onkeypress(onceEnterOnly, 'Return')
sc.listen()

turtle.done()