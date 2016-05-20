import pygame
import simulator
import constants

#Setting up pygame

displayWidth = 1200
displayHeight = 700

particleNumber = 50

clock = pygame.time.Clock()

simulationDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("PyBody Simulation")
pygame.display.update()

simulationExit = False

#Simulation loop

#Initial conditions

simulator.generateParticles(particleNumber,"")

while not simulationExit:
    for event in pygame.event.get():

        #Handling quit events

        if event.type == pygame.QUIT:

            simulationExit = True

    simulationDisplay.fill(constants.black)

    #Update particle positions
    simulator.updatePositions(simulator.particleList,"")

    #Draw particles
    for particle in simulator.particleList:
        x = int(particle.px)
        y = int(particle.py)

        pygame.draw.circle(simulationDisplay,constants.white,(x,y),1,1)

    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()
