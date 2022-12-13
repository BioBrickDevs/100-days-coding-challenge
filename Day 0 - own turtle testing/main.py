
import turtle
import time
# turtle object
screen = turtle.Screen()
screen.setup(width=1000, height=700)

img_turtle = turtle.Turtle()

# registering the image
# as a new shape
screen.tracer(0)


turtle.register_shape('image.gif')
turtle.register_shape('image2.gif')
# setting the image as cursor

img_turtle.penup()
while True:
    time.sleep(0.1)
    img_turtle.shape('image.gif')
    screen.update()
    img_turtle.speed(1)
    time.sleep(0.1)
    img_turtle.shape('image2.gif')
    time.sleep(0.3)
    img_turtle.forward(10)
    screen.update()
