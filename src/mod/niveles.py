import menus
from sound import *
from personajes import *
from ventana import *

# Movimiento libres del Michi y los Ovnis
def nivel1():
    # Declaraciones para preparar el nivel
    level1.play(-1) # musica del nivel en loop
    player = Player(10, 10)
    atunes = [Atun(150, 250), Atun(550, 350), Atun(210, 400)]
    enemies = [Enemy(410, 150), Enemy(240, 350), Enemy(200, 400)]
    atrapado = False
    completado = False
    atunCont = 0
    OBJETIVO = 3
    runing = True
    clock = pygame.time.Clock()

    # Carteles de inicio
    menus.draw_poster("Muevete con las flechas")
    menus.draw_poster("Come atún y evita los aliens")

    # Comienzo del nivel
    while runing == True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False

        screen.blit(background_Image, background_Rect)
        player.draw()
        player.update()

        for atun in atunes:
            atun.draw()
            if player.rect.colliderect(atun.rect):
                atun.encontrado() 
                comio.play()
                atunCont += 1
            if atunCont == OBJETIVO:
                runing = False
                completado = True

        for enemy in enemies:
            enemy.draw()
            enemies[0].updateY()
            enemies[1].update()
            enemies[2].updateX()
            if player.rect.colliderect(enemy.rect):
                runing = False
                atrapado = True
            
        pygame.display.flip()
    
    # Resultado Final
    level1.stop()
    if completado:
        victoria.play()
        menus.draw_poster("Ganaste!!")
    elif atrapado:
        perdio.play()
        menus.draw_poster("Perdiste :(")
    return completado


# Michi y Ovnis moviendose por turnos
def nivel2():
    # Preparando el nivel
    level2.play(-1)
    player = Player(10, 10)
    atunes = [Atun(150, 250), Atun(350, 50), Atun(210, 400), Atun(550, 230), Atun(450, 400)]
    enemies = [Enemy(240, 140, 5, 5), Enemy(300, 40, 6, 0), Enemy(450, 300, 4, 6), Enemy(40, 450, 0, 3)]
    completado = False
    OBJETIVO = 5
    atunCont = 0
    runing = True
    clock = pygame.time.Clock()
    # Variables para hacer por turnos de 2,5 segundos
    waiting = False
    wait_start_time = 0
    wait_duration = 2500    # 2,5 segundos
    next_pause_time = 2500  # 2,5 segundos

    # Cartel de inicio
    menus.draw_poster("Espera y Muevete")

    # Empieza el nivel
    while runing == True:
        clock.tick(FPS)
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False

        screen.blit(background_Image, background_Rect)
        player.draw()

    # Calcular tiempo
        if not waiting and current_time >= next_pause_time:
            waiting = True
            wait_start_time = current_time
            next_pause_time = current_time + wait_duration + 2500

    # Verificar si han pasado los segundos de pausa
        if waiting and current_time - wait_start_time >= wait_duration:
            waiting = False
    
    # Seguir
        if not waiting:
            reloj.stop()
            player.update()
    # Congelado
        if waiting: 
            reloj.play()
            enemies[0].update()
            enemies[1].updateX()
            enemies[2].update()
            enemies[3].updateY()

        for atun in atunes:
            atun.draw()
            if player.rect.colliderect(atun.rect):
                atun.encontrado()
                comio.play()
                atunCont += 1 
        if atunCont == OBJETIVO:    
            runing = False
            completado = True

        for enemy in enemies:
            enemy.draw()
            if player.rect.colliderect(enemy.rect):
                runing = False
                atrapado = True
            
        pygame.display.flip()

    # Resultado Final
    reloj.stop()
    level2.stop()
    if completado:
        victoria.play()
        menus.draw_poster("Ganaste!!")
    elif atrapado:
        perdio.play()
        menus.draw_poster("Perdiste :(")
    return completado


# Ovnis y Atuncitos moviendose por turnos
def nivel3():
    # Preparando nivel
    final.play(-1)
    player = Player(10, 10)
    atunes = [Atun(250, 250), Atun(350, 450), Atun(210, 40), Atun(10, 230), Atun(550, 100)]
    enemies = [Enemy(250, 240, 6, 6), Enemy(300, 40, 11, 0), Enemy(450, 300, 4, 7), Enemy(40, 450, 0, 10), Enemy(540, 450, 0, 10)]
    completado = False
    OBJETIVO = 5
    atunCont = 0
    waiting = False
    wait_start_time = 0
    wait_duration = 2500    # 2,5 segundos
    next_pause_time = 2500  # 2,5 segundos
    runing = True
    clock = pygame.time.Clock()

    # Cartel de inicio
    menus.draw_poster("Descontrol!!")

    # A jugar
    while runing == True:
        clock.tick(FPS)
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False

        screen.blit(background_Image, background_Rect)
        player.draw()
        player.update()

        # Congelado solo para los enemigos
        if not waiting and current_time >= next_pause_time:
            waiting = True
            wait_start_time = current_time
            next_pause_time = current_time + wait_duration + 2500

    # Verificar si han pasado los segundos de pausa
        if waiting and current_time - wait_start_time >= wait_duration:
            waiting = False
    
    # Seguir
        if not waiting:
            enemies[3].updateY()
            enemies[0].update()
            atunes[1].update()
            atunes[2].updateX()
        if waiting: 
            enemies[1].updateX()
            enemies[2].update()
            enemies[4].updateY()
            atunes[0].update()
            atunes[3].updateY()
            atunes[4].update()
        for atun in atunes:
            atun.draw()
            if player.rect.colliderect(atun.rect):
                atun.encontrado()
                comio.play()
                atunCont += 1 
        if atunCont == OBJETIVO:    
            runing = False
            completado = True

        for enemy in enemies:
            enemy.draw()
            if player.rect.colliderect(enemy.rect):
                runing = False
                atrapado = True
        pygame.display.flip()
    
    # Resultado Final
    final.stop()
    if completado:
        victoria.play()
        menus.draw_poster("Ganaste!!")
    elif atrapado:
        perdio.play()
        menus.draw_poster("Perdiste :(")
    return completado