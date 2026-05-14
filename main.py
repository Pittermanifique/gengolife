import random


class Indi:
    def __init__(self, id, c, nom):
        self.nom=nom
        self.id=id
        self.c=c
        self.tab=[[random.randint(0, 1) for j in range(self.c)] for i in range(self.c)]
    def affiche(self):
        print(self.tab)
        for i in self.tab:
            print(str(self.nom))
            print(str(i))



people=Indi(0, 1, "Robert")
people.affiche()

people2=Indi(0, 3, "Roberta")
people2.affiche()