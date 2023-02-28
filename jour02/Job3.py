class Livre:
    def __init__(self, titre, auteur, nb_pages, disponible):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = disponible

    def get_titre(self):
        return self.__titre
        
    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre
        
    def get_auteur(self):
        return self.__auteur
        
    def set_auteur(self, nouveau_auteur):
        self.__auteur = nouveau_auteur
        
    def get_nb_pages(self):
        return self.__nb_pages
        
    def set_disponible(self):
        self.__disponible = True
    
    def verification(self):
        if self.__disponible:
            print("La valeur est True.")
        else:
            print("La valeur est False.")


    def set_nb_pages(self, nouveau_nb_pages):
        if isinstance(nouveau_nb_pages, int) and nouveau_nb_pages > 0:
            self.__nb_pages = nouveau_nb_pages
        else:
            print("Le nombre de pages doit être un entier positif.")
            
livre = Livre("pinpin", "inconnu", 300)
print(livre.get_titre())
print(livre.get_nb_pages())
livre.set_titre(input("nouveau titre: "))
nouveau_nb_pages = int(input("nombre de pages: "))
print(livre.get_titre())
livre.set_nb_pages(nouveau_nb_pages)
print(livre.get_nb_pages())