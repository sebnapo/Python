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


g = arbre(noeud(1,noeud(0,term(),term()),noeud(5,term(),term())))
d = arbre(noeud(4,noeud(3,term(),term()),noeud(8,term(),term())))
a = arbre(noeud(2,g.root(),d.root()))

def afficherArbre(noeud):
    if(noeud == None):
        return 0
    else:
        print(noeud.val)
        afficherArbre(noeud.droite)
        afficherArbre(noeud.gauche)


afficherArbre(a.racine)

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
    return len(nodes)

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
    hierarchieRec(arbre.racine)


def hierarchieRec(noeud,boolean=True):
    if(noeud == None):
        return boolean
    else:
        if(noeud.val < noeud.droite.val )


print("Nombre node :")
print(nb_node(a))

print("somme " + str(summ(a)))

afficherArbre(a.racine)
afficherArbre(inc(a).racine)