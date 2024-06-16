import pygame
from constants import screen
from activitys.game.board import board

pygame.font.init()

title_font = pygame.font.Font(None, 70)
title_color = (255, 255, 255)

class Button:
    def __init__(self, pos, size, text, key, color, font_size=60):
        self.rect = pygame.Rect((pos[0], pos[1], size[0], size[1]))
        self.text = text
        self.key = key
        self.color = color
        self.pos = pos
        self.size = size
        self.text_color = (255, 255, 255)
        self.text_pos = [0, 0]
        self.font = pygame.font.Font(None, font_size)
        self.render = self.font.render(self.text, True, self.text_color)
        self.update_text(self.text)

    def draw(self):
        # Sombra
        pygame.draw.rect(screen, (0, 10, 0), (self.pos[0] + 5, self.pos[1] + 5, self.size[0], self.size[1]))
        # Botão
        pygame.draw.rect(screen, self.color, self.rect)
        # Texto
        screen.blit(self.render, self.text_pos)

    def update_text(self, text):
        self.text = text
        self.render = self.font.render(self.text, True, self.text_color)
        self.text_pos = [(self.pos[0] + (self.size[0] / 2)) - (self.render.get_size()[0] / 2),
                         self.pos[1] + (self.size[1] / 2) - (self.render.get_size()[1] / 2)]

    def click(self, pos):
        # Obter as dimensões atuais da tela do jogo e da janela real
        game_width, game_height = screen.get_size()
        window_width, window_height = pygame.display.get_window_size()

        # Calcular os fatores de escala
        scale_x = game_width / window_width
        scale_y = game_height / window_height

        # Ajustar a posição do clique do mouse
        true_pos = (pos[0] * scale_x, pos[1] * scale_y)
        return self.rect.collidepoint(true_pos)

class GUI:
    def __init__(self):
        self.title = None
        self.title_pos = [0, 0]
        self.buttons = [Button((1330, 480), (300, 80), 'Ok, já pensei.', 'action1', (35, 150, 35)),
                        Button((1330, 580), (300, 80), 'Fila 2', 'action2', (35, 150, 35)),
                        Button((1330, 680), (300, 80), 'Fila 3', 'action3', (35, 150, 35))]

        self.step = 1
        self.set_title('PENSE EM UMA CARTA...')

    def sets(self):
        self.title = None
        self.title_pos = [0, 0]
        self.buttons = [Button((1330, 480), (300, 80), 'Ok, já pensei.', 'action1', (35, 150, 35)),
                        Button((1330, 580), (300, 80), 'Fila 2', 'action2', (35, 150, 35)),
                        Button((1330, 680), (300, 80), 'Fila 3', 'action3', (35, 150, 35))]

        self.step = 1
        self.set_title('PENSE EM UMA CARTA...')

    def set_title(self, content):
        self.title = title_font.render(content, True, title_color)
        pos = [1480, 400]
        self.title_pos = [pos[0] - (self.title.get_size()[0] / 2), pos[1] - (self.title.get_size()[1] / 2)]

    def run(self):
        self.draw()

    def draw(self):
        if self.step == 1:
            self.draw_step1()
        if self.step == 2:
            self.draw_step2()
        if self.step == 3:
            self.draw_step3()
        if self.step == 4:
            self.draw_step4()
        if self.step == 5:
            self.draw_step5()
        if self.step == 6:
            self.draw_step6()

    def draw_step1(self):
        screen.blit(self.title, self.title_pos)
        self.buttons[0].draw()

    def draw_step2(self):
        screen.blit(self.title, self.title_pos)
        for button in self.buttons:
            button.draw()

    def draw_step3(self):
        screen.blit(self.title, self.title_pos)
        for button in self.buttons:
            button.draw()

    def draw_step4(self):
        screen.blit(self.title, self.title_pos)
        for button in self.buttons:
            button.draw()

    def draw_step5(self):
        screen.blit(self.title, self.title_pos)
        self.buttons[0].draw()

    def draw_step6(self):
        from activitys.game.card import cards_images
        screen.blit(self.title, self.title_pos)
        screen.blit(cards_images[board.get_card()], (1370, 340))
        self.buttons[2].draw()

    def click(self, pos):
        for button in self.buttons:
            if button.click(pos):

                # Ir para Step 2
                if self.step == 1:
                    if button.key == 'action1':
                        self.set_title('Em qual fila ela está?')
                        self.buttons[0].update_text('Fila 1')
                        self.step = 2
                        break

                # Ir para Step 3
                if self.step == 2:
                    self.set_title('E agora?')
                    if button.key == 'action1':
                        board.distribute(1)
                    if button.key == 'action2':
                        board.distribute(2)
                    if button.key == 'action3':
                        board.distribute(3)
                    self.step = 3
                    break

                # Ir para Step 4
                if self.step == 3:
                    self.set_title('E dessa vez?')

                    if button.key == 'action1':
                        board.distribute(1)
                    if button.key == 'action2':
                        board.distribute(2)
                    if button.key == 'action3':
                        board.distribute(3)

                    self.step = 4
                    break

                # Ir para Step 5
                if self.step == 4:
                    self.set_title('Já sei qual é ;)')
                    self.buttons[0].update_text('Qual então?')

                    if button.key == 'action1':
                        board.distribute(1)
                    if button.key == 'action2':
                        board.distribute(2)
                    if button.key == 'action3':
                        board.distribute(3)

                    self.step = 5
                    break

                # Ir para o Step 6
                if self.step == 5:
                    self.set_title('Essa...')
                    self.title_pos[1] -= 120
                    self.buttons[2].update_text('Outra vez...')

                    if button.key == 'action1':
                        print('Vou te mostrar...')

                    self.step = 6
                    break

                if self.step == 6:
                    if button.key == 'action3':
                        board.put_cards()
                        self.sets()
