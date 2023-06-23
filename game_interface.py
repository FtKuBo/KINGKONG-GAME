import pygame
class AffichageJeu:
    pygame.font.init()
    def __init__(self):
        self.sticker_image = pygame.image.load('asset/sticker.png')
        self.sticker_image = pygame.transform.scale(self.sticker_image, (30, 30))
        self.parametre = pygame.image.load('asset/settings.png')
        self.parametre = pygame.transform.scale(self.parametre, (50, 50))
        self.home = pygame.image.load('asset/home.png')
        self.home = pygame.transform.scale(self.home, (50, 50))
        self.sticker_image2 = pygame.image.load('asset/sticker2.png')
        self.sticker_image2 = pygame.transform.scale(self.sticker_image2, (30, 30))
        self.sticker_position = (465, 0)
        self.purple = pygame.image.load('asset/purple.png')
        self.purple = pygame.transform.scale(self.purple, (300, 250))
        self.green = pygame.image.load('asset/green.png')
        self.green = pygame.transform.scale(self.green, (300, 250))
        self.g_posy = -250
        self.p_posy = -250
        self.p_posx = 355
        self.g_posx = 355
        self.p_pos = (self.p_posx, self.p_posy)
        self.g_pos = (self.g_posx, self.g_posy)
        self.v_direction = 1
        self.v_pos = (289, -50)
        self.g_p_direction = 1
        self.L_direction = 1
        self.L_pos = (190, 0)
        self.replay = pygame.image.load('asset/replay.png')
        self.replay = pygame.transform.scale(self.replay, (300, 100))
        self.next = pygame.image.load('asset/next.png')
        self.next = pygame.transform.scale(self.next, (300, 100))
        self.r_pos = (365, 540)
        self.full = pygame.image.load('asset/full.jpg')
        self.full = pygame.transform.scale(self.full, (150, 20))
        self.mid = pygame.image.load('asset/mid.jpg')
        self.mid = pygame.transform.scale(self.mid, (150, 20))
        self.low = pygame.image.load('asset/low.jpg')
        self.low = pygame.transform.scale(self.low, (150, 20))
        self.img = pygame.image.load('asset/sticker-2.png')
        self.parscr = pygame.image.load('asset/grey.jpg')
        self.parscr = pygame.transform.scale(self.parscr, (800, 400))
        self.screen = pygame.display.set_mode((1000, 540))
        self.background = pygame.image.load('asset/bg.jpg')
        self.back = pygame.image.load('asset/back.jpg')
        self.back = pygame.transform.scale(self.back, (1000, 540))
        self.one_p = pygame.image.load('asset/one_player.png')
        self.one_p = pygame.transform.scale(self.one_p, (300, 100))
        self.multi_p = pygame.image.load('asset/two_player.png')
        self.multi_p = pygame.transform.scale(self.multi_p, (300, 100))
        self.victory = pygame.image.load('asset/win.jpg')
        self.Game_over = pygame.image.load('asset/Game-over.jpg')
        self.repos = (365, 0)
        self.arial24 = pygame.font.SysFont("arial", 24)
        self.arial25 = pygame.font.SysFont("arial", 60, True)
        self.arial26 = pygame.font.SysFont("arial", 60, True)
        self.un = pygame.image.load('asset/superman-flying.png')
        self.un = pygame.transform.scale(self.un, (100, 100))
        self.unpos=(0,250)
        self.a=pygame.image.load('asset/touche-du-clavier-a.png')
        self.a = pygame.transform.scale(self.a, (50, 50))
        self.e =pygame.image.load('asset/touche-du-clavier-e.png')
        self.e = pygame.transform.scale(self.e, (50, 50))
        self.fd =pygame.image.load('asset/touche-du-clavier-pointant-vers-la-droite.png')
        self.fd = pygame.transform.scale(self.fd, (50, 50))
        self.fg =pygame.image.load('asset/touche-de-variante-fleche-gauche-sur-le-clavier.png')
        self.fg = pygame.transform.scale(self.fg, (50, 50))
        self.arial27 = pygame.font.SysFont("inkfree", 60, True)
        self.arial28 = pygame.font.SysFont("inkfree", 30, True)
        self.arial29 = pygame.font.SysFont("inkfree", 20, True)
        self.croix = pygame.image.load('asset/marque-de-croix.png')
        self.croix = pygame.transform.scale(self.croix, (50, 50))




    def barre_de_vie_solo(self,grll):
        if grll.health == 90:
            self.screen.blit(self.full, (840, 5))
        if grll.health == 60:
            self.screen.blit(self.mid, (840, 5))
        if grll.health == 30:
            self.screen.blit(self.low, (840, 5))
    def ecranacceuil(self,game):
        self.dessination()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.continuer = 0
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_focused():
                    x, y = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0]:
                        if x > 25 and x < 280 and y > 275 and y < 350:
                            # button_sound.play()
                            game.continuer += 1
                if pygame.mouse.get_focused():
                    x, y = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0]:
                        if x > 690 and x < 970 and y > 275 and y < 350:
                            # button_sound.play()
                            game.continuer += 4
                if pygame.mouse.get_focused():
                    x, y = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0]:
                        if x > 10 and x < 60 and y > 10 and y < 60:
                            game.continuer += 10
    def parametrage(self):
        self.screen.blit(self.parscr, (100,70))
        self.screen.blit(self.fd,(300,250))
        self.screen.blit(self.fg,(300,350))
        self.screen.blit(self.a,(700,350))
        self.screen.blit(self.e,(700,250))
        Titre = self.arial27.render("LES TOUCHES", True, pygame.Color(255, 255, 255))
        self.screen.blit(Titre, (250,100 ))
        grlltouche = self.arial28.render("TOUCHES GORILLE :", True, pygame.Color(0, 0, 255))
        self.screen.blit(grlltouche, (110, 200))
        sngtouche = self.arial28.render("TOUCHES SINGE :", True, pygame.Color(0, 255, 0))
        self.screen.blit(sngtouche, (510, 200))
        rth = self.arial29.render("RIGHT:", True, pygame.Color(255, 255, 255))
        self.screen.blit(rth, (210, 265))
        self.screen.blit(rth, (610, 265))
        ltf = self.arial29.render("LEFT:", True, pygame.Color(255, 255, 255))
        self.screen.blit(ltf, (230, 365))
        self.screen.blit(ltf, (630, 365))
        self.screen.blit(self.croix,(840,75))
        pygame.display.flip()



    def dessiner(self,grll,bnn,nx,prj):
        self.screen.fill((0, 0, 0))
        self.surfacescore = self.arial24.render("Score : " + str(grll.score), True, pygame.Color(255, 255, 0))
        self.screen.blit(self.surfacescore, (5, 0))
        self.barre_de_vie_solo(grll)
        self.screen.blit(self.background, (0, 30))
        self.screen.blit(self.home, (10, 35))
        if grll.health > 0:
            self.screen.blit(grll.image, grll.pos)
        self.screen.blit(self.sticker_image, self.sticker_position)
        for prj.y in prj.nxlis:
            self.screen.blit(nx.image, prj.y)

        for prj.x in prj.bnnlis:
            self.screen.blit(bnn.image, prj.x)

        pygame.display.flip()

    def dessiner_rouge(self,grll):
        self.screen.fill((0, 0, 0))
        self.surfacescore = self.arial24.render("Score : " + str(grll.score), True, pygame.Color(255, 255, 0))
        self.screen.blit(self.surfacescore, (5, 0))
        self.barre_de_vie_solo(grll)
        self.screen.blit(self.background, (0, 30))
        self.screen.blit(self.home, (10, 35))
        if grll.health > 0:
            self.screen.blit(grll.red, grll.pos)
        self.screen.blit(self.sticker_image, self.sticker_position)

        pygame.display.flip()


    def dessiner2(self,grll,sng,bnn,nx,prj):
        self.screen.fill((0, 0, 0))
        self.barre_de_vie_duo(grll,sng)
        self.surfacescore = self.arial24.render("BANANAS: " + str(grll.score), True, pygame.Color(255, 0, 255))
        self.surfacescore2 = self.arial24.render("BANANAS: " + str(sng.score), True, pygame.Color(0, 255, 0))
        self.screen.blit(self.surfacescore, (200, 0))
        self.screen.blit(self.surfacescore2, (860, 0))
        self.screen.blit(self.background, (0, 30))
        self.screen.blit(self.home, (10, 35))
        if grll.health > 0:
            self.screen.blit(grll.image, grll.pos)
        self.screen.blit(self.sticker_image, (5, 0))
        self.screen.blit(self.sticker_image2, (665, 0))
        if sng.health > 0:
            self.screen.blit(sng.image, sng.pos)

        for prj.y in prj.nxlis:
            self.screen.blit(nx.image, prj.y)

        for prj.x in prj.bnnlis:
            self.screen.blit(bnn.image, prj.x)

        pygame.display.flip()

    # fonction pour rendre le gorille rouge
    def dessiner2_red_gorille(self,grll,sng):
        self.screen.fill((0, 0, 0))
        self.barre_de_vie_duo(grll,sng)
        self.surfacescore = self.arial24.render("BANANAS: " + str(grll.score), True, pygame.Color(255, 0, 255))
        self.surfacescore2 = self.arial24.render("BANANAS: " + str(sng.score), True, pygame.Color(0, 255, 0))
        self.screen.blit(self.surfacescore, (200, 0))
        self.screen.blit(self.surfacescore2, (860, 0))
        self.screen.blit(self.background, (0, 30))
        self.screen.blit(self.home, (10, 35))
        if grll.health > 0:
            self.screen.blit(grll.red, grll.pos)
        self.screen.blit(self.sticker_image, (5, 0))
        self.screen.blit(self.sticker_image2, (665, 0))
        if sng.health > 0:
            self.screen.blit(sng.image, sng.pos)


        pygame.display.flip()

    # fonction pour rendre le singe rouge
    def dessiner2_red_singe(self,grll,sng):
        self.screen.fill((0, 0, 0))
        self.barre_de_vie_duo(grll,sng)
        self.surfacescore = self.arial24.render("BANANAS: " + str(grll.score), True, pygame.Color(255, 0, 255))
        self.surfacescore2 = self.arial24.render("BANANAS: " + str(sng.score), True, pygame.Color(0, 255, 0))
        self.screen.blit(self.surfacescore, (200, 0))
        self.screen.blit(self.surfacescore2, (860, 0))
        self.screen.blit(self.background, (0, 30))
        self.screen.blit(self.home, (10, 35))
        if grll.health > 0:
            self.screen.blit(grll.image, grll.pos)
        self.screen.blit(self.sticker_image, (5, 0))
        self.screen.blit(self.sticker_image2, (665, 0))
        if sng.health > 0:
            self.screen.blit(sng.red, sng.pos)


        pygame.display.flip()

    # fonction affichage des barre de vie selon les pv des joueurs en duo
    def barre_de_vie_duo(self,grll,sng):
        if grll.health == 90:
            self.screen.blit(self.full, (40, 5))
        if grll.health == 60:
            self.screen.blit(self.mid, (40, 5))
        if grll.health == 30:
            self.screen.blit(self.low, (40, 5))
        if sng.health == 90:
            self.screen.blit(self.full, (700, 5))
        if sng.health == 60:
            self.screen.blit(self.mid, (700, 5))
        if sng.health == 30:
            self.screen.blit(self.low, (700, 5))

    def dessination(self):
        self.screen.blit(self.back, (0, 0))
        self.screen.blit(self.one_p, (10, 270))
        self.screen.blit(self.multi_p, (680, 270))
        self.screen.blit(self.parametre, (10, 10))
        pygame.display.flip()

    # fonction d'affichage de fin en solo pour la victoire
    def fin_v(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.victory, self.v_pos)
        self.screen.blit(self.next, self.r_pos)
        self.screen.blit(self.home, (10, 35))
        pygame.display.flip()

    # fonction d'affichage de fin en solo pour la defaite
    def fin_l(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.Game_over, self.L_pos)
        self.screen.blit(self.replay, self.r_pos)
        self.screen.blit(self.home, (10, 35))
        pygame.display.flip()

    # fonction d'affichage de fin en duo victoire du singe
    def duo_g(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.green, self.g_pos)
        self.screen.blit(self.replay, self.r_pos)
        self.screen.blit(self.home, (10, 35))
        pygame.display.flip()

    # fonction d'affichage de fin en duo victoire du gorille
    def duo_p(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.purple, self.p_pos)
        self.screen.blit(self.replay, self.r_pos)
        self.screen.blit(self.home, (10, 35))
        pygame.display.flip()

    # fonction d'affichage en cas d'egalite
    def duo_equality(self):
        rematch = self.arial25.render("REMATCH ", True, pygame.Color(255, 0, 0))
        self.screen.blit(rematch, self.repos)


import animation
import gorilla
import monkey
import banana
import noix
import main
import projectiles
prj=projectiles.Projectiles()

game = main.Jeu()
anim = animation.Animation()

nx = noix.Noix()
bnn = banana.Banane()
sng = monkey.Singe()
grll = gorilla.Gorille()



