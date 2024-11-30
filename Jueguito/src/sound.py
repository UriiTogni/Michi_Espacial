import pygame
from random import randint
from ventana import *

pygame.mixer.init()

reloj = pygame.mixer.Sound("./sound/reloj.mp3")
comio = pygame.mixer.Sound("./sound/comio.mp3")
victoria = pygame.mixer.Sound("./sound/victoria.mp3")
perdio = pygame.mixer.Sound("./sound/perdio.mp3")
menu = pygame.mixer.Sound("./sound/menu.mp3")
submenu = pygame.mixer.Sound("./sound/TestLevel7_1.mp3")
level1 = pygame.mixer.Sound("./sound/level1.mp3")
level2 = pygame.mixer.Sound("./sound/nivel2.mp3")
level3 = pygame.mixer.Sound("./sound/final.mp3")
level4 = pygame.mixer.Sound("./sound/level4.mp3")
level5 = pygame.mixer.Sound("./sound/level5.mp3")
level6 = pygame.mixer.Sound("./sound/nivel6-1.mp3")
level7 = pygame.mixer.Sound("./sound/TestLevel7_2.mp3")
level8 = pygame.mixer.Sound("./sound/Level8.mp3")
fase2 = pygame.mixer.Sound("./sound/nivel6_2.mp3")
sonidito = pygame.mixer.Sound("./sound/test.mp3")

Sonido = [comio, victoria, perdio, sonidito]
Musica = [reloj, menu, level1, level2, level3, level4, level5, level6, fase2, level7, level8]

for sound in Sonido:
    sound.set_volume(0.4)
for sound in Musica:
    sound.set_volume(0.2)


