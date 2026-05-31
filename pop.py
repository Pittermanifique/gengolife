import indi
import random
import copy


class pop:
    def __init__(self):
        self.individus = []
        self.liste_modif = []
        self.gen = 0

    def gen_base_pop(self, n_pepoles, c):
        if len(self.individus) == 0:
            for i in range(n_pepoles):
                new_indi = indi.Indi(i+1,c)
                new_indi.new_base_indi()
                self.individus.append(new_indi)

    def update_pop(self):
        for i in self.individus:
            i.update_life_game()

    def affiche(self):
        for i in self.individus:
            for j in i.tab:
                print(str(j))
            print("\n")

if __name__ == "__main__":
    population = pop()
    population.gen_base_pop(1,10)
    population.affiche()
    population.update_pop()
    population.affiche()

