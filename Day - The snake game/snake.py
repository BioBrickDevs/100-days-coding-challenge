import turtle
import time

UP = 0
DOWN = 180
LEFT = 270
RIGHT = 90


class Snake:

    def __init__(self):
        self.turtle2 = None
        self.segment_list = []
        self.postitons_list = [(0, 0), (-20, 0), (-40, 0)]

        for seg in self.postitons_list:
            self.add_segment(seg)

    def add_segment(self, seg):
        self.turtle2 = turtle.Turtle()
        self.turtle2.penup()
        self.turtle2.color("white")
        self.turtle2.shape("square")
        self.turtle2.goto(seg)

        self.segment_list.append(self.turtle2)

        self.head = self.segment_list[0]

    def extend(self):
        self.add_segment(self.segment_list[-1].position())

    def move(self):
        for x in range(len(self.segment_list) - 1, 0, -1):
            self.new_x = self.segment_list[x - 1].xcor()
            self.new_y = self.segment_list[x - 1].ycor()
            self.segment_list[x].goto(self.new_x, self.new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
