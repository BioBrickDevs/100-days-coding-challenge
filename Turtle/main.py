import turtle
cursor = turtle.Turtle()

cursor.setheading(360)

def draw_shape(trtl, corners):

    angle = 360 / corners
    for x in range(1,corners+1):
        trtl.setheading(angle*x)
        trtl.forward(100)

cursor.speed(10)
# cursor.setheading(90)
# cursor.speed(0)
# cursor.forward(100)
# cursor.setheading(90 + 90)
# cursor.forward(100)
# cursor.setheading(90 + 90 + 90)
# cursor.forward(100)
# cursor.setheading(90 + 90 + 90 + 90)
# cursor.forward(100)




# # for a in range(50):

# #     for x in range(10):
# #         cursor.speed(10)
# #         cursor.forward(5)
# #         cursor.penup()
# #         cursor.forward(5)
# #         cursor.pendown()


#     for i in range(100):
#         cursor.undo()
cursor.color("red")
for x in range(3, 10):
    draw_shape(cursor, x)

turtle.update()
turtle.tracer(0)
cursor.forward(10)


cursor.onclick()