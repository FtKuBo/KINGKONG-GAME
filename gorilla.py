import pygame


class Gorille:
    def __init__(self):
        self.health = 90
        self.image = pygame.image.load('asset/gorille.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.red= pygame.image.load('asset/red gorille.png')
        self.red = pygame.transform.scale(self.red, (80, 80))
        self.pos = (0, 390)
        self.score = 0
        self.rot = pygame.image.load('asset/rot-gorilla.png')
        self.rot= pygame.transform.scale(self.rot, (80, 80))
    def uppoints(self,prj):
        for prj.x in prj.bnnlis:
            if prj.x[0] > self.pos[0] and prj.x[0] < self.pos[0] + 45 and prj.x[1] < \
                    self.pos[1] + 45 and prj.x[1] > self.pos[1]:
                print("bizarre")
                self.score += 1
                prj.bnnlis.remove(prj.x)

    def downpointsduo(self,nx,game,gameaff,sng,prj):
        for prj.y in prj.nxlis:  # si la noix est au meme endroit que le gorille vie -30 et elle disparait
            if prj.y[0] > self.pos[0] and prj.y[0] < self.pos[0] + 45 and prj.y[1] < self.pos[
                1] + 45 and prj.y[1] > self.pos[1]:
                prj.nxlis.remove(prj.y)
                game.tr = True
                while game.tr == True:  # l affichage pendant un bref instant du gorille en rouge pour faire un effet de degat
                    game.clock.tick(60)
                    game.secs += 1
                    if not game.secs == 5:
                        gameaff.dessiner2_red_gorille(self,sng)
                    elif game.secs == 5:
                        game.secs = 0
                        game.tr = False
                self.health -= 30
    def downpointssolo(self,nx,game,gameaff,prj):
        for prj.y in prj.nxlis: # si la noix est au meme endroit que le gorille vie -30 et elle disparait
            if prj.y[0] > self.pos[0] and prj.y[0] < self.pos[0] + 45 and prj.y[1] < self.pos[
                1] + 45 and prj.y[1] > self.pos[1]:
                prj.nxlis.remove(prj.y)
                game.tr = True
                while game.tr == True:  # l affichage pendant un bref instant du gorille en rouge pour faire un effet de degat
                    game.clock.tick(60)
                    game.secs += 1
                    if not game.secs == 5:
                        gameaff.dessiner_rouge(self)
                    elif game.secs == 5:
                        game.secs = 0
                        game.tr = False
                self.health -= 30

import animation
import main
import monkey
import banana
import noix
import game_interface
import projectiles
prj=projectiles.Projectiles()
anim=animation.Animation()
gameaff=game_interface.AffichageJeu()
nx=noix.Noix()
bnn=banana.Banane()
sng=monkey.Singe()
game=main.Jeu()