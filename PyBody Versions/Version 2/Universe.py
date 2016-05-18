import math
import random
#import PyBody

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
dt = 24*60

msun = 1.98892 * 10**30

mearth = 5.9742 * 10**24
dearth = -1*AU

msaturn = 568.34 * 10**24
mtitan = 1345.5 * 10**20
miapetus = 18.1 * 10**20

dtitan = 1221.83 * 10**3
dmimas = 185.52 * 10**3

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

def generateFieldParticles(particlenumber,displayWidth,displayHeight):

    for n in range(particlenumber):
        #r = random.randint(0.2*AU,0.25*AU)
        #theta = random.uniform(0,6.3)
        #px = int(r*math.sin(theta))
        #py = int(r*math.cos(theta))
        px = random.randint(0,displayWidth)
        py = random.randint(0,displayHeight)
        vx = 0#random.randint(0,100)*random.randint(-1,1)
        vy = 0#random.randint(0,100)*random.randint(-1,1)
        mass = random.randint(100,1000)

        particle = Particle(mass, px, py, vx, vy)

        particlelist.append(particle)

def generateMoonParticles(particlenumber):

    for n in range(particlenumber):
        r = random.randrange(0,4000000)
        #r = random.randint(0,10**10)
        theta = random.uniform(0,6.3)
        px = 0.3*dearth + int(r*math.sin(theta))#*random.randint(-1,1) 
        py = 0 + int(r*math.cos(theta))#*random.randint(-1,1)
        vx = 0 + random.randint(0,10000)*random.randint(-1,1)
        vy = 29.783*1000 + random.randint(0,10000)*random.randint(-1,1)
        mass = mearth

        particle = Particle(mass, px, py, vx, vy)

        particlelist.append(particle)

def distancelimit(i,particle):
    if abs(particle.px) > 3*AU:
        particlelist.pop(i)
        print len(particlelist)
    if abs(particle.py) > 3*AU:
        particlelist.pop(i)
        print len(particlelist)


def escapevelocity(i,particle,centralmass):
    v = math.sqrt(particle.vx**2+particle.vy**2)
    escv = math.sqrt((2*G*centralmass.mass)/(math.sqrt(particle.px**2+particle.py**2)))
    if v > escv:
        particlelist.pop(i)
        print len(particlelist) 
    
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
