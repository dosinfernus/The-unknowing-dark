import pygame, random

pygame.init()
pygame.display.set_caption('Sub!')
WIDTH = 600
HEIGHT = 600
BORDER = 20
FRAMERATE = 120
bgColor = pygame.transform.smoothscale(pygame.image.load("grid.png"), (600,600))
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.blit(bgColor, (-1,-1))

class Player():
    def __init__(self, pImg, pX, pY, p_dX):
        self.img = pImg
        self.x = pX
        self.y = pY
        self.dx = p_dX
    def update(self):
        self.x += self.dx
        # ensure the player doesn't leave the screen
        if self.x <= 0:
            self.x = 0
        elif self.x >= 736:
            self.x = 736
    def show(self):
        global screen
        screen.blit(self.img, (self.x,self.y))

p1 = Player(pygame.image.load('Ship2.png'),140,140,0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick( FRAMERATE )
    p1.update()
    p1.show()
    pygame.display.update()