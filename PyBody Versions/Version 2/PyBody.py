import math
import random
import timeit
import pygame
import Universe
import Physics
import IntegrationMethod

#Setting up pygame

start = timeit.default_timer()

totaltime = 0

displayWidth = 1200
displayHeight = 700

particlenumber = 100
centralmass = Universe.sun
moon = Universe.earth

clock = pygame.time.Clock()

simulationDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("PyBody Simulations")
pygame.display.update()

simulationExit = False

#Simulation loop

Universe.generateFieldParticles(particlenumber,displayWidth,displayHeight)
#Universe.generateMoonParticles(particlenumber)

while not simulationExit:
    for event in pygame.event.get():

        #Handling quit events

        if event.type == pygame.QUIT:

            simulationExit = True

            #Output final simulation data into a text file

            fw = open("SimulationData.txt", "w")
            fw.write("Day Number: " + str(totaltime) + "\n")
            
            for i in Universe.particlelist:
                x = str(i.px)
                y = str(i.py)
                fw.write(x + "," + y + "\n") 
            fw.close()

    simulationDisplay.fill(Universe.black)

    #Universe.particlelist.append(Universe.sun)

    for particle in Universe.particlelist:
        for other in filter(lambda p: p != particle, Universe.particlelist):
            Physics.gravity(particle,other)
            Physics.drag(particle)

        #x = int(displayWidth/2 + particle.px/Universe.AU*500)
        #y = int(displayHeight/2 + particle.py/Universe.AU*500)
        x = int(particle.px)
        y = int(particle.py)

        pygame.draw.circle(simulationDisplay,Universe.white,(x,y),1,1)

    #Add moon
    Physics.gravity(moon,centralmass)
    mx = int(displayWidth/2 + moon.px/Universe.AU*200)
    my = int(displayHeight/2 + moon.py/Universe.AU*200)
    pygame.draw.circle(simulationDisplay,Universe.green,(mx,my),2,0)
    
    for i, particle in enumerate(Universe.particlelist):

        #Removing particles that exceed escape velocity
        Universe.escapevelocity(i,particle,centralmass)

        #Remove particles that exceed distance limit
        Universe.distancelimit(i,particle)

        Physics.gravity(particle,centralmass)
        Physics.gravity(particle,moon)

        x = int(displayWidth/2 + particle.px/Universe.AU*200)
        y = int(displayHeight/2 + particle.py/Universe.AU*200)

        #Draw objects on screen

        pygame.draw.circle(simulationDisplay,Universe.white,(x,y),1,1)
        pygame.draw.circle(simulationDisplay,Universe.yellow,(displayWidth/2,displayHeight/2),5,0)
        pygame.draw.circle(simulationDisplay,Universe.green,(mx,my),2,0)

    pygame.display.update()

    totaltime += 1

    #Print the number of days passed in simulation
    print "Day: %d" %totaltime

    clock.tick(30)

print timeit.default_timer() - start, "seconds"

pygame.quit()
quit()
