import turtle
from turtle import Turtle

ALIGNMENT = "center"
FONT = ('courier', 20, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score_data.txt") as file:
            self.high_score = file.read()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(arg=f"Score {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("score_data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_board()

    def add_score(self):
        self.score += 1
        self.update_board()
