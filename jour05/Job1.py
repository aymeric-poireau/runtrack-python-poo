def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)


resultat = factorielle(5)
print(resultat) # affiche 120