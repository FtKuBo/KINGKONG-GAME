import pygame
import random
class Jeu:
#very ugly code didn't add any comments for the moment
    def __init__ (self):
        self.change = False
        self.change2 = False
        self.appui = False
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.running = 1
        self.secs = 0
        self.tr = False
        self.variable = 1
        self.continuer = 1




    def gererClavierSouris(self,grll):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.continuer = 0

        touchesPressees = pygame.key.get_pressed()
        if touchesPressees[pygame.K_RIGHT] == True and grll.pos[0] < 930:
            grll.pos = (grll.pos[0] + 3, grll.pos[1])
        if touchesPressees[pygame.K_LEFT] == True and grll.pos[0] > 0:
            grll.pos = (grll.pos[0] - 3, grll.pos[1])


    def gererClavierSourismulti(self,sng,grll):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.continuer = 0

        touchesPressees = pygame.key.get_pressed()
        if touchesPressees[pygame.K_RIGHT] == True and grll.pos[0] < 930:
            grll.pos = (grll.pos[0] + 3, grll.pos[1])
        if touchesPressees[pygame.K_LEFT] == True and grll.pos[0] > 0:
            grll.pos = (grll.pos[0] - 3, grll.pos[1])
        if touchesPressees[pygame.K_e] == True and sng.pos[0] < 930:
            sng.pos = (sng.pos[0] + 3, sng.pos[1])
        if touchesPressees[pygame.K_a] == True and sng.pos[0] > 0:
            sng.pos = (sng.pos[0] - 3, sng.pos[1])

    def redefinesolo(self,grll,gameaff,prj):
        gameaff.r_pos = (365, 540)
        gameaff.L_pos = (190, 0)
        grll.pos = (0, 390)
        grll.health = 90
        grll.score = 0
        prj.bnnlis = []
        prj.nxlis = []
        prj.lis = prj.list.copy()
        gameaff.unpos = (0,250)
        for i in range(8):
            prj.bnnlis.append(prj.lis.pop(random.randint(0, len(prj.lis) - 1)))
        for i in range(10):
            prj.nxlis.append(prj.lis.pop(random.randint(0, len(prj.lis) - 1)))
        gameaff.barre_de_vie_solo(grll)

    def redefineduo(self,grll,sng,gameaff,prj):
        gameaff.p_pos = (460, 0)
        gameaff.g_pos = (460, 0)
        gameaff.r_pos = (365, 540)
        grll.pos=(0,390)
        sng.pos=(800, 390)
        grll.score = 0
        sng.score = 0
        grll.health = 90
        sng.health = 90
        gameaff.repos = (365, 0)
        prj.bnnlis = []
        prj.nxlis = []
        prj.lis = prj.list.copy()
        gameaff.unpos = (0,250)
        for i in range(8):
            prj.bnnlis.append(prj.lis.pop(random.randint(0, len(prj.lis) - 1)))
        for i in range(10):
            prj.nxlis.append(prj.lis.pop(random.randint(0, len(prj.lis) - 1)))
        gameaff.barre_de_vie_duo(grll, sng)

game=Jeu()
import animation
import gorilla
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
grll=gorilla.Gorille()

pygame.init()
pygame.mixer.init()

pygame.display.set_caption("GORILLA")
pygame.display.set_icon(gameaff.img)
#boucle de tout le jeu

while game.variable == 1:
    #pygame.mixer.music.play(3000, 0, 5000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.continuer = 0
            pygame.quit()

    while game.continuer == 1:
        gameaff.ecranacceuil(game)

    while game.continuer == 2:
        game.clock.tick(game.FPS)
        gameaff.dessiner(grll,bnn,nx,prj)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.continuer = 0
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_focused():
                    x, y = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0]:
                        if x > 10 and x < 60 and y > 35 and y < 85:
                            # button_sound.play()
                            prj.vel = 5
                            game.continuer -= 1
                            game.redefinesolo(grll,gameaff,prj)

        pygame.display.flip()
        anim.comptearebour(game, gameaff)
        game.gererClavierSouris(grll)
        prj.affichagage()
        grll.uppoints(prj)
        grll.downpointssolo(nx,game,gameaff,prj)

        if grll.health <= 0:
            game.continuer += 8
            
        elif grll.score == 8:
            game.redefinesolo(grll,gameaff,prj)
            game.continuer += 2
        pygame.display.update()

    while game.continuer == 3:
        anim.defaitesolo(game,gameaff,prj,grll)

    while game.continuer== 4:
        anim.victoiresolo(game,gameaff,prj,grll)

    while game.continuer == 5:
        game.clock.tick(game.FPS)
        gameaff.dessiner2(grll,sng,bnn,nx,prj)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = 0
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_focused():
                    x, y = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0]:
                        if x > 10 and x < 60 and y > 35 and y < 85:  # retour a l acceuil toute en reinitialisant les variables et pos
                            # button_sound.play()
                            game.continuer-=4
                            game.redefineduo(grll,sng,gameaff,prj)

        pygame.display.flip()
        anim.comptearebour(game, gameaff)
        game.gererClavierSourismulti(sng,grll)
        prj.affichagage()
        grll.uppoints(prj)
        sng.uppoints(prj)
        grll.downpointsduo(nx,game,gameaff,sng,prj)
        sng.downpoints(nx,game,gameaff,grll,prj)

        if grll.health <= 0 or sng.health <= 0:  # envoire vers une autre boucle
            game.continuer += 4
        
        elif sng.score > 4:  # le singe gagne
            game.redefineduo(grll,sng,gameaff,prj)
            game.continuer+=2
        
        elif grll.score > 4:
            game.redefineduo(grll, sng, gameaff, prj)
            game.continuer += 1
        
        elif grll.score == sng.score == 4 or grll.health == sng.health == 0:
            game.redefineduo(grll, sng, gameaff,prj)
            game.continuer += 3

    while game.continuer == 6:
        anim.victoiregorille(game,gameaff,grll,sng,prj)
    
    while game.continuer == 7:
        anim.victoiresinge(game,gameaff,grll,sng,prj)
    
    while game.continuer == 8:
        anim.egalite(game,gameaff)
    
    while game.continuer == 9:
        anim.deathduo(game,gameaff,grll,sng,bnn,nx,prj)
    
    while game.continuer == 10:
        anim.deathsolo(game,gameaff,grll,bnn,nx,prj)
    
    while game.continuer == 11:
        gameaff.parametrage()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.continuer = 0
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_focused():
                    x, y = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0]:
                        if x > 840 and x < 890 and y > 75 and y < 125:
                            # button_sound.play()
                            print("pressé")
                            game.continuer = 1
        pygame.display.flip()

pygame.quit()





