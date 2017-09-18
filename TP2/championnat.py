

def championnat(N,J,M):
    if(N%2 == 0):
        N1 = N
    else: N1 = N+1
    print("Il y aura" + str(N1-1) + "jours de championnat et " + str(N1/2) + " match par jour")

    if(M == 1):
        if(N%2 == 0): domicile = N1
    if(M > 1):
        domicile = ((J + M-2)%(N1 - 1)) + 1

    deplacement = (((J - M +N1 -1)%(N1 - 1))+1)

    if(domicile):
        print("Equipe à domicile: " + str(domicile) + "equipe en déplacement: " + str(deplacement))
