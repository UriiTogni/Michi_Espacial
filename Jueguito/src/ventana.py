import pygame

# Configuración de la pantalla y fondo
FPS = 60
WIDTH = 1200
HEIGTH = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("Michi espacial")
background_Image = pygame.image.load("./images/Nebula.png").convert_alpha()
background_Rect = background_Image.get_rect()