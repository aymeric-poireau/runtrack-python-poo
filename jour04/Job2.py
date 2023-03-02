class Personne:
    def __init__(self, nom, age=14):
        self.nom = nom
        self.age = age
  
    def afficherAge(self):
        print("L'âge de", self.nom, "est", self.age, "ans")
    

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
    def __init__(self, matiereEnseignée):
        self.matiereEnseignée = matiereEnseignée

    
    def enseigner(self):
        print("Le cours va commencer")


personne1 = Personne("Alice")
personne1.bonjour()
eleve1 = Eleve("Alice", 15)
eleve1.affichageAge()
eleve1.allerEnCours()

personne2 = Personne("Robert", 40)
personne2.bonjour()
personne2.afficherAge()
professeur1 = Professeur("Robert")
professeur1.enseigner()