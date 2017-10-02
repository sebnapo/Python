from tkinter import *
def hanoi(n,i,j,tab):

    if (n > 0):
        hanoi(n-1,i,6-i-j,tab)
        print ("Déplace " + str(i) +"sur" + str(j))

        tab.append([i,j])


        hanoi(n-1,6-i-j,j,tab)



def etatHanoi(tab, n):

    etats = []

    placement = [n , 0, 0]

    etats.append(placement)

    for i in range (len(tab) - 1):

        newPlacement = [0, 0, 0]

        newPlacement[tab[i][0] - 1] = placement[tab[i][0] - 1] - 1
        newPlacement[tab[i][1] - 1] = placement[tab[i][1] - 1] + 1



        etats.append(newPlacement)

    return etats

tab = []

hanoi(3,1,3,tab)

print(tab)

print(etatHanoi(tab, 3))








'''

def jeuHanoi():

    tabDeplacements = []

    hanoi(3, 1, 3, tabDeplacements)

    print(tabDeplacements)




    n = len(tabDeplacements) - 1
    i = 0

    suivant = True
    while(suivant and (i <= n)):

        suivant = False
        i += 1

'''







