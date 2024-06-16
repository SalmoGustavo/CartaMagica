import pygame
from constants import screen, clock
from activitys.game import card
from random import randint

class Board:
    def __init__(self):
        self.cards = []
        self.put_cards()

    def put_cards(self):
        self.cards = []
        choiceds = []

        for x in range(3):
            line = []
            for y in range(7):
                ok = False
                while not ok:
                    number = randint(0, 51)
                    if number not in choiceds:
                        card_item = card.Card(randint(0, 51), [x, y])
                        ok = True
                line.append(card_item)

            self.cards.append(line)

    def distribute(self, no_centro):
        coluna1 = self.cards[0]
        coluna2 = self.cards[1]
        coluna3 = self.cards[2]

        novo_posicionamento = [[],
                               [],
                               []]
        index_coluna = 0

        if no_centro == 1:
            ordem_distribuicao = [coluna2, coluna1, coluna3]
        if no_centro == 2:
            ordem_distribuicao = [coluna1, coluna2, coluna3]
        if no_centro == 3:
            ordem_distribuicao = [coluna2, coluna3, coluna1]

        for coluna in ordem_distribuicao:
            for carta in coluna:
                carta.pos[0] = index_coluna
                carta.pos[1] = len(novo_posicionamento[index_coluna])

                novo_posicionamento[index_coluna].append(carta)

                if index_coluna < 2:
                    index_coluna += 1
                else:
                    index_coluna = 0

        self.cards = novo_posicionamento

    def run(self):
        self.draw()

    def draw(self):
        for line in self.cards:
            for card_item in line:
                card_item.draw((100, 40))

    def get_card(self):
        return self.cards[1][3].type


board = Board()
