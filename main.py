import random

from pandas._config import dates


class Indi:
    def __init__(self, id, c, nom, dadtab, momtab):
        self.nom=nom
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
        pass

    def affiche(self):
        for i in self.tab:
            print(str(i))


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

people=Indi(0, c, "Robert",dadtab_robert, momtab_robert)
people.affiche()


#people2=Indi(0, 3, "Roberta")
#people2.affiche()