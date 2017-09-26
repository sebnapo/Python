import ex8

def inverse():
    liste = ex8.rempl()
    #print(liste)
    listInv = []
    n = len(liste)
    for i in range(n):
        listInv.append(liste[n-(i+1)])
    return(liste, listInv)

print(inverse())