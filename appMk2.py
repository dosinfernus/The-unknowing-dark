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
        

x, y = 220, 220
p1 = pygame.image.load('Ship3.png')  #modified to centre sprite 
loop = True
while loop:
    # this adds the sprite at every frame rate
    screen.fill((0,0,0))        #prevents doubles of sprite forming, deletes images as it goes. 
    screen.blit(bgColor, [0,0]) #redraws grid every time screen is wiped. 
    screen.blit(p1,(x,y))
 
    for event in pygame.event.get():
        # this is to close the window
        if event.type==pygame.QUIT:
            loop = False
            #sys.exit() # this will close the kernel too
            # in development mode leave the comment above
    # this is the list with the keys being pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 0.1
    if keys[pygame.K_RIGHT]:
        x += 0.1
    if keys[pygame.K_UP]:
        y -= 0.1
    if keys[pygame.K_DOWN]:
        y += 0.1 
    # we update the screen at every frame
    pygame.display.flip()
    # if we put the frame rate at 60 the sprite will move slower
    clock.tick(120)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick( FRAMERATE )
    screen.blit(bgColor, [0,0])
    p1.update()
    p1.show()
    pygame.display.update()
