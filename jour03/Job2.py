class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert) -> None:
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher():
        print("Votre nom est: " + CompteBancaire.self.__nom + CompteBancaire.self.__prenom)
        print("Votre numero de compte est: " + CompteBancaire.self.__numero__compte)

    def retrait(self, montant):
        if self.solde >= montant or self.decouvert:
            self.solde -= montant
            print("Retrait de", montant, "effectué. Nouveau solde :", self.solde)
        else:
            print("Solde insuffisant.")

    def versement(self, montant):
        self.solde += montant
        print("Versement de", montant, "effectué. Nouveau solde :", self.solde)



