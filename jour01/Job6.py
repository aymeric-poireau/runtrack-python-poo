class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

# Instancier un objet Animal
mon_animal = Animal()

# Afficher l'âge initial de l'animal
print("L'age de l'animal :", mon_animal.age)

# Faire vieillir l'animal et afficher son âge après le vieillissement
mon_animal.vieillir()
print("L'age de l'animal :", mon_animal.age)