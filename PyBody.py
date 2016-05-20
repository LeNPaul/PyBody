import pygame
import universe

#Setting up pygame

displayWidth = 1200
displayHeight = 700

particleNumber = 25

clock = pygame.time.Clock()

simulationDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("PyBody Simulation")
pygame.display.update()

simulationExit = False

#Simulation loop

universe.generateCloudParticles(particleNumber)

while not simulationExit:
    for event in pygame.event.get():

        #Handling quit events

        if event.type == pygame.QUIT:

            simulationExit = True

    simulationDisplay.fill(universe.black)

    for particle in universe.particleList:
        for other in filter(lambda p: p != particle, universe.particleList):
            universe.eulerIntegrator(particle,other)
        x = int(particle.px)
        y = int(particle.py)
        
        pygame.draw.circle(simulationDisplay,universe.white,(x,y),1,1)

    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()
