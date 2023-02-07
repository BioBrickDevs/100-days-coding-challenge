import colorgram
import turtle
import random
colors = colorgram.extract("image.jpg", 30)
list_of_colors = []
print(colors)


for color in colors:
    color.rgb.r
    color.rgb.g
    color.rgb.b
    color_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
    list_of_colors.append(color_tuple)

print(list_of_colors)



turtle.colormode(255)


screen = turtle.Screen()
screen.setup(width=700,height=600, startx=0,starty=-500)
screen.tracer(0,1)
painter = turtle.Turtle()
print(painter.position())
painter.hideturtle()           #make the turtle invisible
painter.penup()
startx = -275
starty = -250
painter.goto(startx, starty)



for y in range(11):
    for x in range(21):
        painter.forward(25)
        painter.dot(20, random.choice(list_of_colors))

    painter.penup()
    painter.goto(startx,starty + y * 50)
turtle.exitonclick()