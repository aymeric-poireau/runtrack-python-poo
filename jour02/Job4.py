class Student:
    def __init__(self, nom, prenom, num_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etudiant = num_etudiant
        self.__credits = 0
        
    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
        else:
            print("Le nombre de crédits ajouté doit être supérieur à zéro.")
        
john_doe = Student("Doe", "John", 145)

john_doe.add_credits(5)
john_doe.add_credits(3)
john_doe.add_credits(2)

print(john_doe._Student__prenom, john_doe._Student__nom, "a", john_doe._Student__credits, "crédits.")
