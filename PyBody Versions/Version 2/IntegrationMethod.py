import math
import Physics

def euler(self,other):

    #Returns the position and velocity of self object
    #Uses Euler numerical integration

    sx = self.px
    sy = self.py
    ox = other.px
    oy = other.py

    dx = (ox - sx)
    dy = (oy - sy)
    d = math.sqrt(dx**2 + dy**2)

    f = Universe.G*self.mass*other.mass / (d**2)

    theta = math.atan2(dy,dx)
    fx = math.cos(theta) * f
    fy = math.sin(theta) * f

    #Output
    self.vx += fx/self.mass * Universe.dt
    self.vy += fy/self.mass * Universe.dt

    self.px += self.vx * Universe.dt
    self.py += self.vy * Universe.dt
