import pygame
import simulator
import constant
import parameter

#Setting up pygame

clock = pygame.time.Clock()

simulationDisplay = pygame.display.set_mode((parameter.displayWidth, parameter.displayHeight))
pygame.display.set_caption("PyBody Simulation")
pygame.display.update()

simulationExit = False

#Simulation loop

#Initial conditions

simulator.generateParticles(parameter.particleNumber,"")

while not simulationExit:
    for event in pygame.event.get():

        #Handling quit events

        if event.type == pygame.QUIT:

            simulationExit = True

    simulationDisplay.fill(constant.black)

    #Update particle positions
    simulator.updatePositions(simulator.particleList,"")

    #Draw particles
    for particle in simulator.particleList:
        x = int(particle.px)
        y = int(particle.py)

        pygame.draw.circle(simulationDisplay,constant.white,(x,y),1,1)

    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()
