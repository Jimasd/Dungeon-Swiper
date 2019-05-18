# -*- coding: utf-8 -*-
"""
Created on Sat May 11 13:35:54 2019

@author: Jimmy
"""
from random import randint, uniform

class GenererNiveau():
    
    def __init__(self, niveau):
        self.niveau = niveau
        self.longueurX = 15 + self.niveau * 3
        self.longueurY = 15 + self.niveau * 3
        self.lvl = []
        
    def genererLvl(self):
        self.creerBase()
        self.creerChemins()
        self.creerMur()
        self.printLvl()
        
    def getLvl(self):
        return self.lvl
        
    def creerBase(self):
        #0: rien
        #1: bloc
        
        for i in range(0,self.longueurY):
            rangee = []
            
            for j in range(0,self.longueurX):
                rangee.append(1)
            self.lvl.append(rangee)
    
    def creerChemins(self):
        enCreation = True
        longueurY = len(self.lvl) - 1
        longueurX = len(self.lvl[0]) - 1
        coord = [0, 0]
        fin = [longueurY, longueurX]
        
        while enCreation:
            self.lvl[coord[0]][coord[1]] = 0
            direction = uniform(0, 1)
            
            if direction < 0.1 and coord[0] > 0: #Haut
                coord[0] -= 1
            elif direction < 0.5 and coord[1] < longueurX: #Droit
                coord[1] += 1
            elif direction < 0.7 and coord[1] > 0: #Gauche
                coord[1] -= 1
            elif coord[0] < longueurY: #Bas
                coord[0] += 1
            
            if coord[0] == fin[0] and coord[1] == fin[0]:
                self.lvl[coord[0]][coord[1]] = 0
                enCreation = False

    def creerMur(self):

        for i, obj in enumerate(self.lvl):
            
            for j, obj in enumerate(self.lvl):
                if self.lvl[i][j] == 1:
                    self.lvl[i][j] = self.observerAutour(j, i)
                    
    def observerAutour(self, coordX, coordY):
        bas = False
        haut = False
        droite = False
        gauche = False
        diagHautDroite = False
        diagBasDroite = False
        diagHautGauche = False
        diagBasGauche = False
        adjDirecte = False
        
        #Blocs directement a cote
        if self.estUnBlocVide(coordX + 1, coordY):
            droite = True
        
        if self.estUnBlocVide(coordX - 1, coordY):
            gauche = True
        
        if self.estUnBlocVide(coordX, coordY - 1):
            haut = True
        
        if self.estUnBlocVide(coordX, coordY + 1):
            bas = True
        
        #Blocs en diagonals
        if self.estUnBlocVide(coordX + 1, coordY - 1):
            diagHautDroite = True
            
        if self.estUnBlocVide(coordX + 1, coordY + 1):
            diagBasDroite = True
        
        if self.estUnBlocVide(coordX - 1, coordY - 1):
            diagHautGauche = True
        
        if self.estUnBlocVide(coordX - 1, coordY + 1):
            diagBasGauche = True
            
        #Bloc Diretement a cote
        if not haut and not bas and not droite and not gauche:
            adjDirecte = True
            
        if ((adjDirecte)
             and ((not diagHautDroite and not diagBasDroite)
                   and (not diagHautGauche and not diagBasGauche))): #Bloc seul
            return 106
        elif ((haut and bas) #Simple
             or (haut and not bas and not droite and not gauche)
             or (not haut and bas and not droite and not gauche)):
            return 100
        elif ((droite and gauche)
             or (not haut and not bas and droite and not gauche)
             or (not haut and not bas and not droite and gauche)):
            return 101
        elif not haut and bas and not droite and not gauche: #Triple
            return 102
        elif not haut and not bas and droite and not gauche:
            return 103
        elif haut and not bas and not droite and not gauche:
            return 104
        elif not haut and not bas and not droite and gauche:
            return 105
        elif (((haut and not bas and droite and not gauche))
             or ((adjDirecte)
                  and (diagBasGauche))): #Double
            return 107
        elif (((not haut and bas and droite and not gauche))
             or ((adjDirecte)
                  and (diagHautGauche))):
            return 108
        elif (((haut and not bas and not droite and gauche))
             or ((adjDirecte)
                  and (diagBasDroite))):
            return 109
        elif (((not haut and bas and not droite and gauche))
             or ((adjDirecte)
                  and (diagHautDroite))):
            return 110
        elif not haut and not bas and not droite and not gauche: #Aucun
            return 106
        else:
            return 1
    def estUnBlocVide(self, posX, posY):
        
        if ((posX < self.longueurX and posX >= 0) 
                and (posY < self.longueurY and posY >= 0)):
            
            if self.lvl[posY][posX] == 0:
                return True
        return False
    

        
    def printLvl(self):
        string = ""
        
        for i, rg in enumerate(self.lvl):
            
            for j, elem in enumerate(self.lvl[i]):
                
                if elem == 1:
                    string += "# "
                elif elem == 0:
                    string += "  "
                elif elem == 100:
                    string += "\u2550 "
                elif elem == 101:
                    string += "\u2551 "
                elif elem == 102:
                    string += "\u2569 "
                elif elem == 103:
                    string += "\u2563 "
                elif elem == 104:
                    string += "\u2566 "
                elif elem == 105:
                    string += "\u2560 "
                elif elem == 107:
                    string += "\u2557 "
                elif elem == 108:
                    string += "\u255C "   
                elif elem == 109:
                    string += "\u2554 "
                elif elem == 110:
                    string += "\u255A "
                else:
                    string += "# "
            print(string)
            string = ""
            



