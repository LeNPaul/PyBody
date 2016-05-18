import math
import random

#Colours

black = (0,0,0)
white = (255,255,255)

#Universal constants

particlelist = []

#Constants

#G = 6.67428e-11
G = 0.2
AU = (149.6e6 * 1000)
dt = 24*3600

#Parameters

class Particle(object):
    def __init__(self, mass, px, py, vx, vy):

        self.mass = mass

        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy

def integrator(self,other):

    #Returns the position and velocity of self object
    #Uses Euler numerical integration

    sx = self.px
    sy = self.py
    ox = other.px
    oy = other.py

    dx = (ox - sx)
    dy = (oy - sy)
    d = math.sqrt(dx**2 + dy**2)

    f = G*self.mass*other.mass / (d**2)

    theta = math.atan2(dy,dx)
    fx = math.cos(theta) * f
    fy = math.sin(theta) * f

    #Output
    self.vx += fx/self.mass * dt
    self.vy += fy/self.mass * dt

    self.px += self.vx * dt
    self.py += self.vy * dt

def drag(self):

        self.vx = self.vx*0.9
        self.vy = self.vy*0.9

#Generating particles

def generateparticles(particlenumber):

    for n in range(particlenumber):
        px = random.randint(0,700)
        py = random.randint(0,400)
        vx = 0
        vy = 0
        mass = random.randint(100,10000)

        particle = Particle(mass, px, py, vx, vy)

        particlelist.append(particle)
