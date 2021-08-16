import pygame, random
import pandas as pd
from PIL import Image

pygame.init()
pygame.display.set_caption('Sub!')
WIDTH = 600
HEIGHT = 600
BORDER = 20
FRAMERATE = 120
bgColor = Image.open("grid.png")
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH,HEIGHT))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick( FRAMERATE )
    pygame.display.flip()