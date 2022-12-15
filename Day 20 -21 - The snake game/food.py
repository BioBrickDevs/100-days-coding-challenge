import turtle
import random


class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.setposition(random_x, random_y)
