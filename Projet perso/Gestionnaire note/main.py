class VieScolaire:

    def __init__(self):
        self.classe = {}
        self.commandes = {
            "ajouter": self.ajouter,
            "retirer": self.retirer,
            "afficher": self.afficher,
            "moyenne": self.moyenne,
            "moyenneclasse": self.moyenne_classe,

        }
        while True:
            entree = input().split()
            try:
                self.commandes[entree[0]](entree)
            except KeyError:
                print("Incorrect ! ")

    def ajouter(self, entree):
        if entree[1] not in self.classe:
            try:
                self.classe[entree[1]] = [int(entree[2])]
            except ValueError:
                print("Entrez un nombre ! ")
        else:
            try:
                self.classe[entree[1]].append(int(entree[2]))
            except ValueError:
                print("Entrez un nombre ! ")

    def retirer(self, entree):
        if int(entree[2]) in self.classe[entree[1]]:
            try:
                self.classe[entree[1]].remove(int(entree[2]))
            except ValueError:
                print("Entrez un nombre")
        elif not self.classe[entree[1]]:
            del self.classe[entree[1]]

        else:
            print("Note innexsistante")

    def afficher(self, entree):
        for keys in self.classe:
            print("\n", keys, ":", *self.classe[keys])

    def moyenne(self, entree):
        for keys in self.classe:
            print("\n", keys, ":", sum(self.classe[keys]) // len(self.classe[keys]))

    def moyenne_classe(self, entree):
        total_notes = 0
        nombre_notes = 0
        for keys in self.classe:
            total_notes += sum(self.classe[keys])
            nombre_notes += len(self.classe[keys])
        print("Moyenne de la classe : {}".format(total_notes // nombre_notes))


if __name__ == "__main__":
    VieScolaire()