# pong game in Python
# explanation and walkthrough at https://youtu.be/xzuguCSizWw

import turtle


# initialize game window
window = turtle.Screen()
window.title("Python Ping Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# paddle 1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("blue")
paddle1.penup()
paddle1.goto(-350, 0)
paddle1.shapesize(stretch_wid=5, stretch_len=1)

# paddle 2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("red")
paddle2.penup()
paddle2.goto(350, 0)
paddle2.shapesize(stretch_wid=5, stretch_len=1)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = -0.3

# score
score = turtle.Turtle()
score_p1 = 0
score_p2 = 0

score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)

# function to print the score, clears it first then prints with new values


def print_score():
    score.clear()
    score.write(f"Player 1: {score_p1} Player 2: {score_p2}",
                align="center", font=("Courier", 11, "normal"))


print_score()


# functions to move paddles up or down
def paddle1_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)


def paddle1_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)


def paddle2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)


def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)


# keyboard bindings
window.listen()
window.onkey(paddle1_up, "w")
window.onkey(paddle1_down, "s")

window.onkey(paddle2_up, "Up")
window.onkey(paddle2_down, "Down")

# main game loop
while True:
    window.update()

    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # check if ball touches edge
    # top edge
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # bottom edge
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # right edge
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_p1 += 1
        print_score()

    # left edge
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_p2 += 1
        print_score()

    # check collision between ball and paddle
    # if condition explanation in yt video @ minute 52
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
