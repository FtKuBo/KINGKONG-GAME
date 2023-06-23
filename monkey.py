import pygame



class Singe:
    def __init__(self):
        self.health = 90
        self.image = pygame.image.load('asset/monkey.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.red = pygame.image.load('asset/red monkey.png')
        self.red = pygame.transform.scale(self.red, (80, 80))
        self.pos = (800, 390)
        self.score = 0
        self.rot = pygame.image.load('asset/rot-monkey.png')
        self.rot = pygame.transform.scale(self.rot, (80, 80))
    def uppoints(self,prj):
        for prj.x in prj.bnnlis:  # si la banane est au meme endroit que le gorille score+1 et elle disparait
            if prj.x[0] > self.pos[0] and prj.x[0] < self.pos[0] + 45 and prj.x[1] < \
                    self.pos[1] + 45 and prj.x[1] > self.pos[1]:
                self.score += 1
                prj.bnnlis.remove(prj.x)

    def downpoints(self,nx,game,gameaff,grll,prj):
        for prj.y in prj.nxlis:  # si la noix est au meme endroit que le gorille vie -30 et elle disparait
            if prj.y[0] > self.pos[0] and prj.y[0] < self.pos[0] + 45 and prj.y[1] < self.pos[
                1] + 45 and prj.y[1] > self.pos[1]:
                prj.nxlis.remove(prj.y)
                game.tr = True
                while game.tr == True:  # l affichage pendant un bref instant du gorille en rouge pour faire un effet de degat
                    game.clock.tick(60)
                    game.secs += 1
                    if not game.secs == 5:
                        gameaff.dessiner2_red_singe(grll,self)
                    elif game.secs == 5:
                        game.secs = 0
                        game.tr = False
                self.health -= 30
import animation
import gorilla
import main
import banana
import noix
import game_interface
import projectiles
prj=projectiles.Projectiles()
anim=animation.Animation()
gameaff=game_interface.AffichageJeu()
nx=noix.Noix()
bnn=banana.Banane()
game=main.Jeu()
grll=gorilla.Gorille()
