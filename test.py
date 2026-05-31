from indi import *
import sys
import pygame
import random  # Assure-toi que random est bien importé si non inclus dans 'indi'

c = 60
taille_case = 10  # Augmenté pour que la fenêtre soit visible (6 * 20 = 120x120)

dadtab_robert = [[random.randint(0, 1) for j in range(c)] for i in range(c)]
momtab_robert = [[random.randint(0, 1) for j in range(c)] for i in range(c)]

people = Indi(0, c, "Robert", dadtab_robert, momtab_robert)
tab = people.adn()

pygame.init()
screen = pygame.display.set_mode((c * taille_case, c * taille_case))
clock = pygame.time.Clock()

def fontsize(size):
    font = pygame.font.SysFont("Arial", size)
    return font

font_default = fontsize(20)
labels = []

class Label:
    ''' CLASS FOR TEXT LABELS ON THE WIN SCREEN SURFACE '''
    def __init__(self, screen, text, x, y, size=20, color="white"):
        if size != 20:
            self.font = fontsize(size)
        else:
            self.font = font_default
        self.image = self.font.render(text, 1, color)
        _, _, w, h = self.image.get_rect()
        self.rect = pygame.Rect(x, y, w, h)
        self.screen = screen
        self.text = text
        labels.append(self)
    def change_text(self, newtext, color="white"):
        self.image = self.font.render(newtext, 1, color)
    def change_font(self, font, size, color="white"):
        self.font = pygame.font.SysFont(font, size)
        self.change_text(self.text, color)
    def draw(self):
        self.screen.blit(self.image, (self.rect))

def show_labels():
    for _ in labels:
        _.draw()

running = True
Label(screen, "Hello World", 100, 100, 36)
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.KEYDOWN:
            tab = people.update_life_game()

    screen.fill((255, 255, 255))
    show_labels()
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == 1:
                pygame.draw.rect(
                    screen,
                    (0, 255, 0),
                    (i * taille_case, j * taille_case, taille_case, taille_case)
                )
    pygame.display.flip()

pygame.quit()