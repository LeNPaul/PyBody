import math
import random
import physics

particleList = []

class Particle(object):
    def __init__(self, mass, px, py, vx, vy):

        self.mass = mass

        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy

def generateParticles(particleNumber,case):

    for n in range(particleNumber):
        if case == "moon":
            r = random.randrange(0,1000)
            theta = random.uniform(0,6.3)
            px = 600 + int(r*math.sin(theta))
            py = 350 + int(r*math.cos(theta))
            vx = 0 
            vy = 0
            mass = 5
        else:
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
            physics.eulerIntegrator(centralMass,particle)
        if case == "leapFrog":
            for other in filter(lambda p: p != particle, particleList):
                physics.leapFrogIntegrator(particle,other)            
        else:
            for other in filter(lambda p: p != particle, particleList):
                physics.eulerIntegrator(particle,other)
