import math, numpy

def plusoumoinsOrdi(inf,sup):
    pas_trouve = True
    (search_inf, search_sup) = (inf,sup)
    while(pas_trouve):
        answer = 0
        essai = int((search_inf + search_sup)/2)
        while(answer not in ("y","+","-","stop")):
            answer = input("Est-ce le nombre " + str(essai) + " ? (y/+/-/stop) :\n")
        if(answer == "y"):
            print("BRAVO !")
            pas_trouve = False
        elif(answer == "+"):
            search_inf = essai
        elif (answer == "-"):
            search_sup = essai
        else:
            pas_trouve = False

plusoumoinsOrdi(0,100)





