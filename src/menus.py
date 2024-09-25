from niveles import *
from ventana import *
import time

# Opciones del menú
options = ["Jugar", "Salir"]
option_rects = []

# Niveles del juego
nivels = ["Nivel 1", "Nivel 2", "Nivel 3"]
nivels_rects = []

pygame.init()

# Fuente para el menu y carteles
font = pygame.font.Font(None, 74)

# Dibuja Carteles antes de iniciar los niveles
def draw_poster(cartel, tiempo = 2):
    screen.blit(background_Image, background_Rect)
    text = font.render(cartel, True, WHITE)
    text_rect = text.get_rect(center=(400, 300))
    screen.blit(text, text_rect)
    pygame.display.flip()
    time.sleep(tiempo)

# Dibuja un menú modelo
def draw_menu(cadena, rects):
    screen.blit(background_Image, background_Rect)
    rects.clear()
    mouse_pos = pygame.mouse.get_pos()
    for i, option in enumerate(cadena):
        label = font.render(option, True, WHITE)
        rect = label.get_rect(center=(400, 200 + i * 100))
        rects.append(rect)
        if rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, WHITE, rect.inflate(20, 20), 2)
        screen.blit(label, rect)
    pygame.display.flip()


# Selector de niveles
def juego():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for i, rect in enumerate(nivels_rects):
                    if rect.collidepoint(mouse_pos):
                        menu.stop()
                        if i == 0:
                            nivel1()
                        elif i == 1:
                            nivel2()
                        elif i == 2:
                            nivel3()
                    running = False
        draw_menu(nivels, nivels_rects)


# Menú principal
def main():
    running = True
    while running:
        menu.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for i, rect in enumerate(option_rects):
                    if rect.collidepoint(mouse_pos):
                        if i == 0:
                            juego()
                        elif i == 1:
                            pygame.quit()
        draw_menu(options, option_rects)

if __name__ == "__main__":
    main()