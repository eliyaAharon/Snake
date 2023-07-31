import turtle
from turtle import Turtle
from random import randint

Y_INDEX = 0
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        turtle.colormode(255)
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for square in range(3):
            self.add_segment()

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self):
        global Y_INDEX
        new_seg = Turtle("square")
        new_seg.penup()
        new_seg.color("white")
        new_seg.color((randint(25, 255), randint(25, 255), randint(25, 255)))
        if len(self.segments) > 3:
            new_seg.goto(self.segments[-1].position())
        else:
            new_seg.goto(0, Y_INDEX)
            Y_INDEX -= 20

        self.segments.append(new_seg)

    def extend(self):
        self.add_segment()

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)
