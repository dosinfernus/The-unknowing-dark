import pygame, random
import pandas as pd

pygame.init()
pygame.display.set_caption('Sub!')
WIDTH = 600
HEIGHT = 600
BORDER = 20
bgColor = pygame.Color("black")
fgColor = pygame.Color("blue")

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,0,WIDTH-BORDER,BORDER))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,0,BORDER,HEIGHT))
pygame.draw.rect(screen, fgColor, pygame.Rect(0,HEIGHT-BORDER,WIDTH-BORDER,BORDER))