from turtle import Turtle
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.goto(x=0, y=0)
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def ball_moving(self):

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    def bounce_x(self):

        self.x_move *= -1
    def bounce_y(self):

        self.y_move *= -1
