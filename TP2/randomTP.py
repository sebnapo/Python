from random import randint

def randomFunc():
    res = randint(0,100)
    boucle = False
    while(boucle == False):
        x = input("Entrez un nombre entre 0 et 100")
        if(int(x) == res):
            boucle = True
    return("BIEN JOUER")
    print(randomFunc())