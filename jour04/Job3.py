class Rectangle:
    def __init__(self, longueur=23, largeur=15) -> None:
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur

    def perimetre(self, perimetre_):
        self.perimetre_ = perimetre_
        perimetre_ = 2*(self.__longueur+self.__largeur)
        print("Le perimetre du rectangle est", self.perimetre_)

    def surface(self, surface_):
        self.surface_ = surface_
        surface_ = self.__longueur * self.__largeur / 2
        print("La surface du rectangle est", self.surface_)


class Parallélépipède(Rectangle):
    def __init__(self, hauteur) -> None:
        self.hauteur = hauteur
        #Rectangle.__init__(self, longueur=25, largeur=12)

    def volume(self, volume_):
        self.volume_ = volume_
        volume_ = self.__longueur * self.__largeur * self.hauteur
        print("Le volume est", self.volume_)


rectangle1 = Rectangle(32, 23)
rectangle1.perimetre()
rectangle1.surface()

parallélépipède1 = Parallélépipède(10)
parallélépipède1.volume()