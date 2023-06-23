import pygame
import random
class Noix:
    def __init__(self):
        self.pos = (random.randint(1, 1000), random.randint(30, 120))
        self.image = pygame.image.load('asset/noix-de-coco.png')
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.direction= 1

import animation
import gorilla
import monkey
import banana
import game_interface
import main
game=main.Jeu()
anim=animation.Animation()
gameaff=game_interface.AffichageJeu()
bnn=banana.Banane()
sng=monkey.Singe()
grll=gorilla.Gorille()
