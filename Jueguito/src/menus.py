from niveles import *
from ventana import *
import time

# Opciones del menú
options = ["Jugar", "Salir"]
option_rects = []

# Salida al menú
menuOp = ["Salir"]
menuOp_rects = []

# Niveles del juego
nivels = ["Nivel 1", "Nivel 2", "Nivel 3", "Nivel 4", "Nivel 5", "Nivel 6", "Nivel 7", "Nivel 8"]
nivels_rects = []

pygame.init()

# Fuente para el menu y carteles
font = pygame.font.Font(None, 74)

# Dibuja Carteles antes de iniciar los niveles
def draw_poster(cartel, tiempo = 2):
    screen.blit(background_Image, background_Rect)
    text = font.render(cartel, True, WHITE)
    text_rect = text.get_rect(center=(600, 300))
    screen.blit(text, text_rect)
    pygame.display.flip()
    time.sleep(tiempo)

def draw_niveles(cadena, rects, Jugado):
    screen.blit(background_Image, background_Rect)
    rects.clear()
    mouse_pos = pygame.mouse.get_pos()
    offset_y = 110  # Ajuste vertical para subir las columnas
    color = WHITE
    for i, option in enumerate(cadena):
        label = font.render(option, True, color)
        x = 400 if i % 2 == 0 else 800  # Alternar entre las dos columnas
        y = offset_y + (i // 2) * 100  # Incrementar la posición vertical
        rect = label.get_rect(center=(x, y))
        rects.append(rect)
        if rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, color, rect.inflate(20, 20), 3)
        screen.blit(label, rect)
        if(Jugado[i] > 0):
            color = WHITE
        else:
            color = GREY

    # Agregar botón para volver al menú
    menu_label = font.render("Volver", True, WHITE)
    menu_rect = menu_label.get_rect(center=(600, 550))  # Posición del botón
    rects.append(menu_rect)
    if menu_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, WHITE, menu_rect.inflate(20, 20), 2)
    screen.blit(menu_label, menu_rect)
    pygame.display.flip()



# Dibuja un menú modelo
def draw_menu(cadena, rects):
    screen.blit(background_Image, background_Rect)
    rects.clear()
    mouse_pos = pygame.mouse.get_pos()
    for i, option in enumerate(cadena):
        label = font.render(option, True, WHITE)
        rect = label.get_rect(center=(600, 200 + i * 100))
        rects.append(rect)
        if rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, WHITE, rect.inflate(20, 20), 2)
        screen.blit(label, rect)
    pygame.display.flip()

def validacion(ganado, jugo):
    if ganado and jugo >= 0:
        jugo += 1
    return jugo

# Selector de niveles
def juego(Ganado, Jugado):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for i, rect in enumerate(nivels_rects):
                    
                    if rect.collidepoint(mouse_pos):
                        if i == 0:
                            menu.stop()
                            Ganado[i] = nivel1()
                            Jugado[i] = validacion(Ganado[i], Jugado[i])
                            menu.play(-1)

                        elif i == 1 and Jugado[0] > 0:
                            menu.stop()
                            Ganado[i] = nivel2()
                            Jugado[i] = validacion(Ganado[i], Jugado[i])
                            menu.play(-1)

                        elif i == 2 and Jugado[1] > 0:
                            menu.stop()
                            Ganado[i] = nivel3()
                            Jugado[i] = validacion(Ganado[i], Jugado[i])
                            menu.play(-1)
                            
                        elif i == 3 and Jugado[2] > 0:
                            menu.stop()
                            Ganado[i] = nivel4()
                            Jugado[i] = validacion(Ganado[i], Jugado[i])
                            menu.play(-1)
                            
                        elif i == 4 and Jugado[3] > 0: 
                            menu.stop()
                            Ganado[i] = nivel5()
                            Jugado[i] = validacion(Ganado[i], Jugado[i])
                            menu.play(-1)
                            
                        elif i == 5 and Jugado[4] > 0:
                            menu.stop()
                            Ganado[i] = nivel6()
                            Jugado[i] = validacion(Ganado[i], Jugado[i])
                            menu.play(-1)
                            
                        elif i == 6 and Jugado[5] > 0:
                            menu.stop()
                            Ganado[i] = nivel7()
                            Jugado[i] = validacion(Ganado[i], Jugado[i])
                            menu.play(-1)
                            
                        elif i == 7 and Jugado[6] > 0:
                            menu.stop()
                            Ganado[i] = nivel8()
                            Jugado[i] = validacion(Ganado[i], Jugado[i])
                            menu.play(-1)
                            
                        elif i == 8:
                            running = False
        draw_niveles(nivels, nivels_rects, Jugado)


# Menú principal
def main():
    running = True
    menu.play()
    Ganado = [False, False, False, False, False, False, False, False]
    Jugado = [0, 0, 0, 0, 0, 0, 0, 0]
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for i, rect in enumerate(option_rects):
                    if rect.collidepoint(mouse_pos):
                        if i == 0:
                            juego(Ganado, Jugado)
                        elif i == 1:
                            pygame.quit()
        draw_menu(options, option_rects)

if __name__ == "__main__":
    main()