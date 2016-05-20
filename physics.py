import math
import simulator

def gravity(selfMass,otherMass,distance):

    return simulator.G*selfMass*otherMass / (distance**2)

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
    self.vx += fx/self.mass * simulator.dt
    self.vy += fy/self.mass * simulator.dt

    self.px += self.vx * simulator.dt
    self.py += self.vy * simulator.dt
