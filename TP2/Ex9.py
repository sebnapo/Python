def remplMoy():
    remplissage = True
    liste = []
    sumMoy = 0
    while(remplissage):
        entree = input("Entrez une valeur : \n")

        if (entree == " "):
            remplissage = False
        else:
            if (len(liste) == 0):
                min = entree
                max = entree
                sumMoy = float(entree)
            else:
                if(entree < min):
                    min = entree
                elif(entree > max):
                    max = entree
                sumMoy += float(entree)
        liste.append(entree)
        moy = float(sumMoy) / float(len(liste))
        print(liste, "Max : ", max, "Min : ", min, "Moy : ", moy)

remplMoy()