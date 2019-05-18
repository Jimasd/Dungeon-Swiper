# -*- coding: utf-8 -*-
"""
Created on Sun May 12 18:58:45 2019

@author: Jimmy
"""
from Creatures.Entite import Entite

class Monstre(Entite):
    
    def __init__(self, vie: int, nom: str, armure: int, niveau: int, posX: int,
                 posY: int):
        super().__init__(vie, nom, armure, niveau, self.atkPnt, posX, posY)
    
    def getXP(self) -> int:
        return self.niveau + self.armure + self.vie/10 + self.atkPnt