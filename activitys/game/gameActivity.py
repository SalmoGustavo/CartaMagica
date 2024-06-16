import pygame
from constants import screen, clock

images = {'background': pygame.image.load('assets/images/background.jpg')}

class Game:
    def __init__(self):
        pygame.display.set_caption('Carta Mágica | Sg')

    def run(self):
        self.draw()

    def draw(self):
        # Background
        screen.blit(images['background'], (0, 0))
