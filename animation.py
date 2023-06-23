import pygame


class Animation:
    def defaitesolo(self,game,gameaff,prj,grll):
        game.clock.tick(game.FPS)
        pygame.display.flip()
        gameaff.fin_l()
        # pygame.mixer.music.pause()
        game.vellocite = 5
        if gameaff.L_pos[1] < 100:
            gameaff.L_pos = (gameaff.L_pos[0], gameaff.L_pos[1] + 1.25 * gameaff.L_direction)
        if gameaff.r_pos[1] > 350 and gameaff.L_pos[1] == 100:
            gameaff.r_pos = (gameaff.r_pos[0], gameaff.r_pos[1] - 1.25 * gameaff.L_direction)
        # if r_pos[1] > 350:
        # lose_sound.play(0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.continuer = 0
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_focused():
                    x, y = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0] and gameaff.r_pos[1] == 350:
                        if x > 420 and x < 580 and y > 370 and y < 405:
                            # lose_sound.stop()
                            # button_sound.play()
                            prj.vel = 5
                            game.continuer -= 1
                    if pygame.mouse.get_pressed()[0]:
                        if x > 10 and x < 60 and y > 35 and y < 85:
                            # button_sound.play()
                            prj.vel = 5
                            game.continuer -= 2
                            game.redefinesolo(grll,gameaff,prj)

        pygame.display.update()
    def victoiresolo(self,game,gameaff,prj,grll):
        game.clock.tick(game.FPS)
        pygame.display.flip()
        gameaff.fin_v()
        # pygame.mixer.music.pause()
        if gameaff.v_pos[1] < 50:
            gameaff.v_pos = (gameaff.v_pos[0], gameaff.v_pos[1] + 1.25 * gameaff.v_direction)
        if gameaff.r_pos[1] > 350 and gameaff.v_pos[1] == 50:
            gameaff.r_pos = (gameaff.r_pos[0], gameaff.r_pos[1] - 1.25 * gameaff.L_direction)
        # if r_pos[1] > 350:
        # win_sound.play(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.continuer = 0
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_focused():
                    x, y = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0] and gameaff.r_pos[1] == 350:
                        if x > 420 and x < 580 and y > 370 and y < 405:
                            # win_sound.stop()
                            # button_sound.play()
                            # pygame.mixer.music.unpause()
                            prj.vel+=1.5
                            game.continuer -= 2
                    if pygame.mouse.get_pressed()[0]:
                        if x > 10 and x < 60 and y > 35 and y < 85:
                            # button_sound.play()
                            prj.vel= 5
                            game.continuer -= 3
                            game.redefinesolo(grll,gameaff,prj)
        pygame.display.update()

    def victoiregorille(self,game,gameaff,grll,sng,prj):
        game.clock.tick(game.FPS)
        pygame.display.flip()
        gameaff.duo_p()
        # pygame.mixer.music.pause()
        # angel.play(0)
        if gameaff.p_pos[1] < 100:
            gameaff.p_pos = (gameaff.p_posx, gameaff.p_pos[1] + 1.25 * gameaff.g_p_direction)
        if gameaff.r_pos[1] > 350 and gameaff.p_pos[1] == 100:
            gameaff.r_pos = (gameaff.r_pos[0], gameaff.r_pos[1] - 1.25 * gameaff.L_direction)
        # if r_pos[1] > 350:
        # angel.play(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.continuer = 0
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_focused():
                    x, y = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0] and gameaff.r_pos[
                        1] == 350:  # ne fonctionne que lorsque le bouton a fini de bouger
                        if x > 420 and x < 580 and y > 370 and y < 405:
                            # angel.stop()
                            # pygame.mixer.music.unpause()
                            # button_sound.play()
                            game.continuer -= 1
                    if pygame.mouse.get_pressed()[0]:
                        if x > 10 and x < 60 and y > 35 and y < 85:
                            # button_sound.play()
                            game.continuer -= 5
                            game.redefineduo(grll,sng,gameaff,prj)

    def victoiresinge(self,game,gameaff,grll,sng,prj):
        game.clock.tick(game.FPS)
        pygame.display.flip()
        gameaff.duo_g()
        # pygame.mixer.music.pause()
        if gameaff.g_pos[1] < 100:
            gameaff.g_pos = (gameaff.g_posx, gameaff.g_pos[1] + 1.25 * gameaff.g_p_direction)
        if gameaff.r_pos[1] > 350 and gameaff.g_pos[1] == 100:
            gameaff.r_pos = (gameaff.r_pos[0], gameaff.r_pos[1] - 1.25 * gameaff.L_direction)
        # if r_pos[1] > 350:
        # angel.play(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.continuer = 0
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_focused():
                    x, y = pygame.mouse.get_pos()
                    if pygame.mouse.get_pressed()[0] and gameaff.r_pos[1] == 350:
                        if x > 420 and x < 580 and y > 370 and y < 405:
                            print("appuer")
                            # angel.stop()
                            # pygame.mixer.music.unpause()
                            # button_sound.play()
                            game.continuer -= 2
                    if pygame.mouse.get_pressed()[0]:
                        if x > 10 and x < 60 and y > 35 and y < 85:
                            # button_sound.play()
                            game.continuer -= 6
                            game.redefineduo(grll,sng,gameaff,prj)
        pygame.display.update()
    def egalite(self,game,gameaff):
        game.clock.tick(game.FPS)
        if gameaff.repos[1] < 600:
            # pygame.mixer.music.pause()
            pygame.display.flip()

        gameaff.screen.fill((0, 0, 0))
        gameaff.duo_equality()
        if gameaff.repos[1] < 600:
            gameaff.repos = (gameaff.repos[0], gameaff.repos[1] + 3 * gameaff.g_p_direction)
        elif gameaff.repos[1] == 600:
            game.continuer -= 3
        pygame.display.update()

    def deathsolo(self,game,gameaff,grll,bnn,nx,prj):
        while grll.pos[1] < 600:  # meme chose mais pour la solo
            game.clock.tick(game.FPS)
            # dead_sound.play()
            # pygame.mixer.music.set_volume(0.2)
            pygame.display.flip()
            gameaff.dessiner(grll,bnn,nx,prj)
            gameaff.screen.blit(grll.rot, grll.pos)
            grll.pos = (grll.pos[0], grll.pos[1] + 3 * nx.direction)
            pygame.display.update()
            if grll.pos[1] == 600:
                game.redefinesolo(grll,gameaff,prj)
                game.continuer -= 7
                pygame.display.update()
            break
    def comptearebour(self,game,gameaff):
        if game.continuer!=1:
            zb=True
            while zb:
                if gameaff.unpos[0]<1200:
                    game.clock.tick(game.FPS)
                    pygame.display.flip()
                    gameaff.screen.fill((255, 255, 255))
                    ready = gameaff.arial26.render("BE READY !!!", True, pygame.Color(0,0, 0))
                    gameaff.screen.blit(ready, (350, 150))
                    gameaff.screen.blit(gameaff.un,gameaff.unpos)
                    gameaff.unpos = (gameaff.unpos[0] + 10 * 1, gameaff.unpos[1])

                else:
                    zb=False
                    break
        pygame.display.flip()


    def deathduo(self,game,gameaff,grll,sng,bnn,nx,prj):
        if grll.health <= 0 and grll.pos[1] < 600:
            while grll.pos[1] < 600:
                game.clock.tick(game.FPS)
                # dead_sound.play()
                #pygame.mixer.music.set_volume(0.2)
                pygame.display.flip()
                gameaff.dessiner2(grll,sng,bnn,nx,prj)
                gameaff.screen.blit(grll.rot, grll.pos)
                grll.pos = (grll.pos[0], grll.pos[1] + 3 * nx.direction)
                pygame.display.update()
                if grll.pos[1] == 600:
                    game.redefineduo(grll,sng,gameaff,prj)
                    game.continuer -= 2
                    print("j'aime les beate")
                break


        elif sng.health <= 0 and sng.pos[1] < 600:
            while sng.pos[1] < 600:
                game.clock.tick(game.FPS)
                # dead_sound.play()
                pygame.mixer.music.set_volume(0.2)
                pygame.display.flip()
                gameaff.dessiner2(grll,sng,bnn,nx,prj)
                gameaff.screen.blit(sng.rot, sng.pos)
                sng.pos= (sng.pos[0], sng.pos[1] + 3 * nx.direction)
                pygame.display.update()
                if sng.pos[1] == 600:
                    game.redefineduo(grll,sng,gameaff,prj)
                    game.continuer -= 3
                    print("j'aime les beates")
                break
        pygame.display.update()
import main
import gorilla
import monkey
import banana
import noix
import game_interface
import projectiles
prj=projectiles.Projectiles()
game=main.Jeu()
gameaff=game_interface.AffichageJeu()
nx=noix.Noix()
bnn=banana.Banane()
sng=monkey.Singe()
grll=gorilla.Gorille()