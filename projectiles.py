import random
import banana
bnn=banana.Banane()
import noix
nx=noix.Noix()
class Projectiles:
    def __init__(self):
        self.list = [(10, random.randint(40,200)), (50, random.randint(40,200)), (110, random.randint(40,200)), (150, random.randint(40,200)), (190, random.randint(40,200)), (250, random.randint(40,200)), (320, random.randint(40,200)), (370, random.randint(40,200)), (410, random.randint(40,200)),
                     (480, random.randint(40,200)), (520, random.randint(40,200)), (560, random.randint(40,200)), (610, random.randint(40,200)), (670, random.randint(40,200)), (720, random.randint(40,200)), (800, random.randint(40,200)), (870, random.randint(40,200)), (950, random.randint(40,200))]
        self.direction=1
        self.x=0
        self.y=0
        self.bnnlis=[]
        self.nxlis=[]
        self.lis = self.list.copy()
        for i in range(10):
            self.nxlis.append(self.lis.pop(random.randint(0,len(self.lis)-1)))
        self.y = random.choice(self.nxlis)
        for i in range(8):
            self.bnnlis.append(self.lis.pop(random.randint(0,len(self.lis)-1)))
        self.x = random.choice(self.bnnlis)
        self.vel = 5


    def affichagage(self):

        for self.y in self.nxlis:  # affichage de plusieurs banane a des pos diff en meme temps
            noixtmp = self.y
            self.nxlis.remove(self.y)
            noixtmp = (noixtmp[0], noixtmp[1] + self.vel * self.direction)
            self.nxlis.insert(0, noixtmp)
            if self.y[1] < 0 or self.y[1] > 760:
                game.change = True
        for self.x in self.bnnlis:
            bananetmp = self.x
            self.bnnlis.remove(self.x)
            bananetmp = (bananetmp[0], bananetmp[1] + self.vel * self.direction)
            self.bnnlis.insert(0, bananetmp)
            if self.x[1] < 0 or self.x[1] > 700:
                game.change = True

        if game.change == True :
            self.lis = self.list.copy()
            for self.x in self.bnnlis:
                bananetmp = self.x
                self.bnnlis.remove(self.x)
                bananetmp=self.lis.pop(random.randint(0,len(self.lis)-1))
                self.bnnlis.insert(0, bananetmp)
            for self.y in self.nxlis:
                noixtmp = self.y
                self.nxlis.remove(self.y)
                noixtmp=self.lis.pop(random.randint(0,len(self.lis)-1))
                self.nxlis.insert(0, noixtmp)
            self.lis = self.list.copy()
            game.change = False




import animation
import gorilla
import monkey

import game_interface
import main
game=main.Jeu()
anim=animation.Animation()
gameaff=game_interface.AffichageJeu()
sng= monkey.Singe()
grll=gorilla.Gorille()