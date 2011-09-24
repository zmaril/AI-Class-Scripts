import pygame

sizes = 500,250
screen= pygame.display.set_mode(sizes)
running =1 
white= 0,0,0
black= 255,255,255
pointsize = 2

for x in range(sizes[0]/pointsize):
    bound = x/2 if x>10 else x
    #Replace rem with x for whole thing below.
    for y in range(bound):
        color = white
        if x >1 and y > 1 and x%y==0:
            color = black
        screen.fill(color,map(lambda x: pointsize*x,(x,y,(x+pointsize),(y+pointsize))))
        pygame.display.flip()

while running:
    event =pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
            
    

