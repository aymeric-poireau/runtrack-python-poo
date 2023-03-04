x = int(input("Valeur de x:"))
n = int(input("Valeur de n:"))

def produit_recursif(n, x):
    
    if n == 0:
        return 0
    else:
        return x + produit_recursif(n-1, x)
    
resultat = produit_recursif(5, 3)
print(resultat)