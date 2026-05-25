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


    def update(self):
        lignes = self.tab
        colones = []
        colone = []
        a=0
        for i in range(self.c):
            for j in range(self.c):
                colone.append(lignes[j][i])

            colones.append(colone)
            colone = []

        new_tab = []
        new_ligne = []
        sum_lignes = []
        sum_colones = []

        for i in lignes:
            if sum(i) >= self.c:
                sum_lignes.append(sum(i))
            else:
                sum_lignes.append(self.c - sum(i))

        for i in colones:
            if sum(i) >= self.c:
                sum_colones.append(sum(i))
            else:
                sum_colones.append(self.c - sum(i))
        
        for i in sum_lignes:
            for j in sum_colones:
                if i%2 == 0 and j%2 == 0 and self.c/6 < i < self.c/1.5 and self.c/6 < j < self.c/1.5:
                    new_ligne.append(1)
                else:
                    a+=1
                    new_ligne.append(0)
            new_tab.append(new_ligne)
            new_ligne = []
        self.tab = new_tab
        self.age += 1
        return a # on pourrait utiliser le nombre de fois qu'on rentre dans la boucle du else pour définir un etat, un relation ou un autre truc. Parce que pârfois on ne rentre jamais dedans.

    import copy

    def update_life_game(self):
        new_tab = copy.deepcopy(self.tab)

        for i in range(self.c):
            for j in range(self.c):
                neighbor = 0
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

        self.tab = new_tab
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