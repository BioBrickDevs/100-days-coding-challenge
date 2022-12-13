import pygame


class Ball:
    def __init__(self):
        self.x = 400
        self.y = 300
        self.x_move = 4
        self.y_move = 4

    def move(self):
        self.x += self.x_move
        self.y += self.y_move

    def reverse(self):
        self.y_move *= -1
