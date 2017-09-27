import random

def sort(tab):
    return(quickSort(tab,0,len(tab)-1))

def quickSort(tab,indinf, indsup):
    if(abs(indinf - indsup) <= 1):
        return "done"
    else:
        pivot = tab[0]
        ind_inf = indinf
        ind_sup = indsup
        while (ind_inf != ind_sup):
            if (tab[ind_inf] <= pivot):
                ind_inf += 1
            else:
                tab[ind_inf], tab[ind_sup] = tab[ind_sup], tab[ind_inf]
                ind_sup -= 1

        quickSort(tab,0,ind_inf)
        quickSort(tab,ind_inf,len(tab)-1)


tableau = []
for i in range(100):
    tableau.append(random.randint(0,100))

sort(tableau)

print(tableau)