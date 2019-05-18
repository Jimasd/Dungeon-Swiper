from Creatures import Joueur
from GenererLvl import GenererNiveau

class Jeu():
    
    def __init__(self):
        self.lvl = GenererNiveau(1)
        self.joueur = Joueur.Joueur(10, "Player 1", 2, 1, 0, 0, 0)
    
    def start(self):
        self.lvl.genererLvl()
        carte = self.lvl.getLvl()
        posX, posY = self.joueur.getPos()
        carte[posY][posX] = 1000 #1000 -> identification du joueur
        #self.lvl.printLvl()
    
    def setPosJoueur(self, x, y):
        pass

Jeu().start()