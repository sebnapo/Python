import random
def main():
    liste = []
    for i in range(100):
        liste.append(random.randint(0, 100))
    liste.sort()
    print(liste)
    x = int(input("Entrez votre nombre entre 0 et 100 \n"))
    while(not(0 <= x <= 100)):
        x = int(input("Entrez votre nombre entre 0 et 100 \n"))
    print(dichotomie(liste,x))

def dichotomie(liste,nombre):
    return(dicho_rec(liste,nombre,0,len(liste)-1))

def dicho_rec(liste,nombre,borneInf,borneSup):
    if (borneInf > borneSup): return "Pas de solution"
    centre = int((borneInf + borneSup)/2)
    if(nombre == liste[centre]):
        return centre

    elif(nombre < liste[centre]):
        return dicho_rec(liste,nombre,borneInf,centre-1) #car centre déjà exclus par le second if
    else:
        return dicho_rec(liste,nombre,centre+1,borneSup)

main()