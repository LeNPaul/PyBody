import pygame
import simulator
import constant
import parameter
import Tkinter

#Setting up pygame

pygame.init()

clock = pygame.time.Clock()

simulationDisplay = pygame.display.set_mode((parameter.displayWidth, parameter.displayHeight))
pygame.display.set_caption("ApplePy Simulation")

icon = pygame.image.load('planet.png')
pygame.display.set_icon(icon)

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

def pause(count):
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
                    count = 0
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key in functionKeys:
                    functionKeys[event.key](simulationScreen)

        simulationDisplay.fill(constant.black)
        daysPassed(count)

        messageFunction("Press space bar to continue simulation",parameter.displayWidth/2,parameter.displayHeight/2)

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

def messageFunction(text,x,y):
    largeText = pygame.font.Font('freesansbold.ttf',30)
    textSurf, textRect = textObjects(text, largeText)
    textRect.center = ((x), (y))
    simulationDisplay.blit(textSurf, textRect)
    #pygame.display.update()

#Add button function here

#Button function

def button(text,x,y,buttonWidth,buttonHeight,inactiveColor,activeColor,action=None):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + buttonWidth/2 > mouse[0] > x - buttonWidth/2 and y + buttonHeight/2 > mouse[1] > y - buttonHeight/2:
        pygame.draw.rect(simulationDisplay, activeColor,(x-(buttonWidth/2),y-(buttonHeight/2),buttonWidth,buttonHeight))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(simulationDisplay, inactiveColor,(x-(buttonWidth/2),y-(buttonHeight/2),buttonWidth,buttonHeight))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = textObjects(text, smallText)
    textRect.center = ( (x), (y))
    simulationDisplay.blit(textSurf, textRect)

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

        messageFunction("ApplePy",parameter.displayWidth/2,parameter.displayHeight/8)

        messageFunction("n-body simulator",parameter.displayWidth/2,parameter.displayHeight/8 + 50)

        button("Start!", parameter.displayWidth/2,parameter.displayHeight/2,100,50, constant.green,constant.darkGreen,simulationLoop)

        pygame.display.update()
        clock.tick(30)

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
                    count = 0
                elif event.key == pygame.K_SPACE:
                    pause(count)
                elif event.key in functionKeys:
                    functionKeys[event.key](simulationScreen)

        simulationDisplay.fill(constant.black)

        #Update particle positions
        simulator.updatePositions(simulator.particleList,"euler")

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

#simulationIntro()
#simulationLoop()

#Initial start screen
top = Tkinter.Tk()
def hello():
   simulationLoop()

B1 = Tkinter.Button(top, text = "Start simulation", command = hello)
B1.pack()

top.mainloop()
