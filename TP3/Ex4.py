def NbChiffres(n,compteur = 1):

    if(n // 10 == 0):
        return(compteur)
    else:
        return NbChiffres(n//10,compteur+1)


print("Nombre de chiffre" + NbChiffres(1000))
