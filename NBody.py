for particle in Universe.particlelist:
        for other in filter(lambda p: p != particle, Universe.particlelist):
            Universe.integrator(particle,other)
            Universe.drag(particle)

        #x = int(displayWidth/2 + particle.px/Universe.AU*500)
        #y = int(displayHeight/2 + particle.py/Universe.AU*500)
        x = int(particle.px)
        y = int(particle.py)
