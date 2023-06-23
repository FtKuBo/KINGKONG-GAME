import pygame
class Banane:
    def __init__(self):
        self.image = pygame.image.load('asset/banane.png')
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.pos = (random.randint(1,995), random.randint(30,60))
        self.direction= 1

import random
import animation
import gorilla
import monkey
import main
import noix
import game_interface
anim=animation.Animation()
gameaff=game_interface.AffichageJeu()
nx=noix.Noix()
game=main.Jeu()
sng=monkey.Singe()
grll=gorilla.Gorille()