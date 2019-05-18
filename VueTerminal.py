# -*- coding: utf-8 -*-
"""
Created on Sun May 12 20:36:42 2019

@author: Jimmy
"""

class VueTerminalCmd():
    
    def __init__(self):
        self.encode = {0: "  ", #Vide
                       1: "# ", #Mur interieur
                       100: "\u2550 ", #Mur simple
                       101: "\u2551 ",
                       102: "\u2569 ", #Mur triple
                       103: "\u2563 ",
                       104: "\u2566 ",
                       105: "\u2560 ",
                       106: "\u256C ", #Mur quadruple
                       107: "\u2557 ", #Mur double
                       108: "\u255C ",
                       109: "\u2554 ",
                       110: "\u255A "
                       }
    
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