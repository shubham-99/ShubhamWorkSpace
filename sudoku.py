# Sudoku Generator Algorithm - www.101computing.net/sudoku-generator-algorithm/
import turtle
from random import randint, shuffle
from time import sleep
point=turtle.Turtle()
point.speed(0)
point.shape("square")
point.color('blue')
point.penup()
point.shapesize(stretch_wid=0.5, stretch_len=0.5)
point.goto(-125, 125)
# initialise empty 9 by 9 grid
grid = [[0 for cols in range(9)] for rows in range(9)]
wn=turtle.Screen()

myPen = turtle.Turtle()
wn.tracer(0)
myPen.speed(0)
myPen.color("#000000")
myPen.hideturtle()
topLeft_x = -150
topLeft_y = 150
pinpen = turtle.Turtle()
pinpen.speed(0)
pinpen.shape("square")
pinpen.color("red")
pinpen.penup()
pinpen.hideturtle()

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("red")
pen.penup()
pen.hideturtle()

pen.penup()
def text(message, x, y, size):
    FONT = ('Arial', size, 'normal')
    myPen.penup()
    myPen.goto(x, y)
    myPen.write(message, align="left", font=FONT)


# A procedure to draw the grid on screen using Python Turtle
def drawGrid(grid):
    intDim = 35
    for row in range(0, 10):
        if (row % 3) == 0:
            myPen.pensize(6)
        else:
            myPen.pensize(3)


        myPen.penup()
        myPen.goto(topLeft_x, topLeft_y - row * intDim)
        myPen.pendown()
        myPen.goto(topLeft_x + 9 * intDim, topLeft_y - row * intDim)
    for col in range(0, 10):
        if (col % 3) == 0:
            myPen.pensize(6)
        else:
            myPen.pensize(3)


        myPen.penup()
        myPen.goto(topLeft_x + col * intDim, topLeft_y)
        myPen.pendown()
        myPen.goto(topLeft_x + col * intDim, topLeft_y - 9 * intDim)

    for row in range(0, 9):
        for col in range(0, 9):

            if grid[row][col] != 0:
                text(grid[row][col], topLeft_x + col * intDim + 9, topLeft_y - row * intDim - intDim + 8, 18)


# A function to check if the grid is full
def checkGrid(grid):
    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] == 0:
                return False

    # We have a complete grid!
    return True


# A backtracking/recursive function to check all possible combinations of numbers until a solution is found
def solveGrid(grid):
    global counter
    # Find next empty cell
    for i in range(0, 81):
        row = i // 9
        col = i % 9
        if grid[row][col] == 0:
            for value in range(1, 10):
                # Check that this value has not already be used on this row
                if not (value in grid[row]):
                    # Check that this value has not already be used on this column
                    if not value in (
                    grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col], grid[5][col], grid[6][col],
                    grid[7][col], grid[8][col]):
                        # Identify which of the 9 squares we are working on
                        square = []
                        if row < 3:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(0, 3)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(0, 3)]
                            else:
                                square = [grid[i][6:9] for i in range(0, 3)]
                        elif row < 6:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(3, 6)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(3, 6)]
                            else:
                                square = [grid[i][6:9] for i in range(3, 6)]
                        else:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(6, 9)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(6, 9)]
                            else:
                                square = [grid[i][6:9] for i in range(6, 9)]
                        # Check that this value has not already be used on this 3x3 square
                        if not value in (square[0] + square[1] + square[2]):
                            grid[row][col] = value
                            if checkGrid(grid):
                                counter += 1
                                break
                            else:
                                if solveGrid(grid):
                                    return True
            break
    grid[row][col] = 0


numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# shuffle(numberList)

# A backtracking/recursive function to check all possible combinations of numbers until a solution is found
def fillGrid(grid):
    global counter
    # Find next empty cell
    for i in range(0, 81):
        row = i // 9
        col = i % 9
        if grid[row][col] == 0:
            shuffle(numberList)
            for value in numberList:
                # Check that this value has not already be used on this row
                if not (value in grid[row]):
                    # Check that this value has not already be used on this column
                    if not value in (
                    grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col], grid[5][col], grid[6][col],
                    grid[7][col], grid[8][col]):
                        # Identify which of the 9 squares we are working on
                        square = []
                        if row < 3:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(0, 3)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(0, 3)]
                            else:
                                square = [grid[i][6:9] for i in range(0, 3)]
                        elif row < 6:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(3, 6)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(3, 6)]
                            else:
                                square = [grid[i][6:9] for i in range(3, 6)]
                        else:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(6, 9)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(6, 9)]
                            else:
                                square = [grid[i][6:9] for i in range(6, 9)]
                        # Check that this value has not already be used on this 3x3 square
                        if not value in (square[0] + square[1] + square[2]):
                            grid[row][col] = value
                            if checkGrid(grid):
                                return True
                            else:
                                if fillGrid(grid):
                                    return True
            break
    grid[row][col] = 0


# Generate a Fully Solved Grid
fillGrid(grid)

myPen.getscreen().update()
sleep(1)
sua=''
for id in grid:
    for jd in id:
        sua+=str(jd)

# Start Removing Numbers one by one

# A higher number of attempts will end up removing more numbers from the grid
# Potentially resulting in more difficiult grids to solve!
attempts=3
counter=1
while attempts > 0:
    # Select a random cell that is not already empty
    row = randint(0, 8)
    col = randint(0, 8)
    while grid[row][col] == 0:
        row = randint(0, 8)
        col = randint(0, 8)
    # Remember its cell value in case we need to put it back
    backup = grid[row][col]
    grid[row][col] = 0

    # Take a full copy of the grid
    copyGrid = []
    for r in range(0, 9):
        copyGrid.append([])
        for c in range(0, 9):
            copyGrid[r].append(grid[r][c])

    # Count the number of solutions that this grid has (using a backtracking approach implemented in the solveGrid() function)
    counter = 0
    solveGrid(copyGrid)
    # If the number of solution is different from 1 then we need to cancel the change by putting the value we took away back in the grid
    if counter != 1:
        grid[row][col] = backup
        # We could stop here, but we can also have another attempt with a different cell just to try to remove more numbers
        attempts -= 1

    myPen.clear()

    myPen.getscreen().update()
see=grid.copy()
suii=[]
for i in range(0,8):
    for j in range(0,8):
        if grid[i][j] in range(1,10):

            suii.append(j+1+i*9)

drawGrid(grid)

print("Enter a,w,s,d to navigate")
print("At a valid position you can Enter the numer you want")
print("Enter 10 when finished")
print("Enter 20 to reset")
l=100
i=0
j=0



s=0
re=0
uu=0
dd=0

def up():
    global i
    global uu
    global dd

    y = point.ycor()
    if i > 0:
        i -= 1
        y += 35
        point.sety(y)
        if dd>0:
            pen.clear()
            dd=0
        pinpen.clear()
    else:
        pen.hideturtle()
        pen.goto(0, -260)
        pen.clear()
        pen.write("Cannot move up", align="center", font=("Courier", 12, "normal"))
        uu += 1


def down():
    global i
    global dd
    global uu
    y = point.ycor()
    if i < 8:
        i += 1
        y -= 35
        point.sety(y)
        if uu>0:
            pen.clear()
            uu=0
        pinpen.clear()
    else:
        pen.hideturtle()
        pen.goto(0, -260)
        pen.clear()
        pen.write("Cannot move down", align="center", font=("Courier", 12, "normal"))
        dd += 1


def left():
    global j
    global s
    global re

    x = point.xcor()
    if j > 0:
        j -= 1
        x -= 35
        point.setx(x)
        if re>0:
            pen.clear()
            re=0
        pinpen.clear()
    else:

        pen.hideturtle()
        pen.goto(0, -260)
        pen.clear()
        pen.write("Cannot move left", align="center", font=("Courier", 12, "normal"))
        s+=1



def right():
    global j
    global s
    global re
    x = point.xcor()
    pinpen.clear()
    if j < 8:
        j += 1
        x += 35
        point.setx(x)
        if s>0:
            pen.clear()
            s=0
        pinpen.clear()
    else:
        pen.hideturtle()
        pen.goto(0,-260)
        pen.clear()
        pen.write("Cannot move right", align="center", font=("Courier", 12, "normal"))
        re+=1

def one():
    global j
    global i


    if grid[i][j] not in range(1,10):

        grid[i][j]=1

        myPen.getscreen().update()
        drawGrid(grid)

    else:
        pen.hideturtle()
        pinpen.goto(0, -200)
        pinpen.clear()
        pinpen.write("Cannot place here", align="center", font=("Courier", 12, "normal"))

def two():
    global j
    global i

    if grid[i][j] not in range(1, 10):
        grid[i][j] = 2

        myPen.getscreen().update()
        drawGrid(grid)

    else:
        pinpen.hideturtle()
        pinpen.goto(0, -200)
        pinpen.clear()
        pinpen.write("Cannot place here", align="center", font=("Courier", 12, "normal"))

def three():

    global j
    global i
    global pop
    global pos
    if grid[i][j] not in range(1, 10):
        grid[i][j] = 3

        myPen.getscreen().update()
        drawGrid(grid)

    else:
        pinpen.hideturtle()
        pinpen.goto(0, -200)
        pinpen.clear()
        pinpen.write("Cannot place here", align="center", font=("Courier", 12, "normal"))

def four():
    global j
    global i
    global pop
    global pos
    if grid[i][j] not in range(1, 10):
        grid[i][j] = 4

        myPen.getscreen().update()
        drawGrid(grid)

    else:
        pinpen.hideturtle()
        pinpen.goto(0, -200)
        pinpen.clear()
        pinpen.write("Cannot place here", align="center", font=("Courier", 12, "normal"))

def five():
    global j
    global i
    if grid[i][j] not in range(1, 10):
        grid[i][j] = 5

        myPen.getscreen().update()
        drawGrid(grid)

    else:
        pinpen.hideturtle()
        pinpen.goto(0, -200)
        pinpen.clear()
        pinpen.write("Cannot place here", align="center", font=("Courier", 12, "normal"))
def six():
    global j
    global i
    if grid[i][j] not in range(1, 10):
        grid[i][j] = 6

        myPen.getscreen().update()
        drawGrid(grid)

    else:
        pinpen.hideturtle()
        pinpen.goto(0, -200)
        pinpen.clear()
        pinpen.write("Cannot place here", align="center", font=("Courier", 12, "normal"))
def seven():
    global j
    global i
    if grid[i][j] not in range(1, 10):
        grid[i][j] = 7

        myPen.getscreen().update()
        drawGrid(grid)

    else:
        pinpen.hideturtle()
        pinpen.goto(0, -200)
        pinpen.clear()
        pinpen.write("Cannot place here", align="center", font=("Courier", 12, "normal"))
def eight():
    global j
    global i
    if grid[i][j] not in range(1, 10):
        grid[i][j] = 8

        myPen.getscreen().update()
        drawGrid(grid)

    else:
        pinpen.hideturtle()
        pinpen.goto(0, -200)
        pinpen.clear()
        pinpen.write("Cannot place here", align="center", font=("Courier", 12, "normal"))
def nine():
    global j
    global i



    if grid[i][j] not in range(1, 10):
        grid[i][j] = 9

        myPen.getscreen().update()
        drawGrid(grid)

    else:
        pinpen.hideturtle()
        pinpen.goto(0, -200)
        pinpen.clear()
        pinpen.write("Cannot place here", align="center", font=("Courier", 12, "normal"))
def finish():
    pinpen.clear()
    pen.clear()
    sae=''
    global sua
    for id in grid:
        for jd in id:
            sae+=str(jd)
    if sae==sua:

        pen.hideturtle()
        pen.goto(0, 260)
        pen.color("Green")
        pen.write("You WIn", align="center", font=("Courier", 24, "bold"))

    else:

        pen.hideturtle()
        pen.goto(0, 260)

        pen.write("You lost", align="center", font=("Courier", 24, "bold"))
    turtle.done()
def call():
    global i
    global j
    myPen.clear()
    grid[i][j] = 0
    drawGrid(grid)

def back():
    global i
    global j



    if (j+1+9*i) not in suii:
            call()



def reset():
    myPen.clear()
    for i in range(0, 8):
        for j in range(0, 8):

            if (j+1+9*i) not in suii:
                    grid[i][j]=0

    myPen.clear()
    drawGrid(grid)


def quit():
    turtle.bye()

wn.listen()
wn.onkeypress(up, "Up")
wn.onkeypress(up,"w")
wn.onkeypress(down, "s")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "a")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "d")
wn.onkeypress(right, "Right")
wn.onkeypress(one, "1")
wn.onkeypress(two, "2")
wn.onkeypress(three, "3")
wn.onkeypress(four, "4")
wn.onkeypress(five, "5")
wn.onkeypress(six, "6")
wn.onkeypress(seven, "7")
wn.onkeypress(eight, "8")
wn.onkeypress(nine, "9")
wn.onkeypress(finish, "Return")
wn.onkeypress(back, "b")
wn.onkeypress(reset, "r")
wn.onkeypress(quit, "q")

while True:
    wn.update()



