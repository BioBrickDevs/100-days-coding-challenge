import turtle
import random

screen = turtle.Screen()
screen.setup(width=400, height=300, starty=100)
screen.title("The turtle race.")
bet = screen.textinput("Choose your color for the bet.", "Type the color.").lower()

t_list = []
colors = ["red", "blue", "green", "purple", "yellow", ]
for x in range(5):
    buffer = 50
    t = turtle.Turtle(shape="turtle")
    t.penup()
    t.color(colors[x])
    t.forward(100)
    t.goto(x=-150, y=-100 + x * buffer)
    t.speed(0)
    t_list.append(t)

while True:
    x = random.randint(0, 4)


    t_list[x].forward(1)
    if t_list[x].xcor() > 175:
        winner = t_list[x].pencolor()
        print(f"The winner is {winner}!")
        if winner == bet:
            print("You win the bet!")
        else:
            print("you lost the bet!")
        break



screen.exitonclick()
