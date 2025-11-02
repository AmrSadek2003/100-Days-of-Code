from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(-50, 270)
        self.hideturtle()
        self.momentary_score = 0
        with open("../../../Desktop/highscores.txt", mode="r") as file:
            self.highscore = int(file.read())

    def tally(self):
        self.clear()
        self.write(f"Score: {self.momentary_score}, Highscore: {self.highscore}", font=('Courier', 15, 'normal'))

    def scoreboard_reset(self):
        if self.momentary_score > self.highscore:
            self.highscore = self.momentary_score
            with open("../../../Desktop/highscores.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.momentary_score = 0
    # def game_over(self):
    #     self.goto(x = 0,y = 0)
    #     self.write("GAME OVER", align = "center", font= ('Courier', 30, 'bold'))
