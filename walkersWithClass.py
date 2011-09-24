##
# An example of object oriented programming. This script defines a Walker, which is an colored square which walks around a pygame screen changing colors. 
# IMPORTANT: You probably need a local install of pygame for this to work correctly
# -Zack Maril, 2011
##


#Import pygame, which handles the graphics, and random, which handles generating the random numbers (6!). 
import pygame
import random

#Defines the class Walker. The class is nothing more than a wrapper 
class Walker():
    #The __init__ method is called by python to set everything up for the class. Self is always passed in.
    # I pass in sizes, the variable which holds the screen size, size, which sets up how large the Walker should be, and 
    # pSig, which is short for pathSigma, a measure of how much the walker deviates each time it is asked to change
    def __init__(self,sizes,size,pSig,cSig):
        ##Random starting position
        self.pos = (random.randint(0,sizes[0]),random.randint(0,sizes[1]))
        
        ## This is what is used to determine how large the thing actually is. 
        self.footprint = (size,size)
        #Random starting color 
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

        #How much the color deviates 
        self.colorSigma = cSig

        #How much the path deviates
        self.pathSigma = pSig

    #This is used to increment through the color space safely. If you put in x<0 or x>255 for part of a color tuple, pygame hates you. 
    def nextColor(self,n):
        deviate = random.randint(-self.colorSigma,self.colorSigma)
        n += deviate
        if n<=0:n=0
        if n>=255:n=255
        return n

    # draw allows a Walker to draw itself onto the screen.
    def draw(self,screen):
        screen.fill(self.color,(self.pos[0],self.pos[1],self.footprint[0],self.footprint[1]))
        pygame.display.flip()
    
    # updatePos finds the next values for where the Walker should be based on pathSigma
    def updatePos(self):
        x,y= self.pos
        x += random.randint(-self.pathSigma,self.pathSigma)
        y += random.randint(-self.pathSigma,self.pathSigma)
        if x<0: x = 0
        if x>sizes[0]: x = sizes[0]
        if y<0: y = 0
        if y>sizes[1]: y = sizes[1]
        self.pos = (x,y)

    # nextMove takes the screen and gets the walker to draw itself on that sucker.
    def nextMove(self,screen):
        self.updatePos()
        self.draw(screen)
        self.color = map(self.nextColor,self.color)


# Size of the screen.
sizes = 500,500

# Set up the screen from the pygame module and save it for later
screen= pygame.display.set_mode(sizes)

# Used for the while loop
running =1 

# List comprehension to create some walkers. They are of varying sizes to show that you can create different walkers that still do the same basic thing.
walkers = [Walker(sizes,i,50-i,50-i) for i in range(1,50,10)]


# while loop to keep things going
while running:
    # Capture the events from pygame
    event =pygame.event.poll()

    #Stop the loop if one the events is a QUIT action
    if event.type == pygame.QUIT:
        running = 0

    #Go through all the walkers and move those bad boys 
    for w in walkers:    
        w.nextMove(screen)


    
            
