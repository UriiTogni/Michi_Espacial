import pygame

# Configuración de la pantalla y fondo
FPS = 60
WIDTH = 800
HEIGTH = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("Michi espacial")
background_Image = pygame.image.load("Michi_Espacial/images/Nebula.png").convert()
background_Rect = background_Image.get_rect()