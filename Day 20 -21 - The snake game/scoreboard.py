import turtle

class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.setposition(0,250)
        self.color("red")
        self.write("Score: ", move=False,align="center", font=("Arial", 30,"normal"))
        self.score = -1
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 30, "normal"))
