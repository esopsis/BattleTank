import pygame, sys
from pygame.locals import *
pygame.init()

WIDTH = 500
HEIGHT = 400

# set up the window
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FPS = 30
clock = pygame.time.Clock()

def draw():
    windowSurface.fill(WHITE)
    #Code here
    pygame.draw.circle(windowSurface, BLACK, [200, 200], 100)
    pygame.display.flip()

def update():
    #Code here
    clock.tick(FPS)

windowSurface.fill(WHITE)

while(True):
    draw()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    update()
