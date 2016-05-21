import math
import constant
import parameter

def gravity(selfMass,otherMass,distance):

    return constant.G*selfMass*otherMass / (distance**2)

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
    self.vx += fx/self.mass * parameter.dt
    self.vy += fy/self.mass * parameter.dt

    self.px += self.vx * parameter.dt
    self.py += self.vy * parameter.dt

def leapFrogIntegrator(self,other):

    #Returns the position and velocity of self object
    #Uses Leap Frog numerical integration

    dx = (other.px - self.px)
    dy = (other.py - self.py)
    
    distance = math.sqrt(dx**2 + dy**2)

    f1 = gravity(self.mass,other.mass,distance)

    theta = math.atan2(dy,dx)
    fx1 = math.cos(theta) * f1
    fy1 = math.sin(theta) * f1

    #Output

    self.px += self.px + self.vx * parameter.dt + 0.5 * (fx1/self.mass) * parameter.dt**2
    self.py += self.py + self.vy * parameter.dt + 0.5 * (fy1/self.mass) * parameter.dt**2

    dx = (other.px - self.px)
    dy = (other.py - self.py)
    
    distance = math.sqrt(dx**2 + dy**2)

    f2 = gravity(self.mass,other.mass,distance)

    theta = math.atan2(dy,dx)
    fx2 = math.cos(theta) * f2
    fy2 = math.sin(theta) * f2
    
    self.vx += self.vx + 0.5 * ((fx1+fx2)/self.mass) * parameter.dt
    self.vy += self.vy + 0.5 * ((fy1+fy2)/self.mass) * parameter.dt
