from turtle import Turtle


class Paddle:
    def __init__(self, position_x, position_y):
        self.paddle = Turtle(shape="square")
        self.paddle.penup()
        self.paddle.shapesize(stretch_len=0.5, stretch_wid=3)
        self.paddle.color("white")
        self.paddle.setposition(x = position_x, y = position_y)

    def move_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def move_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)
