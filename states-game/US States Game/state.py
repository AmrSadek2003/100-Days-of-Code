from turtle import Turtle, Screen


class State(Turtle):

    def __init__(self, user_input,x_input, y_input ):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=x_input, y=y_input)
        self.write(user_input)

