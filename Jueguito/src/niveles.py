from menus import draw_poster
from sound import *
from personajes import *
from ventana import *

def resultado(completado, atrapado):
    if completado:
        victoria.play()
        draw_poster("Ganaste!!")
    elif atrapado:
        perdio.play()
        draw_poster("Perdiste :(")

def isWin(atunes, player, Cont, objetivo, runing, completado):
    for atun in atunes:
        atun.draw()
        if player.rect.colliderect(atun.rect) and atun.visible:
            atun.encontrado()
            comio.play()
            Cont += 1 
        if Cont == objetivo:    
            runing = False
            completado = True
    return Cont, runing, completado

def isLose(enemies, player, runing, atrapado):
    for enemy in enemies:
        enemy.draw()
        if player.rect.colliderect(enemy.rect) and enemy.visible:
            runing = False
            atrapado = True
    return runing, atrapado

def Time(waiting, current_time, next_pause_time, wait_start_time, wait_duration, extra):
    if not waiting and current_time >= next_pause_time:
            waiting = True
            wait_start_time = current_time
            next_pause_time = current_time + wait_duration + extra
    if waiting and current_time - wait_start_time >= wait_duration:
            waiting = False
    return waiting, current_time, next_pause_time, wait_start_time, wait_duration

def ChangeVelocity(enemies, atunes):
    for enemy in enemies:
        enemy.velocityX = randint(2, 9)
        enemy.velocityY = randint(2, 9)
    for atun in atunes:
        atun.velocityX = randint(1, 10)
        atun.velocityY = randint(1, 10)

def nivel1():
    level1.play(-1)
    player = Player(10, 10)
    atunes = [Atun(850, 250), Atun(550, 350), Atun(210, 400), Atun(410, 10)]
    enemies = [Enemy(510, 150, 0, 5), Enemy(240, 350, 4, 3), Enemy(140, 400, 6)]
    atrapado = False
    completado = False
    atunCont = 0
    OBJETIVO = 4
    runing = True
    clock = pygame.time.Clock()

    draw_poster("Muevete con las flechas")
    draw_poster("Come atún y evita los aliens")

    while runing:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False
        screen.blit(background_Image, background_Rect), player.draw(), player.update()

        enemies[0].updateY(), enemies[1].update(), enemies[2].updateX()
        
        atunCont, runing, completado = isWin(atunes, player, atunCont, OBJETIVO, runing, completado)
        runing, atrapado = isLose(enemies, player, runing, atrapado)
        pygame.display.flip()
    level1.stop()
    resultado(completado, atrapado)
    return completado



def nivel2():
    level2.play(-1)
    player = Player(10, 10)
    atunes = [Atun(150, 250), Atun(350, 50), Atun(810, 550), Atun(550, 230), Atun(1130, 80)]
    enemies = [Enemy(240, 140, 5, 6), Enemy(300, 40, 7), Enemy(1100, 200, 5, 6), Enemy(40, 450, 0, 3), Enemy(1080, 500, 8)]
    completado = False
    atrapado = False
    OBJETIVO = 5
    atunCont = 0
    runing = True
    clock = pygame.time.Clock()
    # Variables para hacer por turnos de 2,5 segundos
    turno = False
    waitStart = 0
    duration = 2500    
    nextPause = 2500  
    extra = 2500  

    draw_poster("Espera y Muevete")

    while runing == True:
        clock.tick(FPS)
        concurrido = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False

        screen.blit(background_Image, background_Rect), player.draw()
        turno, concurrido, nextPause, waitStart, duration = Time(turno, concurrido, nextPause, waitStart, duration, extra)
    
        if not turno:
            reloj.stop(), player.update()
        else: 
            reloj.play(), enemies[0].update(), enemies[1].updateX(), enemies[2].update(), enemies[3].updateY(), enemies[4].updateX()

        atunCont, runing, completado = isWin(atunes, player, atunCont, OBJETIVO, runing, completado)
        runing, atrapado = isLose(enemies, player, runing, atrapado)
        pygame.display.flip()
    reloj.stop()
    level2.stop()
    resultado(completado, atrapado)
    return completado 


def nivel3():
    level3.play(-1)
    player = Player(10, 10)
    atunes = [Atun(250, 450), Atun(300, 450,2), Atun(210, 40), Atun(10, 230, 0,2), Atun(550, 100), Atun(1140, 540,0,8)]
    enemies = [Enemy(250, 240, 6, 6), Enemy(300, 40, 11, 0), Enemy(450, 300, 4, 7), Enemy(40, 450, 0, 10), Enemy(540, 450, 0, 10)]
    completado = False
    atrapado = False
    OBJETIVO = 6
    atunCont = 0
    turno = False
    waitStart = 0
    duration = 2500     # 2,5 segundos
    nextPause = 2500    # 2,5 segundos
    extra = 2500        # 2,5 segundos
    runing = True
    clock = pygame.time.Clock()

    draw_poster("Atunes Movidizos")

    while runing == True:
        clock.tick(FPS)
        concurrido = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False

        screen.blit(background_Image, background_Rect), player.draw(), player.update()
        turno, concurrido, nextPause, waitStart, duration = Time(turno, concurrido, nextPause, waitStart, duration, extra)
    
        if not turno:
            enemies[3].updateY(), enemies[0].update()
            atunes[1].update(), atunes[2].updateX(), atunes[5].updateY()
        else: 
            enemies[1].updateX(), enemies[2].update(), enemies[4].updateY()
            atunes[0].update(), atunes[3].updateY(), atunes[4].update()

        atunCont, runing, completado = isWin(atunes, player, atunCont, OBJETIVO, runing, completado)
        runing, atrapado = isLose(enemies, player, runing, atrapado)
        pygame.display.flip()
    level3.stop()
    resultado(completado, atrapado)
    return completado

def nivel4():
    level4.play(-1)
    player = Player(10, 10)
    atunes = [Atun(150, 250, 2, 2), Atun(350, 50), Atun(210, 400, 4, 5), Atun(550, 230, 3, 3), Atun(450, 400), Atun(50, 200)]
    enemies = [Enemy(240, 140, 8, 8), Enemy(300, 40, 8, 8), Enemy(450, 300, 8, 8), Enemy(40, 450, 8, 8)]
    completado = False
    atrapado = False
    OBJETIVO = 6
    atunCont = 0
    runing = True
    turno = False
    waitStart = 0
    duration = 1500     # 1,5 segundo
    nextPause = 1500    # 1,5 segundo
    extra = 1500
    clock = pygame.time.Clock()

    draw_poster("Atunes Fantasmas")

    while runing == True:
        clock.tick(FPS)
        concurrido = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False

        screen.blit(background_Image, background_Rect), player.draw(), player.update()
        turno, concurrido, nextPause, waitStart, duration = Time(turno, concurrido, nextPause, waitStart, duration, extra)

        if not turno:
            enemies[3].update(), enemies[0].update()
            atunes[0].visible = False
            atunes[1].visible = False
            atunes[4].visible = False
            atunes[2].visible = True
            atunes[3].visible = True
            atunes[5].visible = True
        else: 
            enemies[1].update(), enemies[2].update()
            atunes[2].visible = False
            atunes[3].visible = False
            atunes[5].visible = False
            atunes[0].visible = True
            atunes[1].visible = True
            atunes[4].visible = True

        atunCont, runing, completado = isWin(atunes, player, atunCont, OBJETIVO, runing, completado)
        runing, atrapado = isLose(enemies, player, runing, atrapado)
        pygame.display.flip()
    level4.stop()
    resultado(completado, atrapado)
    return completado

def nivel5():
    player = Player(10, 10)
    enemies = [Enemy(240, 140, 5, 10), Enemy(240, 340, 2, 6), Enemy(300, 200, 10, 6), Enemy(300, 10, 4)] 
    atunes = [Atun(1050, 50), Atun(210, 50, 0,0, False), Atun(850, 500, 0,0, False), Atun(600, 240), Atun(150, 480)]
    completado = False
    atrapado = False
    OBJETIVO = 5
    atunCont = 0
    runing = True
    waitStart = 0
    duration = randint(1000, 2000)      # entre 1 segundo a 2 segundos
    nextPause = randint(1000, 1200)     # entre 1 segundo a 1,2 segundos
    extra = randint(1400, 2000)         # entre 1,4 segundo a 2 segundos
    turno = True
    segundaFase = False
    clock = pygame.time.Clock()

    draw_poster("Nunca pares")
    level5.play(-1)

    while runing == True:
        clock.tick(FPS)
        concurrido = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False

        screen.blit(background_Image, background_Rect), player.draw(), player.update()
        turno, concurrido, nextPause, waitStart, duration = Time(turno, concurrido, nextPause, waitStart, duration, extra)

        if turno:
            enemies[0].update(), enemies[1].updateY()
            enemies[2].updateX(), enemies[3].updateX()
        else:
            enemies[0].updateX(), enemies[1].updateX()
            enemies[2].update(), enemies[3].updateY()
        
        if atunCont == 2:
            atunes[1].visible = True
            atunes[2].visible = True

        if not segundaFase and atunCont == 3:
            segundaFase = True
            duration = randint(800, 1000)    
            nextPause = randint(1000, 1100)
            extra = randint(1000, 1100)
            enemies[3].velocityX = 7
            enemies[1].velocityX = 5
        
        atunCont, runing, completado = isWin(atunes, player, atunCont, OBJETIVO, runing, completado)
        runing, atrapado = isLose(enemies, player, runing, atrapado)
        pygame.display.flip()
    level5.stop()
    resultado(completado, atrapado)
    return completado

def nivel6():
    player = Player(10, 10)
    atunes = [Atun(200, 10), Atun(850, 50), Atun(210, 400, 1, 5), Atun(550, 230, 3, 4), Atun(450, 400), Atun(50, 200)]
    enemies = [Enemy(240, 340, 6), Enemy(860, 340, 1, 8), Enemy(450, 300, 2, 5), Enemy(40, 450, 2, 4), Enemy(40, 450, 5, 8)]
    completado = False
    atrapado = False
    OBJETIVO = 6
    atunCont = 0
    runing = True
    primeraFase = True
    segundaFase = False
    cambio = False
    clock = pygame.time.Clock()

    atunes[2].visible = False
    atunes[3].visible = False
    atunes[5].visible = False

    level6.play(-1)
    draw_poster("Controles invertidos")

    while runing:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False

        screen.blit(background_Image, background_Rect), player.draw(), player.invertido()

        if primeraFase:
            enemies[0].updateX(), enemies[1].updateY()
            enemies[2].updateY(), enemies[3].updateY()
            enemies[4].update()
            if cambio:
                fase2.stop(), level6.play(-1)
                cambio = False
        elif segundaFase:
            enemies[0].updateY(), enemies[1].updateX()
            enemies[2].updateX(), enemies[3].updateX()
            if not cambio:
                level6.stop(), fase2.play(-1)
                cambio = True

        if atunCont == 3:
            primeraFase = False
            segundaFase = True
            player.velocity = 2.7
            atunes[2].visible = True
            atunes[3].visible = True
        elif atunCont == 5:
            player.velocity = 5
            atunes[5].visible = True
            segundaFase = False
            primeraFase = True


        atunCont, runing, completado = isWin(atunes, player, atunCont, OBJETIVO, runing, completado)
        runing, atrapado = isLose(enemies, player, runing, atrapado)
        pygame.display.flip()
    level6.stop(), fase2.stop()
    resultado(completado, atrapado)
    return completado

def nivel7():
    player = Player(10, 10)
    atunes = [Atun(150, 250), Atun(750, 50), Atun(210, 400), Atun(1050, 230), Atun(450, 400), Atun(50, 200)]
    enemies = [Enemy(940, 340), Enemy(300, 40), Enemy(450, 300), Enemy(840, 450), Enemy(40, 450)]
    completado = False
    atrapado = False
    OBJETIVO = 6
    atunCont = 0
    runing = True
    PrimeraFase = True
    SegundaFase = False
    cambio = False
    cambio2 = False
    clock = pygame.time.Clock()

    level7.play(-1)
    draw_poster("Cambios de Velocidad")

    while runing:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False

        screen.blit(background_Image, background_Rect), player.draw(), player.update()

        if atunCont >= 1:
            if atunCont % 2 and cambio == False:
                ##sonidito.play()
                ChangeVelocity(enemies, atunes)
                PrimeraFase = False
                SegundaFase = True
                cambio = True
                cambio2 = False
            elif not atunCont % 2 and cambio2 == False:
                player.velocity = randint(1, 10)
                PrimeraFase = True
                SegundaFase = False
                cambio = False
                cambio2 = True
        
        if PrimeraFase:
            enemies[0].update(), enemies[4].update(),
            enemies[1].updateX(), enemies[3].updateX(), enemies[2].updateY()
            atunes[0].updateX(), atunes[2].updateY(), atunes[5].update()
        if SegundaFase:
            enemies[1].update(), enemies[3].update(),
            enemies[0].updateY(), enemies[4].updateY(), enemies[2].updateX()
            atunes[1].update(), atunes[3].updateX(), atunes[4].update()

        atunCont, runing, completado = isWin(atunes, player, atunCont, OBJETIVO, runing, completado)
        runing, atrapado = isLose(enemies, player, runing, atrapado)
        pygame.display.flip()
    
    level7.stop()
    resultado(completado, atrapado)
    return completado

def nivel8():
    player = Player(10, 10)
    atunes = [Atun(10, 450), Atun(350, 150), Atun(210, 400), Atun(550, 230), Atun(650, 420), Atun(850, 200)]
    enemies = [Enemy(240, 340,6,7), Enemy(300, 40,7,6), Enemy(450, 300,1,8), Enemy(40, 450,5,8), Enemy(40, 450,8,2), Enemy(40, 450,7,7)]
    completado = False
    atrapado = False
    OBJETIVO = 6
    atunCont = 0
    runing = True
    clock = pygame.time.Clock()
    turno = False
    waitStart = 0
    duration = randint(500, 2000)    
    nextPause = randint(500, 2000)  
    extra = randint(500, 2000)  
    fantasma = randint(0, 5)
    atunes[fantasma].visible = False
    atunes[fantasma].velocityX = 5
    atunes[fantasma].velocityY = 8

    level8.play(-1)
    draw_poster("Nivel final")

    while runing == True:
        clock.tick(FPS)
        concurrido = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False

        screen.blit(background_Image, background_Rect), player.draw()
        turno, concurrido, nextPause, waitStart, duration = Time(turno, concurrido, nextPause, waitStart, duration, extra)
    
        if turno:
            enemies[0].visible = True
            enemies[1].visible = True
            enemies[2].visible = True
            enemies[3].visible = False
            enemies[4].visible = False
            enemies[5].visible = False
            player.velocity = 4
        else:
            enemies[0].visible = False
            enemies[1].visible = False
            enemies[2].visible = False
            enemies[3].visible = True
            enemies[4].visible = True
            enemies[5].visible = True
            player.velocity = 8

        if atunCont < 2:
            player.update()
            enemies[0].update(), enemies[1].update(), enemies[2].updateX() 
            enemies[3].updateX(), enemies[4].updateY(), enemies[5].updateY()
        elif atunCont >= 2 and atunCont < 4:
            player.invertido()
            enemies[0].updateX(), enemies[1].updateX(), enemies[2].updateY() 
            enemies[3].updateY(), enemies[4].update(), enemies[5].update()
        else:            
            player.update()
            atunes[fantasma].visible = True
            enemies[0].updateY(), enemies[1].updateY(), enemies[2].update() 
            enemies[3].update(), enemies[4].updateX(), enemies[5].updateX()
            
        atunCont, runing, completado = isWin(atunes, player, atunCont, OBJETIVO, runing, completado)
        runing, atrapado = isLose(enemies, player, runing, atrapado)
        pygame.display.flip()
    
    level8.stop()
    resultado(completado, atrapado)
    return completado