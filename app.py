import pygame, random

pygame.init()
pygame.display.set_caption('Sub!')
WIDTH = 601
HEIGHT = 601
BORDER = 20
FRAMERATE = 120
bgColor = pygame.transform.smoothscale(pygame.image.load("grid.png"), (600,600))
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.blit(bgColor, (0,0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick( FRAMERATE )
    pygame.display.flip()