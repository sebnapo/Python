from tkinter import *
def hanoi(n):
    etat = [[], [], []]

    for i in range(n):
        etat[0].append(i)

    hanoiVrai(n,1,n,etat)

def hanoiVrai(n,i,j,etat):
    if (n > 0):
        printHanoi(etat)
        hanoiVrai(n-1,i,6-i-j,etat)
        print ("Déplace " + str(i) +"sur" + str(j))
        etat = changement(etat, i-1, j-1)
        printHanoi(etat)

        hanoiVrai(n-1,6-i-j,j,etat)




def changement(etat,a,b):

    move = etat[a][len(etat[a])-1]
    etat[a].pop()
    etat[b].append(move)

    return(etat)

def printHanoi(etat):

    print("||||||||||||||||||||||||")

    for i in range(3):

        pile = "["

        for j in range(len(etat[i])):

            pile += str(etat[i][j]+1)

        print(pile)




hanoi(3)

