import pygame
import Universe

#Setting up pygame

displayWidth = 700
displayHeight = 400

particlenumber = 100

clock = pygame.time.Clock()

simulationDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("PyBody Simulation")
pygame.display.update()

simulationExit = False

#Simulation loop

Universe.generateparticles(particlenumber)

while not simulationExit:
    for event in pygame.event.get():

        #Handling quit events

        if event.type == pygame.QUIT:

            simulationExit = True

    simulationDisplay.fill(Universe.black)

    #Universe.particlelist.append(Universe.sun)

    for particle in Universe.particlelist:
        for other in filter(lambda p: p != particle, Universe.particlelist):
            Universe.integrator(particle,other)
            Universe.drag(particle)
        x = int(particle.px)
        y = int(particle.py)
        
        pygame.draw.circle(simulationDisplay,Universe.white,(x,y),1,1)

    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()
