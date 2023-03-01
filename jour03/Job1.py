class Ville:
    def __init__(self, nom_ville, population):
        self.__nom = nom_ville
        self.__population = population


    def getPopulation(self):
        return self.__population

class Personne:
    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville
    
    def ajouterPopulation(self):
        self.__population += 1

# création des objets Personne et Ville
john = Personne("John", 45, "Paris")
myrtille = Personne("Myrtille", 4, "Paris")
chloe = Personne("Chloé", 18, "Marseille")
paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

print("Population de Paris :", paris.getPopulation())
print("Population de Marseille :", marseille.getPopulation())
Personne.ajouterPopulation()
print("Mise a jour de la population de Paris :", paris.getPopulation())
print("Mise a jour de la population de Marseille :", marseille.getPopulation())

