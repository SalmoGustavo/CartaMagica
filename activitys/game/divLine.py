import pygame
from random import randint
from constants import screen

class DivLine:
    def __init__(self):
        self.pos = 1000
        self.width = 15
        self.color = [randint(0, 255), randint(0, 255), randint(0, 255)]
        self.future = [randint(0, 255), randint(0, 255), randint(0, 255)]
        self.velocity = 1

    def draw(self):
        pygame.draw.line(screen, self.color, (self.pos, 0), (self.pos, 1080), self.width)
        self.change_line_color()

    def change_line_color(self):
        if self.color[0] != self.future[0] and self.color[1] != self.future[1] and self.color[2] != self.future[2]:
            # Red
            if self.color[0] < self.future[0]:
                self.color[0] += self.velocity
            if self.color[0] > self.future[0]:
                self.color[0] -= self.velocity

            # Green
            if self.color[1] < self.future[1]:
                self.color[1] += self.velocity
            if self.color[1] > self.future[1]:
                self.color[1] -= self.velocity

            # Blue
            if self.color[2] < self.future[2]:
                self.color[2] += self.velocity
            if self.color[1] > self.future[1]:
                self.color[2] -= self.velocity
        else:
            self.future = [randint(0, 255), randint(0, 255), randint(0, 255)]
