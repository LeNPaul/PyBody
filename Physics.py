import math
import Universe

def force(self,other):
    
    sx = self.px
    sy = self.py
    ox = other.px
    oy = other.py

    dx = (ox - sx)
    dy = (oy - sy)
    d = math.sqrt(dx**2 + dy**2)

    f = Universe.G*self.mass*other.mass / (d**2)

    theta = math.atan2(dy,dx)
    
    return (fx = math.cos(theta) * f, fy = math.sin(theta) * f)

#Drag
#Merge
#Collisions
