import math
import universe

def gravity(selfMass,otherMass,distance):

    return universe.G*selfMass*otherMass / (distance**2)
