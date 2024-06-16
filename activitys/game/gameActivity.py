import pygame
from constants import screen, clock
from activitys.game.board import board
from activitys.game import divLine
from activitys.game import GUI

images = {'background': pygame.image.load('assets/images/background.jpg')}

divLine = divLine.DivLine()
gui = GUI.GUI()

class Game:
    def __init__(self):
        pygame.display.set_caption('Carta Mágica | Sg')

    def run(self):
        self.draw()
        gui.run()
        board.run()

    def draw(self):
        # Background
        screen.blit(images['background'], (0, 0))
        # Linha Divisão
        divLine.draw()

    @staticmethod
    def click(pos):
        gui.click(pos)
