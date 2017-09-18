import math

def periSurf(rayon):
    p = 2* math.pi * rayon
    s = math.pi * rayon**2
    return(p,s)

def periSurfHaut(rayon,hauteur):
    ps = periSurf(rayon)
    return(ps[0] * hauteur + 2*ps[1], ps[1]*hauteur)

print(periSurf(5))
print(periSurfHaut(5,10))