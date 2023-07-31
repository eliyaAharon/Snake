import turtle
from turtle import Turtle
from random import randint

WINDOW_LEN = 600


class Food(Turtle):

    def __init__(self):
        super().__init__()
        turtle.colormode(255)
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.change_place()

    def change_place(self):
        color = (randint(40, 255), randint(40, 255), randint(40, 255))
        self.color(color)
        self.goto(randint(-260, 260), randint(-260, 260))
