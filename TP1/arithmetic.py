def est_div_par(n,k):
    if(k == 0):
        return False
    if(n % k == 0):
        return True
    else:
        return False

def est_paire(x):
    return(est_div_par(x,2))

def est_compris_dans(a,b,c):
    if((b < a) and (c > a)):
        return True
    else: return False
print(est_compris_dans(1,2,6))