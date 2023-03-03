class Forme:
    def __init__(self, largeur, hauteur) -> None:
        self.largeur = largeur
        self.hauteur = hauteur
        self.hauteur = 34
        self.largeur = 17

    def aire(self):
        return 0



class Rectangle(Forme):
    def aire(self):
        return self.hauteur * self.largeur
        
rectangle1 = Rectangle()
print(rectangle1.aire())
