import math
import random
import timeit
import pygame

#set start screen
#lump everything under removeParticle function (escape velocity, distances limit)
#Integrator

black = (0,0,0)
white = (255,255,255)

#Setting up PyGame

start = timeit.default_timer()

totaltime = 0

displayWidth = 1200
displayHeight = 700

clock = pygame.time.Clock()

simulationDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("PyBody Simulation")
pygame.display.update()

simulationExit = False

#Simulation loop

while not simulationExit:
    for event in pygame.event.get():

        #Handling quit events

        if event.type == pygame.QUIT:

            simulationExit = True

    simulationDisplay.fill(white)

    pygame.display.update()

pygame.quit()
quit()
