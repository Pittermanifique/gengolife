import indi
import random
import copy
from tqdm import tqdm

class Pop:
    def __init__(self,c):
        self.individus = []
        self.liste_interactions = []
        self.gen = 0
        self.c = c

    def gen_base_pop(self, n_pepoles):
        if len(self.individus) == 0:
            for i in range(n_pepoles):
                new_indi = indi.Indi(i,self.c)
                new_indi.new_base_indi()
                self.individus.append(new_indi)

    def new_interactions(self,id1,id2,interaction_type):
        if interaction_type == "same" or interaction_type == "xor":
            random_col = random.randint(0,self.c-1)
            random_line = random.randint(0,self.c-1)
            interaction = (id1,id2,interaction_type,(random_line,random_col))
            self.liste_interactions.append(interaction)

    def update_interactions(self):
        new_individus = copy.deepcopy(self.individus)
        for i in tqdm(self.liste_interactions):
            id1 = i[0]
            id2 = i[1]
            interaction_type = i[2]
            if interaction_type == "same":
                coo = i[3]
                target = new_individus[id2]
                base = self.individus[id1]
                target.tab[coo[0]][coo[1]] = base.tab[coo[0]][coo[1]]
            elif interaction_type == "xor":
                coo = i[3]
                target = new_individus[id2]
                base = self.individus[id1]
                if target.tab[coo[0]][coo[1]] == base.tab[coo[0]][coo[1]]:
                    target.tab[coo[0]][coo[1]] = 0
                else:
                    target.tab[coo[0]][coo[1]] = 1

        self.individus = new_individus


    def update_pop(self):
        self.update_interactions()
        for i in tqdm(self.individus):
            i.update_life_game()

    def affiche(self):
        for i in self.individus:
            for j in i.tab:
                print(str(j))
            print("\n")

if __name__ == "__main__":
    population = Pop(16)
    population.gen_base_pop(20000)

    for i in range(100000):
        population.new_interactions(0, 1, "same")
    for i in range(100000):
        population.new_interactions(0, 1, "xor")

    population.update_pop()
    population.affiche()

