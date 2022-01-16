import time
import turtle
from screens import *
from create_elements import *
from random import random, randrange

print('Hello! Welcome to Feed My Snake Game')


def moveUp():
    if snake.direction != "down":
        snake.direction = "up"


def moveDown():
    if snake.direction != "up":
        snake.direction = "down"


def moveLeft():
    if snake.direction != "right":
        snake.direction = "left"


def moveRight():
    if snake.direction != "left":
        snake.direction = "right"


def moveSnakeHead(snake):
    if snake.direction == "up":
        snake.sety(snake.ycor() + 20)
    if snake.direction == "down":
        snake.sety(snake.ycor() - 20)
    if snake.direction == "left":
        snake.setx(snake.xcor() - 20)
    if snake.direction == "right":
        snake.setx(snake.xcor() + 20)


def moveTheSnake(snake, snakeBody, snakeLength):
    # Loop to move body parts other than 0th indexed part and head
    for i in range(snakeLength-1, 0, -1):
        xOfAheadPart = snakeBody[i-1].xcor()
        yOfAheadPart = snakeBody[i-1].ycor()
        snakeBody[i].goto(xOfAheadPart, yOfAheadPart)
    if snakeLength > 0:  # Move 0th indexed part
        xOfAheadPart = snake.xcor()
        yOfAheadPart = snake.ycor()
        snakeBody[0].goto(xOfAheadPart, yOfAheadPart)
    moveSnakeHead(snake)  # Move the Head


def foodPositioner(food, score):
    if score % 50 == 0 and score != 0:
        food.shapesize(2, 2, 2)
        food.goto(randrange(-440, 440, 20), randrange(-180, 240, 20))
    else:
        food.shapesize(1, 1, 1)
        food.goto(randrange(-480, 480, 20), randrange(-220, 280, 20))


def checkDistance(one, two, score):
    if score % 50 == 0 and score != 0:
        if one.distance(two) <= 20:
            return True
        else:
            return False
    else:
        if one.distance(two) == 0:
            return True
        else:
            return False


def play():
    turtle.tracer(0)
    score = 0
    ended = False
    snakeBody = []
    snakeLength = 0
    speedDecider = 0.11  # Changes the speed of snake by decreasing loop sleep
    snake.showturtle()
    food = createFood()
    foodPositioner(food, score)
    scoring = createScoring()
    scoring.write("Score:", align="center", font=("Courier", 24, "bold"))
    sc.onkeypress(moveUp, "Up")
    sc.onkeypress(moveDown, "Down")
    sc.onkeypress(moveLeft, "Left")
    sc.onkeypress(moveRight, "Right")

    while True:
        sc.update()
        if checkDistance(snake, food, score):  # Check if snake ate food
            if score % 50 == 0 and score != 0:
                score += 60  # Firstly, Update the Score
            else:
                score += 10  # Firstly, Update the Score
            scoring.clear()
            scoring.write(f"Score:{score}",
                          align="center", font=("Courier", 24, "bold"))
            newBodyPart = createBodyPart()  # Secondly, create and add body part to snake
            snakeBody.append(newBodyPart)
            snakeLength += 1
            speedDecider -= 0.001  # Thirdly, Increase Speed
            # At Last, Create new food for Snake
            foodPositioner(food, score)
            i = 0
            while i < snakeLength:  # Check whether food is not on snake
                while checkDistance(snake, food, score) or checkDistance(snakeBody[i], food, score):
                    foodPositioner(food, score)
                    i = 0
                else:
                    i += 1
        moveTheSnake(snake, snakeBody, snakeLength)
        if snake.xcor() == 500 or snake.xcor() == -500 or snake.ycor() == 300 or snake.ycor() == -240:
            time.sleep(1)
            scoring.goto(0, 0)
            scoring.write(f"   GAME OVER \n Your Score is {score}", align="center", font=(
                "Courier", 30, "bold"))
            break
        for part in snakeBody:
            if part.distance(snake) == 0:
                time.sleep(1)
                scoring.goto(0, 0)
                scoring.write(f"    GAME OVER \n Your Score is {score}", align="center", font=(
                    "Courier", 30, "bold"))
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

sc = turtle.Screen()  # Setting up Turtle Window
sc.title('Feed my Snake')
sc.setup(width=1.0, height=1.0)
sc.bgcolor(random(), random(), random())

name = None
while name == None or name == '':
    name = turtle.textinput('Player Name Input', 'Enter Player Name').upper()

arenaSetup()  # Builds arena for the Snake
introWindow(name)  # Introduction of the Game

snake = createSnake()

sc.onkeypress(onceEnterOnly, 'Return')
sc.listen()

turtle.done()
