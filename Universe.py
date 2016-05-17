import math
import random

#Colours

black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
yellow = (255,255,0)

#Universal constants

particlelist = []

#Constants

G = 6.67428e-11
AU = (149.6e6 * 1000)
dt = 24*3600

msun = 1.98892 * 10**30
mearth = 5.9742 * 10**24
dearth = -1*AU

#Parameters

class Particle(object):
    def __init__(self, mass, px, py, vx, vy):

        self.mass = mass

        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy

#Initial massive objects
sun = Particle(msun,0,0,0,0)
earth = Particle(mearth,-dearth,0,0,29.783 * 1000)

#Generating particles

def generateparticles(particlenumber):

    for n in range(particlenumber):
        #r = random.randint(0.2*AU,0.25*AU)
        #theta = random.uniform(0,6.3)
        #px = int(r*math.sin(theta))
        #py = int(r*math.cos(theta))
        px = random.randint(0,1200)
        py = random.randint(0,700)
        vx = 0#random.randint(0,100)*random.randint(-1,1)
        vy = 0#random.randint(0,100)*random.randint(-1,1)
        mass = random.randint(100,1000)

        particle = Particle(mass, px, py, vx, vy)

        particlelist.append(particle)
        
#Merge function

def merge(self,other, particlelist,i,p):

    if self.px == other.px and self.py == other.py:
        px = self.px
        py = self.py
        vx = self.vx + other.vx
        vy = self.vy + other.vy
        mass = self.mass + other.mass
        particlelist.pop(i)
        particlelist.pop(p)

        particle = Particle(mass, px, py, vx, vy)
        particlelist.append(particle)
        print "THIS SHIT WORKS"
