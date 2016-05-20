import math
import random
import physics

#Colours

black = (0,0,0)
white = (255,255,255)

#Universal constants

particleList = []

#Constants

G = 6.67428e-11
dt = 24*3600

#Parameters

class Particle(object):
    def __init__(self, mass, px, py, vx, vy):

        self.mass = mass

        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy

def eulerIntegrator(self,other):

    #Returns the position and velocity of self object
    #Uses Euler numerical integration

    dx = (other.px - self.px)
    dy = (other.py - self.py)
    
    distance = math.sqrt(dx**2 + dy**2)

    f = physics.gravity(self.mass,other.mass,distance)

    theta = math.atan2(dy,dx)
    fx = math.cos(theta) * f
    fy = math.sin(theta) * f

    #Output
    self.vx += fx/self.mass * dt
    self.vy += fy/self.mass * dt

    self.px += self.vx * dt
    self.py += self.vy * dt
    
#Generating particles

def generateCloudParticles(particleNumber):

    for n in range(particleNumber):
        px = random.randint(0,1200)
        py = random.randint(0,700)
        vx = 0
        vy = 0
        mass = random.randint(10,50)

        particle = Particle(mass, px, py, vx, vy)
        particleList.append(particle)

def updatePositions(particleList,case):
    for particle in particleList:
        if case == "largeBody":
            eulerIntegrator(centralMass,particle)
        else:
            for other in filter(lambda p: p != particle, particleList):
                eulerIntegrator(particle,other)
