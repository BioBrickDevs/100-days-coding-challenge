import pygame


class Paddle(pygame.Rect):
    def __init__(self, center_pos_x, center_pos_y):
        super().__init__(self.width, self.height, self.y, self.x)

        self.width = 20
        self.height = 100
        self.centerx = center_pos_x
        self.centery = center_pos_y

    def up(self):
        if self.centery > 50:
            self.centery -= 6

    def down(self):
        if self.centery < 550:
            self.centery += 6

