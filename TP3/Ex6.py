from tkinter import *
def hanoi(n,i,j):
    if (n > 0):
        hanoi(n-1,i,6-i-j)
        print ("Déplace " + str(i) +"sur" + str(j))
        hanoi(n-1,6-i-j,j)

hanoi(3,1,3)