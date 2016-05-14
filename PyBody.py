import math
import random
import timeit
import pygame
import Universe

#Setting up pygame

start = timeit.default_timer()

totaltime = 0

displayWidth = 700
displayHeight = 400

particlenumber = 100
centralmass = Universe.sun

clock = pygame.time.Clock()

simulationDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Galaxy Simulation")
pygame.display.update()

simulationExit = False

#Simulation loop

Universe.generateparticles(particlenumber)

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
            Universe.integrator(particle,other)
            Universe.drag(particle)

        #x = int(displayWidth/2 + particle.px/Universe.AU*500)
        #y = int(displayHeight/2 + particle.py/Universe.AU*500)
        x = int(particle.px)
        y = int(particle.py)
        
        pygame.draw.circle(simulationDisplay,Universe.white,(x,y),1,1)

    print len(Universe.particlelist)
    pygame.display.update()

    totaltime += 1

    #Print the number of days passed in simulation
    print "Day: %d" %totaltime

    clock.tick(30)

print timeit.default_timer() - start, "seconds"

pygame.quit()
quit()
