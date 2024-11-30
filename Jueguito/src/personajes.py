from ventana import screen, pygame
# Aca estan las tres clases de personajes

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("./images/t3.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocity = 5
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.x < 1150:
            self.rect.x += self.velocity
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN] and self.rect.y < 550:
            self.rect.y += self.velocity
    def invertido(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.x > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_LEFT] and self.rect.x < 1150:
            self.rect.x += self.velocity
        if keys[pygame.K_DOWN] and self.rect.y > 0:
            self.rect.y -= self.velocity
        if keys[pygame.K_UP] and self.rect.y < 550:
            self.rect.y += self.velocity

class Enemy:
    def __init__(self, x, y, velocidad_x = 2, velocidad_y = 2, visible = True):
        self.image = pygame.image.load("./images/image3.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocityX = velocidad_x
        self.velocityY = velocidad_y
        self.visible = visible
    def draw(self):
        if self.visible:
            screen.blit(self.image, (self.rect.x, self.rect.y))
        else:
            ghost = pygame.image.load("./images/image3 - ghost.png").convert_alpha()
            screen.blit(ghost, (self.rect.x, self.rect.y))
    def updateX(self):
        self.rect.x += self.velocityX
        if self.rect.left < 0 or self.rect.right > 1200:
            self.velocityX = -self.velocityX
    def updateY(self):
        self.rect.y += self.velocityY
        if self.rect.top < 0 or self.rect.bottom > 600:
            self.velocityY = -self.velocityY
    def update(self):
        Enemy.updateY(self)
        Enemy.updateX(self)

class Atun:
    def __init__(self, x, y, velocidad_x = 3, velocidad_y = 4, visible = True):
        self.image = pygame.image.load("./images/atun1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.velocityX = velocidad_x
        self.velocityY = velocidad_y
        self.visible = visible
        self.rect.topleft = (x, y)
    def draw(self):
        if self.visible:
            screen.blit(self.image, (self.rect.x, self.rect.y))
        else:
            ghost = pygame.image.load("./images/ghost.png").convert_alpha()
            screen.blit(ghost, (self.rect.x, self.rect.y))
            Atun.update(self)
    def encontrado(self):
        if self.visible:
            self.rect.topleft = (-100, -100)
    def updateX(self):
        self.rect.x += self.velocityX
        if self.rect.left < 0 or self.rect.right > 1200:
            self.velocityX = -self.velocityX
    def updateY(self):
        self.rect.y += self.velocityY
        if self.rect.top < 0 or self.rect.bottom > 600:
            self.velocityY = -self.velocityY
    def update(self):
        Atun.updateY(self)
        Atun.updateX(self)
