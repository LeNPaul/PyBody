import math
import random

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

def gravity(selfMass,otherMass,distance):

    return G*selfMass*otherMass / (distance**2)

def eulerIntegrator(self,other):

    #Returns the position and velocity of self object
    #Uses Euler numerical integration

    sx = self.px
    sy = self.py
    ox = other.px
    oy = other.py

    dx = (ox - sx)
    dy = (oy - sy)
    distance = math.sqrt(dx**2 + dy**2)

    f = gravity(self.mass,other.mass,distance)

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

def nBody(particleList):
    for particle in particleList:
        for other in filter(lambda p: p != particle, particleList):
            eulerIntegrator(particle,other)
