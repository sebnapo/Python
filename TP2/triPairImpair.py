import random

def parite(size):
    liste = []
    for i in range(size):
        liste.append(random.randint(0,100))

    ind_pair = 0
    ind_impair = len(liste) - 1
    while (ind_pair != ind_impair):
        if (liste[ind_pair] % 2 == 0):
            ind_pair += 1
        else:
            liste[ind_pair],liste[ind_impair] = liste[ind_impair],liste[ind_pair]
            ind_impair -= 1
    return liste

print(parite(100))