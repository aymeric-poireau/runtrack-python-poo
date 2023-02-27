class Point:
    def __init__(self, x=2, y=4):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print("Les coordonnées du point sont ({}, {})".format(self.x, self.y))
    
    def afficherX(self):
        print("La coordonnée x du point est {}".format(self.x))
    
    def afficherY(self):
        print("La coordonnée y du point est {}".format(self.y))
    
    def changerX(self, nouveau_x):
        self.x = input()
    
    def changerY(self, nouveau_y):
        self.y = input()


op = Point()
op.changerY()