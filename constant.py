#Colours

black = (0,0,0)
grey = (169,169,169)
white = (255,255,255)
green = (0,255,0)
darkGreen = (0,100,0)
orange = (255,165,0)
teal = (0,128,128)
yellow = (255,255,0)

#Universal constants

G = 6.67428e-11
AU = (149.6e6 * 1000)

#Planet data stored as planet name, mass, distance, velocity in SI units

planetData = [["mercury", 3.3011 * 10**23, -0.4*AU, 47.362*1000],
              ["venus", 4.8675 * 10**24, -0.7*AU, 35.02*1000],
              ["earth", 5.9742 * 10**24, -1*AU, 29.78*1000],
              ["mars", 6.4171 * 10**23, -1.5*AU, 24.077*1000],
              ["jupiter",1898 * 10**24, -5.2*AU, 13.1 * 1000],
              ["saturn", 568 * 10**24,-9.5*AU, 9.7 * 1000],
              ["uranus", 86.8 * 10**24, -19.2*AU, 6.8*1000],
              ["neptune", 102 * 10**24, -30.1*AU, 5.4 * 1000],
              ["pluto",1.46 * 10**22, -39*AU, 4.7 * 1000]]

#Generating list of planets as objects

#Common star variables

starData = [["sun",1.98892 * 10**30,0,0]]
