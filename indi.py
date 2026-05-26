import random
import copy

from pandas._config import dates


class Indi:
    def __init__(self, id, c, nom, dadtab, momtab):
        self.nom=nom
        self.papa=str(dadtab)
        self.maman=str(momtab)
        self.id=id
        self.c=c
        self.age=0
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

    def update_life_game(self):
        new_tab = copy.deepcopy(self.tab)

        for i in range(self.c):
            for j in range(self.c):
                neighbor = 0
                random_mutation = random.randint(0,100)
                if random_mutation > self.age//6:
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            if x == 0 and y == 0:
                                continue

                            ni = (i + x) % self.c
                            nj = (j + y) % self.c

                            if self.tab[ni][nj] == 1:
                                neighbor += 1
                    if self.tab[i][j] == 1:
                        if neighbor < 2 or neighbor > 3:
                            new_tab[i][j] = 0
                    else:
                        if neighbor == 3:
                            new_tab[i][j] = 1
                else:
                    new_tab[i][j] = 0

        self.tab = new_tab
        self.age += 1
        return new_tab

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