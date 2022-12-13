import pygame
import paddle
import ball
import math
import random


def random_way():
    number = random.randint(0, 1)
    if number == 1:
        return -1
    if number == 0:
        return 1


pygame.init()

screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

position = 300
l_paddle = paddle.Paddle(center_pos_y=300, center_pos_x=20)
r_paddle = paddle.Paddle(center_pos_y=300, center_pos_x=780)
ball = ball.Ball()
keys = pygame.key.get_pressed()
pygame.key.set_repeat()
while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        l_paddle.up()
    if keys[pygame.K_s]:
        # Mo ve Down
        l_paddle.down()

    if keys[pygame.K_UP]:
        # Render the graphics here.
        r_paddle.up()

    if keys[pygame.K_DOWN]:
        r_paddle.down()

    if ball.x > 812 or ball.x < -12:
        ball.y_move = 4 * random_way()
        ball.x_move = 4 * random_way()
        ball.x = 400
        ball.y = 300

        ball.y_move = 4 * random_way()
        ball.x_move = 4 * random_way()

    r_list_of_pixels = []

    for y in range(-50, 51, 1):
        x = -10
        r_list_of_pixels.append([x, y])

    for cord in r_list_of_pixels:

        if ball.y > 590 or ball.y < 10:
            ball.reverse()

        if math.dist([ball.x, ball.y], [r_paddle.centerx + cord[0], r_paddle.centery + cord[1]]) < 10:
            if ball.y > 0:
                ball.y += 1

            else:
                ball.y -= 1

            ball.x_move *= -1

            if ball.x_move > 0:

                ball.x_move += 1
            else:
                ball.x_move -= 1

            break

        if math.dist([ball.x, ball.y], [l_paddle.centerx - cord[0], l_paddle.centery + cord[1]]) < 10:
            ball.x_move *= -1

            if ball.y > 0:
                ball.y += 1

            else:
                ball.y -= 1

            if ball.x_move > 0:

                ball.x_move += 1
            else:
                ball.x_move -= 1

            break
    ball.move()

    screen.fill("black")  # Fill the display with a solid color
    pygame.draw.rect(screen, "white", l_paddle)
    pygame.draw.rect(screen, "white", r_paddle)
    pygame.draw.circle(screen, "white", (ball.x, ball.y), 10)

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)  # wait until next frame (at 60 FPS)
