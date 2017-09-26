def factorielle(entier):
    if(entier <= 1):
        return 1
    else:
        return entier * factorielle(entier-1)

print(factorielle(5))