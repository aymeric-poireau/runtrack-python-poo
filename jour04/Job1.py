class Personne:
    def __init__(self, nom, age=14):
        self.nom = nom
        self.age = age
  
    def afficherAge(self):
        print("L'âge de", self.nom, "est", self.age)
    

    def bonjour(self):
        print("Hello")


    def modifierAge(self, nouvel_age):
        self.nouvel_age = nouvel_age




class Eleve(Personne):
    def allerEnCours(self):
        print("je vais en cours")


    def affichageAge(self):
        print("J'ai", self.age, "ans")



class Professeur(Personne):
    def __init__(self, matiereEnseignée) -> None:
        self.matiereEnseignée = matiereEnseignée

    
    def enseigner(self):
        print("Le cours va commencer")


eleve1 = Eleve("Alice")
eleve1.affichageAge() 
