import pygame
import random

sizes = 500,250
screen= pygame.display.set_mode(sizes)
mouse = pygame.mouse
running =1 
black= 0,0,0
white = 255,255,255
pointsize = 2
color = 125,125,125

screen.fill(black,(0,0,20,20))
pygame.display.flip()

def nextColor(n):
    deviate = random.randint(-6,6)
    n += deviate
    if n<=0:
        n=0
    if n>=255:
        n=255
    return n

while running:
    print color
    event =pygame.event.poll()
    pos = mouse.get_pos()
    screen.fill(color,(pos[0],pos[1],10,10))
    pygame.display.flip()
    if event.type == pygame.QUIT:
        running = 0
    
    color = map(nextColor,color)
    
            
