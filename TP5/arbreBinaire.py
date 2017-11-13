class arbre:
    def __init__(self,racine=None,nbElem=1):
        self.racine = racine
        self.nbElem = nbElem

    def empty(self):
        if(self.racine == None):
            return True
        else: return False

    def root(self):
        return self.racine


class noeud:
    def __init__(self,val, droite, gauche):
        self.val = val
        self.droite = droite
        self.gauche = gauche

def term():
    return None


g = arbre(noeud(11,noeud(12,term(),term()),noeud(7,term(),term())))
d = arbre(noeud(2,noeud(4,term(),term()),noeud(1,term(),term())))
a = arbre(noeud(6,g.root(),d.root()))

def afficherArbre(noeud):
    if(noeud == None):
        return 0
    else:
        print(noeud.val)
        afficherArbre(noeud.droite)
        afficherArbre(noeud.gauche)

def depth(arbre):
    paths = []
    pathfind(arbre.racine, paths)
    print(paths)
    return max(paths)


def pathfind(noeud, paths, count=0):
    if(noeud == None):
        paths.append(count)
    else:
        count += 1
        pathfind(noeud.gauche, paths, count)
        pathfind(noeud.droite, paths, count)

##print(depth(a))


def nb_node(arbre):
    nodes =  []
    pathfind(arbre.racine, nodes)
    return len(nodes)-1

def summ(arbre):
    somme = []
    sumRecursif(arbre.racine,somme)
    print(somme)
    return sum(somme)

def sumRecursif(noeud,somme):
    if(noeud == None):
        return 0
    else:
        somme.append(noeud.val)
        sumRecursif(noeud.droite,somme)
        sumRecursif(noeud.gauche,somme)

def inc(arbre):
    incRecursif(arbre.racine)
    return arbre

def incRecursif(noeud):
    if(noeud == None):
        return 0
    else:
        noeud.val += 1
        incRecursif(noeud.droite)
        incRecursif(noeud.gauche)

def hierarchie(arbre):
    bool = hierarchieRec(arbre.racine)
    return bool


def hierarchieRec(noeud,boolean=True):
    if(noeud == None):
        print(boolean)
        return boolean
    else:
        if(noeud.droite != None):
            if(noeud.val < noeud.droite.val ):
                boolean = False
                return boolean
        if(noeud.gauche != None):
            if(noeud.val < noeud.gauche.val):
                boolean = False
                return boolean
        hierarchieRec(noeud.droite,boolean)
        hierarchieRec(noeud.gauche,boolean)

print("Affichage de l'arbre a :")
afficherArbre(a.racine)
print("Nombre node :")
print(nb_node(a))

print("somme " + str(summ(a)))

print("Incrémentation de 1 de chaque noeud de l'arbre : ")
#afficherArbre(inc(a).racine)
print("Les fils sont-il tout inférieur aux parents ?")
print(hierarchie(a))

##------------------Partie arbre binaire de recherche-------------------##
def InsertionAbr(arbre,val):
    InsertionAbrRecursif(arbre.racine,val)

def InsertionAbrRecursif(node,val):
    if(node == None):
        return 0
    if(node.gauche == None and node.val >= val):
        node.gauche = noeud(val,term(),term())
    elif(node.gauche != None and node.val >= val):
        InsertionAbrRecursif(node.gauche,val)
    elif(node.droite == None):
        node.droite = noeud(val,term(),term())
    else:
        InsertionAbrRecursif(node.droite,val)


def InsertionAbrIteratif(arbre,val):
    inserer = False
    node = arbre.racine
    while(inserer == False):
        if(val <= node.val and node.gauche == None):
            node.gauche = noeud(val,term(),term())
            inserer = True
        elif(val <= node.val):
            node = node.gauche
        elif(node.droite == None):
            node.droite = noeud(val,term(),term())
            inserer = True
        elif(val > node.val):
            node = node.droite

def RechercheAbr(arbre,val):
    res = RechercheAbrRecursif(arbre.racine,val)
    return res


def RechercheAbrRecursif(node,val):
    trouve = False
    if (node == None):
        return trouve
    elif(node.val == val):
        trouve = True
        return trouve
    elif (node.val >= val):
        trouve = RechercheAbrRecursif(node.gauche,val)
    elif (node.val <= val):
        trouve = RechercheAbrRecursif(node.droite,val)
    return trouve


def rechercheNodeIteratif(arbre, val):

    node = arbre.racine
    trouve = False

    while((node != None) and (trouve == False)):
        if (node.val == val):
            trouve = True
        elif (node.val > val):
            node = node.gauche
        else:
            node = node.droite

    return(trouve)

def affichageCroissant(arbre):
    affichageNoeudCroissant(arbre.racine)

def affichageNoeudCroissant(noeud):
    if(noeud != None):
        affichageNoeudCroissant(noeud.gauche)
        if(noeud.gauche != None):
            print(",")
        print(str(noeud.val))
        if(noeud.droite != None):
            print(",")
        affichageNoeudCroissant(noeud.droite)


def affichageDecroissant(arbre):
    affichageNoeudDecroissant(arbre.racine)

def affichageNoeudDecroissant(noeud):
    if(noeud != None):
        affichageNoeudDecroissant(noeud.droite)
        if(noeud.droite != None):
            print(",")
        print(str(noeud.val))
        if(noeud.gauche != None):
            print(",")
        affichageNoeudDecroissant(noeud.gauche)


InsertionAbr(a,1)
InsertionAbrIteratif(a,0)
afficherArbre(a.racine)
print("recherche recursive :")
print(RechercheAbr(a,12))
print("Recherche itérative :")
print(rechercheNodeIteratif(a,12))
print("Affichage croissant :")
affichageCroissant(a)
print("Affichage decroissant :")
affichageDecroissant(a)