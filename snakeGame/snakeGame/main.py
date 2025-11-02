from turtle import Turtle, Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

new_snake = Snake()

new_food = Food()

new_scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(fun=new_snake.up, key="Up")
screen.onkeypress(fun=new_snake.down, key="Down")
screen.onkeypress(fun=new_snake.right, key="Right")
screen.onkeypress(fun=new_snake.left, key="Left")

game_is_on = True

current_score = 0

while game_is_on:
    screen.update()
    time.sleep(0.1)
    new_snake.move()
    new_scoreboard.tally()

    if new_snake.check_collision_wall():
        current_score = 0
        new_scoreboard.scoreboard_reset()
        new_snake.snake_reset()

    if new_snake.check_collision_self():
        current_score = 0
        new_scoreboard.scoreboard_reset()
        new_snake.snake_reset()

    if new_snake.head.distance(new_food) < 15:
        new_food.refresh()
        new_snake.grow()
        current_score +=1
        new_scoreboard.momentary_score = current_score


screen.exitonclick()
