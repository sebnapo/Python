import numpy

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
d = arbre(noeud(4,noeud(3,term(),term()),noeud(5,noeud(5,term(),term()),term())))
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

print(depth(a))
