import pygame
import simulator
import constant
import parameter

#Setting up pygame

clock = pygame.time.Clock()

simulationDisplay = pygame.display.set_mode((parameter.displayWidth, parameter.displayHeight))
pygame.display.set_caption("PyBody Simulation")
pygame.display.update()

#Simulation screen

class SimulationScreen:
    def __init__ (self, width, height):
        self.width = width
        self.height = height
        (self.dx, self.dy) = (0, 0)
        (self.mx, self.my) = (0, 0)
        self.magnification = 1.0
        
    def scroll(self, dx=0, dy=0):
        self.dx += dx * parameter.displayWidth / (self.magnification*10)
        self.dy += dy * parameter.displayHeight / (self.magnification*10)
        
    def zoom(self, zoom):
        self.magnification *= zoom
        self.mx = (1-self.magnification) * self.width/2
        self.my = (1-self.magnification) * self.height/2
        
    def reset(self):
        (self.dx, self.dy) = (0, 0)
        (self.mx, self.my) = (0, 0)
        self.magnification = 1.0

simulationScreen = SimulationScreen(parameter.displayWidth,parameter.displayHeight)

#Reset function

def resetSimulation():
    simulationDisplay.fill(constant.black)
    simulator.particleList = []
    simulator.generateParticles(parameter.particleNumber,"")
    for particle in simulator.particleList:
        x = int(particle.px)
        y = int(particle.py)
        pygame.draw.circle(simulationDisplay,constant.white,(x,y),1,1)
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
                if event.key == pygame.K_r:
                    resetSimulation()
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
                if event.key == pygame.K_r:
                    resetSimulation()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        
        simulationDisplay.fill(constant.black)
        #Draw initial particles
        for particle in simulator.particleList:
            x = int(particle.px)
            y = int(particle.py)

            pygame.draw.circle(simulationDisplay,constant.white,(x,y),1,1)

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    resetSimulation()

                elif event.key == pygame.K_LEFT:
                    simulationScreen.scroll(dx=1)
                elif event.key == pygame.K_RIGHT:
                    simulationScreen.scroll(dx=-1)
                elif event.key == pygame.K_UP:
                    simulationScreen.scroll(dy=1)
                elif event.key == pygame.K_DOWN:
                    simulationScreen.scroll(dy=-1)
                elif event.key == pygame.K_EQUALS:
                    simulationScreen.zoom(2)
                elif event.key == pygame.K_MINUS:
                    simulationScreen.zoom(0.5)
             
                elif event.key == pygame.K_SPACE:
                    pause()

        simulationDisplay.fill(constant.black)

        #Update particle positions
        simulator.updatePositions(simulator.particleList,"")

        #Draw particles
        for particle in simulator.particleList:

            x = int(simulationScreen.mx + (simulationScreen.dx + particle.px) * simulationScreen.magnification)
            y = int(simulationScreen.my + (simulationScreen.dy + particle.py) * simulationScreen.magnification)

            size = int(simulationScreen.magnification)

            if size < 2:
                pygame.draw.circle(simulationDisplay,constant.white,(x,y),1,1)
            else:
                pygame.draw.circle(simulationDisplay,constant.white,(x,y),size,0)

        pygame.display.update()

        clock.tick(30)

    pygame.quit()
    quit()

#Calling simulation program functions

simulationIntro()
simulationLoop()
