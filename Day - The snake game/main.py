import turtle
import time
import snake
import food
import scoreboard

turtle.mode("logo")
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("The snake game")
screen.bgcolor("black")
screen.tracer(0)
food = food.Food()
snake = snake.Snake()
scoreboard =  scoreboard.ScoreBoard()
screen.update()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left,"Left")


game_is_on = True
while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.1)

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        print("Game over")
        game_is_on = False

    for seg in snake.segment_list[1:]:

        if snake.head.distance(seg) < 10:
            game_is_on = False
screen.exitonclick()