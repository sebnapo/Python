import math
def equationSolver(x,y,z):
    delta = (y**2) - (4*x*z)
    if(delta < 0):
        print("Pas do solution réel")
    elif(delta == 0):
        print("Une solution")
        return -y/2*x
    else:
        print("Deux solutions")
        res1 = (-y - math.sqrt(delta))/ 2*x
        res2 = (-y + math.sqrt(delta))/ 2*x
        return (res1,res2)

print(equationSolver(1,-3,2))