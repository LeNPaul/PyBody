import math
import random

particleList = []
particleNumber = 10;
dt = 1

class Particle(object):
    def __init__(self, mass, px, py, vx, vy):

        self.mass = mass
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy

def generateParticles(particleNumber):

    for n in range(particleNumber):
    
        px = random.randint(0,100)
        py = random.randint(0,100)
        vx = 0
        vy = 0
        mass = random.randint(1,10)

        particle = Particle(mass, px, py, vx, vy)
        particleList.append(particle)

def gravity(selfMass,otherMass,distance):

    return constant.G*selfMass*otherMass / (distance**2)

def eulerIntegrator(self, other):

    dx = (other.px - self.px)
    dy = (other.py - self.py)

    distance = math.sqrt(dx**2 + dy**2)

    f = gravity(self.mass,other.mass,distance)

    theta = math.atan2(dy,dx)
    fx = math.cos(theta) * f
    fy = math.sin(theta) * f

    self.vx += fx/self.mass * dt
    self.vy += fy/self.mass * dt

    self.px += self.vx * dt
    self.py += self.vy * dt

# Start simulation

generateParticles(particleNumber)
