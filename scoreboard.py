import turtle
from turtle import Turtle

ALIGNMENT = "center"
FONT = ('courier', 20, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_board()

    def update_board(self):
        self.write(arg=f"Score {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.color((255, 0, 0))
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_board()
