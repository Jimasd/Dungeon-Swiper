# -*- coding: utf-8 -*-
"""
Created on Sat May 11 22:15:26 2019

@author: Jimmy
"""
from random import uniform
from Creatures.Joueur import Joueur

class InstancierBataille():
    
    def __init__(self, otherJoueur, otherEntite):
        self.otherJoueur = otherJoueur
        self.otherEntite = otherEntite
        self.tour = "Joueur"
    def commencerBataille(self):
        
        while not (self.otherJoueur.estMort() or self.otherEntite.estMort()):
            self.rotationTour()
        nomMonstre = self.otherEntite.getNom()
        
        if self.otherEntite.estMort():
            xpRecu = self.otherEntite.getXP()
            msgVictoire = "Vous avez tué {} et vous avez reçu {} " \
                          "XP".format(nomMonstre, xpRecu)
            self.otherJoueur.addExp(xpRecu)
            self.afficherMessage(msgVictoire)
        else:
            msgDefaite = "Vous avez été tué par {}".format(nomMonstre)
            self.afficherMessage(msgDefaite)
        
    def tourAttaquant(self, otherAttaque, otherDefense):
        defense = otherDefense.getArmure()
        hitChance = uniform(0,1)
        
        if hitChance > defense/100:
            otherAttaque.attaquer(otherDefense)
            return otherAttaque.getAtkPt()
        else:
            return 0
        
    def rotationTour(self):
        
        if self.tour == "Entite":
            HPperdu = self.tourAttaquant(self.otherEntite, self.otherJoueur)
            msgAtk = "Vous avez perdu {} vie(s)".format(str(HPperdu))
            msgDef = "Vous avez bloqué le coup!"
            
            if HPperdu > 0:
                self.afficherMessage(msgAtk)
            else:
                self.afficherMessage("Vous avez bloqué le coup!")
            self.tour = "Joueur"
        else:
            HPperdu = self.tourAttaquant(self.otherJoueur, self.otherEntite)
            msgAtk = "Vous avez frappé {} pour {} " \
                     "vie(s)".format(self.otherEntite.getNom(), str(HPperdu)) 
            msgDef = "Oh non! {} a esquivé votre coup" \
                     ".".format(self.otherEntite)
            
            if HPperdu > 0:
                self.afficherMessage(msgAtk)
            else:
                self.afficherMessage(msgDef)
            self.tour = "Entite"
            
    def afficherMessage(self, message):
        print(message)
    
    
p1 = Joueur(10, "Player 1", 2, 1, 3434)
p2 = Joueur(7, "Player 2", 0.5, 1, 3)    

for i in range(0,10):
    p1.lvlUp()

btl = InstancierBataille(p1, p2)
btl.rotationTour()
p2.getVie()









