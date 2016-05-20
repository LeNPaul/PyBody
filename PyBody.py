import pygame
import simulator
import constant
import parameter

#Setting up pygame

clock = pygame.time.Clock()

simulationDisplay = pygame.display.set_mode((parameter.displayWidth, parameter.displayHeight))
pygame.display.set_caption("PyBody Simulation")
pygame.display.update()

#Pause function

def pause():
    paused = True

    pygame.display.update()    

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        clock.tick(5)

#Simulation start screen

def simulationIntro():

    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        
        simulationDisplay.fill(constant.white)

        pygame.display.update()
        clock.tick(15)

#Simulation loop

#Initial conditions
simulator.generateParticles(parameter.particleNumber,"")

def simulationLoop():

    simulationExit = False

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

#Calling simulation program functions

simulationIntro()
simulationLoop()
