
import turtle
class Answer(turtle.Turtle):
    def __init__(self):
        super().__init__()


    def right(self,x,y,state_name):
    
        writing = turtle.Turtle()
        writing.penup()
        writing.setheading(90)
        writing.setpos(x,y)
        writing.write(str(state_name), move=False, align="center", font=("Arial", 10, "normal"))

        self.list_of_right_answers.append(writing)
    
        




