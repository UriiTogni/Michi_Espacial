import pygame

pygame.mixer.init()

# Guardar los sonidos 
reloj = pygame.mixer.Sound("./sound/reloj.mp3")
comio = pygame.mixer.Sound("./sound/comio.mp3")
victoria = pygame.mixer.Sound("./sound/victoria.mp3")
perdio = pygame.mixer.Sound("./sound/perdio.mp3")
final = pygame.mixer.Sound("./sound/final.mp3")
menu = pygame.mixer.Sound("./sound/menu.mp3")
level1 = pygame.mixer.Sound("./sound/level1.mp3")
level2 = pygame.mixer.Sound("./sound/nivel2.mp3")

# Modificar el volumen
level1.set_volume(0.4)
level2.set_volume(0.4)
menu.set_volume(0.1)
reloj.set_volume(0.2)
final.set_volume(0.8)
comio.set_volume(1)