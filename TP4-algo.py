##TP4
from random import *
##Exercices sur les structures de données simples :
## Exercice 1
##Q1
def insertion(l,i,val):
    if i > len(l)-1:
        print("insertion impossible dans la liste")
    else :
        li=[] 
        a=val
        for j in range(0,len(l)):
            if j<i:
                li.append(l[j])
            if j==i :
                li.append(a)
            if j>i:
                li.append(l[j-1])
        return(li)
liste=[1,2,3,4,5,4,3,2,1,2,3,4,5]

##Q2

# def concatenation(l1,l2):
#     return(l1+l2)

def concatenafion(l1,l2):
    for i in range(0,len(l2)-1):
        l1.append(l2[i])
    return(l1)
    
##Q3

def recherch_tablo(tablo,valeur):
    l=[]
    for i in range (0,len(tablo)-1):
        if tablo[i]==valeur :
            l.append(i)
    if len(l) ==0 :
        return(None)
    elif l==1: 
        return("La valeur est dans le tableau, à l'indice suivant : ",l[0])
    else :
        return("La valeur est dans le tableau, aux indices suivants : ",l)
        
##Exercice 2

##Q1+Q2
#classe premier élément 
#classe nombre
class Liste :
    def __init__(self,tete):
        self.tete=tete

    # def dernierel(self):
    #     l=self
    #     aide=l
    #     if l!=None:
    #         while aide.suiv != None :
    #             aide = aide.suiv
    #     return(aide)

    def insert(self,valeur,place):         #ici on insère APRES un élément
        insert=Element(None,valeur,None)   #insert est l'Element à insérer
        element=self.tete                  #element est l'élément étudié dans la liste
        if place==0 :                      #traitement du cas premier élément
            if element!=None:              #si liste non vide
                 element.prec=insert
            insert.suiv=element
            self.tete=insert
        else:
            i=0
            if element!=None :
                while (i < place-1) :
                    if element.suiv!=None :  #gère le dernier élément
                        element=element.suiv
                    i+=1
            insert.suiv=element.suiv
            insert.prec=element
            if element.suiv!=None :   #gère le dernier element
                element.suiv.prec=insert        #FONCTIONNEL <3
            element.suiv=insert
    def __str__(self):
        out=""
        element=self.tete
        while element!=None :
            out+=str(element.val)
            out+=" "
            element=element.suiv
        return out
        
class Element :
    def __init__(self, prec, val, suiv):
        self.prec=prec
        self.val=val
        self.suiv=suiv
##Q3
l1=Liste(Element(None,1,None))
l1.insert(2,0)
print(l1)
l2=Liste(Element(None,8,None))
l2.insert(9,1)
print(l2)    
concaten(l1,l2)

def concaten(l1,l2):
    i=9999
    element=l2.tete
    while element!=None :
        l1.insert(element.val,i)
        element=element.suiv
##Q4
def recherche_chain(liste,valeur):
    element=liste.tete
    i=0
    a=True
    while element.val!=valeur :
        element=element.suiv
        i+=1
        if element==None:
            print("la valeur n'est pas dans la liste")
            a=False
            break
    if a ==True :
        return("La valeur recherchée est dans la liste à la ", i , "ième position")

##EXERCICE 3

# Q1 : + - 4 * 3 2 / 5 2 correspond à  (4 -(3*2)+(5/2))       : OK
# Q2 : ((3 − 4)/(6 − 12)) ∗ ((7 + 2)/6) s'écrit : * / - 3 4 - 6 12 / + 7 2 6  :OK
# Q3 : On constate que l'algorithme fonctionne
# Q4 :
def Push(list,val):
    insertion(list,0,val)
def Pop(list):
    return(list.pop)
def Top(list):
    

# Q5 : 
def(evalprefix(chaine)): 


 

