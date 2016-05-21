import pygame
import simulator
import constant
import parameter

#Setting up pygame

pygame.init()

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

#Initialize a simulation screen object

simulationScreen = SimulationScreen(parameter.displayWidth,parameter.displayHeight)

#Dictionary of possible input values

functionKeys = {
    pygame.K_LEFT:   (lambda x: x.scroll(dx = 1)),
    pygame.K_RIGHT:  (lambda x: x.scroll(dx = -1)),
    pygame.K_DOWN:   (lambda x: x.scroll(dy = -1)),
    pygame.K_UP:     (lambda x: x.scroll(dy = 1)),
    pygame.K_EQUALS: (lambda x: x.zoom(2)),
    pygame.K_MINUS:  (lambda x: x.zoom(0.5)),
    pygame.K_z:      (lambda x: x.reset())}

#Diplay number of days passed

def daysPassed(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Day "+str(count), True, constant.white)
    simulationDisplay.blit(text,(0,0))

#Reset simulation function

def resetSimulation():
    simulationDisplay.fill(constant.black)
    simulator.particleList = []
    count = 0
    simulator.generateParticles(parameter.particleNumber,"moon")
    for particle in simulator.particleList:
        x = int(simulationScreen.mx + (simulationScreen.dx + particle.px) * simulationScreen.magnification)
        y = int(simulationScreen.my + (simulationScreen.dy + particle.py) * simulationScreen.magnification)

        size = int(simulationScreen.magnification)

        if size < 2:
            pygame.draw.circle(simulationDisplay,constant.white,(x,y),1,1)
        else:
            pygame.draw.circle(simulationDisplay,constant.white,(x,y),size,0)

    pygame.display.update()
    clock.tick(15)
    
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
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key in functionKeys:
                    functionKeys[event.key](simulationScreen)

        simulationDisplay.fill(constant.black)

        messageFunction("Press space bar to continue simulation")
        
        for particle in simulator.particleList:
            x = int(simulationScreen.mx + (simulationScreen.dx + particle.px) * simulationScreen.magnification)
            y = int(simulationScreen.my + (simulationScreen.dy + particle.py) * simulationScreen.magnification)

            size = int(simulationScreen.magnification)

            if size < 2:
                pygame.draw.circle(simulationDisplay,constant.white,(x,y),1,1)
            else:
                pygame.draw.circle(simulationDisplay,constant.white,(x,y),size,0)

        pygame.display.update()
        clock.tick(5)

#Message to screen function

def textObjects(text, font):
    textSurface = font.render(text, True, constant.white)
    return textSurface, textSurface.get_rect()

def messageFunction(text):
    largeText = pygame.font.Font('freesansbold.ttf',30)
    textSurf, textRect = textObjects(text, largeText)
    textRect.center = ((parameter.displayWidth/2), (parameter.displayHeight/2))
    simulationDisplay.blit(textSurf, textRect)
    pygame.display.update()

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
                if event.key in functionKeys:
                    functionKeys[event.key](simulationScreen)
        
        simulationDisplay.fill(constant.black)
        
        #Draw initial particles
        for particle in simulator.particleList:

            x = int(simulationScreen.mx + (simulationScreen.dx + particle.px) * simulationScreen.magnification)
            y = int(simulationScreen.my + (simulationScreen.dy + particle.py) * simulationScreen.magnification)

            size = int(simulationScreen.magnification)

            if size < 2:
                pygame.draw.circle(simulationDisplay,constant.white,(x,y),1,1)
            else:
                pygame.draw.circle(simulationDisplay,constant.white,(x,y),size,0)

        #Menu

        pygame.draw.rect(simulationDisplay, constant.white, (parameter.displayWidth/2-50,450,100,50))

        messageFunction("Press space bar to start simulation")

        pygame.display.update()
        clock.tick(15)

#Simulation loop

#Initial conditions
simulator.generateParticles(parameter.particleNumber,"moon")

def simulationLoop():

    count = 0

    simulationExit = False

    while not simulationExit:
        for event in pygame.event.get():

            #Handling quit events

            if event.type == pygame.QUIT:
                simulationExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    resetSimulation()
                elif event.key == pygame.K_SPACE:
                    pause()
                elif event.key in functionKeys:
                    functionKeys[event.key](simulationScreen)

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

        count += 1
        daysPassed(count)

        pygame.display.update()

        clock.tick(30)

    pygame.quit()
    quit()

#Calling simulation program functions

simulationIntro()
simulationLoop()
