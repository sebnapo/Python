import random

def sort(tab):
    return(quickSort(tab,0,len(tab)-1))

def quickSort(tab, debut, fin):
    print(tab)
    if (fin - debut < 1): #condition d'arrêt : "sous-tableaux" de 1 elt
        return("done")

    else:
        pivot = tab[debut]
        ind_inf = debut + 1
        ind_sup = fin
        #TRI, arrêt quand ind_inf > ind_sup
        while (ind_inf <= ind_sup):
            print(tab)
            if (tab[ind_inf] <= pivot):
                ind_inf += 1
            else:
                tab[ind_inf], tab[ind_sup] = tab[ind_sup], tab[ind_inf]
                ind_sup -= 1

        #échange du pivot avec le dernier des elts triés à gauche.

        tab[debut], tab[ind_sup] = tab[ind_sup], tab[debut]

        # on trie tout sauf le pivot comme ça on est sûr que les sous-tableaux se réduisent
        quickSort(tab, debut, ind_sup - 1)
        quickSort(tab, ind_inf, fin)


tableau = []
for i in range(50):
    tableau.append(random.randint(0,100))


sort(tableau)
