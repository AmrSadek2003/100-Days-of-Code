from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

score = Scoreboard()
paddle1 = Paddle(position_x=280, position_y=0)
paddle2 = Paddle(position_x=-280, position_y=0)
ball = Ball()

screen.listen()

screen.onkeypress(key='Up', fun=paddle1.move_up)
screen.onkeypress(key='Down', fun=paddle1.move_down)

screen.onkeypress(key='w', fun=paddle2.move_up)
screen.onkeypress(key='s', fun=paddle2.move_down)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    ball.ball_moving()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle1.paddle) < 50 and ball.xcor() > 200 or ball.distance(paddle2.paddle) < 50 and ball.xcor() < -200:
        ball.bounce_x()

screen.exitonclick()
