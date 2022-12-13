from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,cord):
        super().__init__()
        self.position = cord
        self.new_segment = Turtle()

        self.new_segment.penup()
        self.new_segment.shape("square")
        self.new_segment.color("white")
        self.new_segment.shapesize(stretch_wid=5, stretch_len=1)
        self.new_segment.goto(self.position)

    def up(self):
        self.new_segment.goto(self.new_segment.xcor(), self.new_segment.ycor() + 10)

    def down(self):
        self.new_segment.goto(self.new_segment.xcor(), self.new_segment.ycor() - 10)
