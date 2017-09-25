def rempl():
    liste = []
    remplissage = True
    while(remplissage):
        entree = input("Entrez une valeur : \n")
        if (entree == " "):
            remplissage = False
        else:
            liste.append(entree)
    return(liste)

