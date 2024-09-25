import pygame

pygame.mixer.init()

# Guardar los sonidos 
reloj = pygame.mixer.Sound("Michi_Espacial/sound/reloj.mp3")
comio = pygame.mixer.Sound("Michi_Espacial/sound/comio.mp3")
victoria = pygame.mixer.Sound("Michi_Espacial/sound/victoria.mp3")
perdio = pygame.mixer.Sound("Michi_Espacial/sound/perdio.mp3")
final = pygame.mixer.Sound("Michi_Espacial/sound/final.mp3")
inicio = pygame.mixer.Sound("Michi_Espacial/sound/menu.mp3")
level1 = pygame.mixer.Sound("Michi_Espacial/sound/level1.mp3")
level2 = pygame.mixer.Sound("Michi_Espacial/sound/nivel2.mp3")

# Modificar el volumen
level1.set_volume(0.4)
level2.set_volume(0.4)
inicio.set_volume(0.1)
reloj.set_volume(0.2)
final.set_volume(0.8)
comio.set_volume(1)