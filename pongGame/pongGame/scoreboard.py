from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_p1 = 0
        self.score_p2 = 0
        self.penup()
        self.goto(0, 230)
        self.color("white")
        self.tally()
        self.hideturtle()
        self.dashmarks()

    def tally(self):
        self.clear()
        self.write(f"{self.score_p1}   {self.score_p2}", align="center", font=('Futura', 40, 'bold'))

    def dashmarks(self):
        x_position = 0
        y_position = 280
        for i in range(1, 13):
            new_dash = Turtle("square")
            new_dash.penup()
            new_dash.shapesize(stretch_len=0.25, stretch_wid=1.5)
            new_dash.color("white")
            new_dash.goto(x_position, y_position)
            y_position -= 50
