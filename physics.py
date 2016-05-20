import math
import simulator
import constants

def gravity(selfMass,otherMass,distance):

    return constants.G*selfMass*otherMass / (distance**2)

def eulerIntegrator(self,other):

    #Returns the position and velocity of self object
    #Uses Euler numerical integration

    dx = (other.px - self.px)
    dy = (other.py - self.py)
    
    distance = math.sqrt(dx**2 + dy**2)

    f = gravity(self.mass,other.mass,distance)

    theta = math.atan2(dy,dx)
    fx = math.cos(theta) * f
    fy = math.sin(theta) * f

    #Output
    self.vx += fx/self.mass * constants.dt
    self.vy += fy/self.mass * constants.dt

    self.px += self.vx * constants.dt
    self.py += self.vy * constants.dt
