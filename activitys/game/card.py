import pygame
from constants import screen

# Carregando Imagens das Cartas
cards_sheet = pygame.image.load('assets/images/cards.png')
card_size_x = cards_sheet.get_size()[0] / 13
card_size_y = cards_sheet.get_size()[1] / 4

cards_images = []

for y in range(4):
    for x in range(13):
        card = cards_sheet.subsurface((x * card_size_x, y * card_size_y, card_size_x, card_size_y))
        cards_images.append(card)

class Card:
    def __init__(self, card_type, pos, size=(card_size_x, card_size_y)):
        self.type = card_type
        self.pos = pos
        self.size = size
        self.visible = True

    def draw(self, pos):
        if self.visible:
            space_x = 50

            pos_x = pos[0] + (self.pos[0] * self.size[0])
            pos_y = pos[1] + (self.pos[1] * (self.size[0] / 2))

            if self.pos[0] == 1:
                pos_x += space_x
            if self.pos[0] == 2:
                pos_x += (space_x * 2)

            screen.blit(cards_images[self.type], (pos_x, pos_y))

