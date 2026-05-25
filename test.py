from indi import *
import sys
import pygame
import random  # Assure-toi que random est bien importé si non inclus dans 'indi'

c = 40
taille_case = 20  # Augmenté pour que la fenêtre soit visible (6 * 20 = 120x120)

pygame.init()
screen = pygame.display.set_mode((c * taille_case, c * taille_case))
clock = pygame.time.Clock()

print("dadtab_robert")
dadtab_robert = [[random.randint(0, 1) for j in range(c)] for i in range(c)]
for i in dadtab_robert:
    print(str(i))

print("\n")

print("momtab_robert")
momtab_robert = [[random.randint(0, 1) for j in range(c)] for i in range(c)]
for i in momtab_robert:
    print(str(i))

people = Indi(0, c, "Robert", dadtab_robert, momtab_robert)

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.KEYDOWN:
            screen.fill((255, 255, 255))

            tab = people.update_life_game()
            for i in range(len(tab)):
                for j in range(len(tab[i])):
                    if tab[i][j] == 1:
                        # CORRECTION ICI : position (i*taille, j*taille) et taille fixe (taille_case, taille_case)
                        pygame.draw.rect(
                            screen,
                            (0, 255, 0),
                            (i * taille_case, j * taille_case, taille_case, taille_case)
                        )
    pygame.display.flip()

pygame.quit()