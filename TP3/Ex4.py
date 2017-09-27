def NbChiffres(n,compteur = 1,base = 10):

    if(n // base == 0):
        return(compteur)
    else:
        return NbChiffres(n//base,compteur+1,base)




def convert(n,base):
    if(n // base == 0):
        print (n % base)
    else:
        print (n % base)
        convert(n//base,base)



convert(107,2)