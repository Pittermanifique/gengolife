import random

from pandas._config import dates


class Indi:
    def __init__(self, id, c, nom, dadtab, momtab):
        self.nom=nom
        self.papa=str(dadtab)
        self.maman=str(momtab)
        self.id=id
        self.c=c
        randomtab=[[random.randint(0, 1) for j in range(self.c)] for i in range(self.c)]
        self.tab=[]
        repartion = c/3
        for i in range(c):
            if i<repartion:
                self.tab.append(dadtab[i])
            elif repartion < i < repartion*2:
                self.tab.append(momtab[i])
            else:
                self.tab.append(randomtab[i])


    def update(self):
        lignes = self.tab
        colones = []
        colone = []

        for i in range(self.c):
            for j in range(self.c):
                colone.append(lignes[j][i])

            colones.append(colone)
            colone = []

        print(lignes)
        print(colones)


    def affiche(self):
        print(self.nom)
        for i in self.tab:
            print(str(i))
        print("\n")
    
    def adn(self):
        return self.tab
    
    # essai d'un bidule pour avoir en mémoire les parents d'un gugs, foireux. Faut voir comment prendre les noms des générations antérieures à l'individu
    def parents(self):
        print(self.papa + self.maman)



c = 6

print("dadtab_robert")
dadtab_robert=[[random.randint(0, 1) for j in range(c)] for i in range(c)]
for i in dadtab_robert:
    print(str(i))

print("\n")

print("momtab_robert")
momtab_robert=[[random.randint(0, 1) for j in range(c)] for i in range(c)]
for i in momtab_robert:
    print(str(i))

print("\n")

print("momtab_roberta")
momtab_roberta=[[random.randint(0, 1) for j in range(c)] for i in range(c)]
for i in momtab_robert:
    print(str(i))

print("\n")

print("dadtab_roberta")
dadtab_roberta=[[random.randint(0, 1) for j in range(c)] for i in range(c)]
for i in momtab_robert:
    print(str(i))

print("\n")

people=Indi(0, c, "Robert",dadtab_robert, momtab_robert)
people.affiche()
people.update()

pine_apple=Indi(1, c, "Roberta", dadtab_roberta, momtab_roberta)
pine_apple.affiche()

apple=Indi(1, c, "Robierto", people.adn(), pine_apple.adn())
apple.affiche()



#people2=Indi(0, 3, "Roberta")
#people2.affiche()