# -*- coding: utf-8 -*-
"""
Created on Sat May 11 10:59:46 2019

@author: Jimmy
"""
from Creatures.Entite import Entite

class Joueur(Entite):
    atkPnt = 1
    
    def __init__(self, vie: int, nom: str, armure: int, niveau: int, exp: int, 
                 posX: int, posY: int):
        super().__init__(vie, nom, armure, niveau, self.atkPnt, posX, posY)
        
    def lvlUp(self):
        self.atkPt += 0.5
        self.armure += 0.5
        self.niveau += 1
        
    def addExp(nb):
        self.exp += nb
        

#joueur = Joueur(10, "asd", 3, 3, 5)
#joueur.decrire()
