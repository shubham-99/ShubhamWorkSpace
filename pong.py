import turtle
import random

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0
obj = turtle.Turtle()
obj.speed(0)
obj.shape("circle")
obj.color("red")

obj.penup()
obj.goto(0,0)
# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(-150, 200)
ball.dx = 0.5
ball.dy = 0.5

k=0
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 50
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 50
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 50
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 50
    paddle_b.sety(y)

def quit():
    turtle.bye()
# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(quit, "q")

# Main game loop
while True:
    wn.update()
    if score_a==20:
        pen.goto(0,200)
        pen.write("Player A wins", align="center", font=("Courier", 24, "normal"))

        turtle.done()
    if score_b == 20:
        pen.goto(0, 200)
        pen.write("Player B wins", align="center", font=("Courier", 24, "normal"))

        turtle.done()
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1


    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        if k>0:

            ball.goto(0, 250)
            ball.color("blue")
            ball.dx = 0.5
            ball.dy = 0.5
            k = 0
            a = random.randrange(-300, 300)
            b = random.randrange(-250, 250)
            obj.goto(a, b)

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

        if k>0:


            ball.goto(0,250)
            ball.color("blue")
            ball.dx=0.5
            ball.dy=0.5
            k=0
            a=random.randrange(-300,300)
            b=random.randrange(-250,250)
            obj.goto(a,b)
            obj.color("red")
    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1


    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1

    if abs(obj.xcor()-ball.xcor())<=10:
        if abs(obj.ycor()-ball.ycor())<=10:

            ball.color("red")
            if ball.dx>0:
                ball.dx=0.7
            else:
                ball.dx=-0.7

            if ball.dy > 0:
                ball.dy = 0.7
            else:
                ball.dy = -0.7
            k+=1
