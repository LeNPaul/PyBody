import math
import Physics

def euler(self,other):

    #Returns the position and velocity of self object
    #Uses Euler numerical integration

    Physics.force(self,other)

    #Output
    self.vx += fx/self.mass * dt
    self.vy += fy/self.mass * dt

    self.px += self.vx * dt
    self.py += self.vy * dt

def leapFrog(self,other):

    return none
