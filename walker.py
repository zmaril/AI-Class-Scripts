import pygame
import random

sizes = 500,250
screen= pygame.display.set_mode(sizes)

running =1 
black= 0,0,0


walker = sizes[0]/2,sizes[1]/2
walkerFootprint= (5,5)
color = 125,125,125


colorSigma = 6
walkerSigma = 6

screen.fill(black,(0,0,20,20))
pygame.display.flip()

def nextColor(n):
    deviate = random.randint(-colorSigma,colorSigma)
    n += deviate
    if n<=0:
        n=0
    if n>=255:
        n=255
    return n

def moveWalker(walker):
    x,y = walker
    x += random.randint(-walkerSigma,walkerSigma)
    y += random.randint(-walkerSigma,walkerSigma)
    if x<0: x = 0
    if x>sizes[0]: x = sizes[0]
    if y<0: y = 0
    if y>sizes[1]: y = sizes[1]
    walker = (x,y)
    return walker

while running:
    event =pygame.event.poll()
    screen.fill(color,(walker[0],walker[1],walkerFootprint[0],walkerFootprint[1]))
    walker= moveWalker(walker)
    pygame.display.flip()

    if event.type == pygame.QUIT:
        running = 0
    
    color = map(nextColor,color)
    
            
