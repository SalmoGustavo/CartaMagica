import pygame
from activitys.game import gameActivity
from constants import display, screen, clock

game = gameActivity.Game()

class App:
    def __init__(self):
        self.running = True

    def run(self):
        while self.running:
            self.readEvents()  # Lê eventos de Entrada
            game.run()  # Executa a Classe do Jogo

            # Configurando Tela
            display.blit(pygame.transform.scale(screen, display.get_size()), (0, 0))
            pygame.display.update()
            clock.tick(60)

    @staticmethod
    def readEvents():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
            if event.type == pygame.VIDEORESIZE:
                # Mantendo Proporção de 16:9
                display = pygame.display.set_mode((event.size[0], event.size[0] / 1.77), pygame.RESIZABLE)
            if event.type == pygame.MOUSEBUTTONDOWN:
                game.click(event.pos)


app = App()

if __name__ == '__main__':
    app.run()
