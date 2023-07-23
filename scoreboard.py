from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.pu()
        self.color("white")
        self.hideturtle()
        self.sety(270)
        self.get_score()

    def get_score(self):
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 50
        self.get_score()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER!", move=False, align=ALIGNMENT, font=FONT)

