import pygame
import sys

screen= pygame.display.set_mode((640,400))
running =1 
coords = [6,6,6]
updowns = [1,1,1]
primes = [2,3,5]
while running:
    event =pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    pos = pygame.mouse.get_pos()
    pygame.display.flip()


