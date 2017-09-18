import re

def estceunnombre():
    nombre = True
    truc = input("Entrez un nombre :\n")
    while
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




