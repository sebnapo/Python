import re
'''
def estceunnombre():
    nombre = False
    while(nombre == False):
        truc = input("Entrez un nombre :\n")
        nombre = True
        try:
            truc = int(truc)
            break
        except ValueError:
            try:
                truc = float(truc)
                break
            except ValueError:
                nombre = False

estceunnombre()

'''
'''
def validation(str):
    if((type(str) != int) and (type(str) != float)):
        return(False)
    else:
        return(str)
'''
'''
print(validation(5.5))
print(validation(5))
print(validation("abc"))
'''


def validation(str):
    n = 0
    for i in str:
        if (ord('0') <= ord(i) <= ord('9')):
            n = 10 * n + (ord(i) - ord('0'))
        else:
            return(False)
    return(n)

def validationAll(str):
    point = str.find(".")
    if(point == -1):
        return(validation(str))
    else:
        a = str[:point]
        b = str[(point+1):]

        if((validation(a) == False) or (validation(b) == False)):
            return(False)
        else:
            res = validation(a) + (validation(b) * 10**(-len(b)))
            return(res)



def calculer(str):
    if(str[len(str) - 1] != '='):
        return("Pas une opération")
    else:
        str = str[:-1]
        operande_index = -1
    for i in range(len(str)):
        if(str[i] in ["+","-","*","/","%"]):
            operande_index = i
            operande = str[i]
    if(operande_index == -1):
        return("Opérande incorrecte")
    a = validation(str[:operande_index])
    b = validation(str[(operande_index + 1):])

    if((a == False) or (b == False)):
        return("Un des deux arguments est invalide")
    else:
        if(operande == "+"): return(a+b)
        elif(operande == "-"): return(a-b)
        elif(operande == "*"): return(a*b)
        elif(operande == "/"): return(a/b)
        elif(operande == "%"): return(a%b)


print(validationAll("98"))
print(validationAll("12.125"))