def NbChiffres(n,compteur = 1,base = 10):

    if(n // base == 0):
        return(compteur)
    else:
        return NbChiffres(n//base,compteur+1,base)




def convert(n,base,res = ""):
    if(n // base == 0):
        return res + str((n % base))
    else:
        return convert(n//base,base,(str((n//base) % base) + res ))

print(convert(107,2))