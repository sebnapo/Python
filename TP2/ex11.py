import Ex8

def palindromes():
    liste = Ex8.rempl()
    n = len(liste)
    listePal = []
    for i in range(n):
        pal = True
        n2 = len(liste[i])
        n2eff = int( len(liste[i]) / 2)
        for j in range(n2eff):
            if(liste[i][j] != liste[i][n2 - (j+1)]):
                pal = False
        if (pal):
            listePal.append(liste[i])
    return(listePal)

print(palindromes())