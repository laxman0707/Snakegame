from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 268)
        self.hideturtle()
        self.updatescore()

    def updatescore(self):
        self.write(f"Score:{self.score}", align="center", font=("Arial", 24, "normal"))
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER:{self.score}", align="center", font=("Arial", 24, "normal"))
    def increasescore(self):
        self.score+=1
        self.clear()
        self.updatescore()


