import pygame
import platform
import ctypes

def set_dpi_awareness():
    if platform.system() == "Windows":
        try:
            # Windows 10 ou Superior
            ctypes.windll.shcore.SetProcessDpiAwareness(2)
        except Exception as e:
            try:
                # Windows 8.1 ou Superior
                ctypes.windll.user32.SetProcessDPIAware()
            except Exception as e:
                pass


# Configurando DPI
set_dpi_awareness()

screen = pygame.Surface((1920, 1080))
display = pygame.display.set_mode((1700, 956), pygame.RESIZABLE)
clock = pygame.time.Clock()
