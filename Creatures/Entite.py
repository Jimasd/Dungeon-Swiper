class Entite:
    
    def __init__(self, vie: int, nom: str, armure: int, niveau: int, 
                 atkPt: int, posX: int, posY: int):
        self.vie = vie
        self.nom = nom
        self.armure = armure
        self.niveau = niveau
        self.atkPt = atkPt
        self.__posX = posX
        self.posY = posY
    
    def attaquer(self, other):
        other.perdreVie(self.atkPt)
        
    def perdreVie(self, nbVie: int):
        self.vie -= nbVie
        
    def decrire(self):
        print(
              "Nom: {} \n".format(self.nom) +
              "Nombre de vie restante: {} \n".format(self.vie) +
              "Armure: {} \n".format(self.armure) +
              "Niveau: {} \n".format(self.niveau) +
              "Nombre d'attaque: {} \n".format(self.atkPt)
              )
    
    
    @property
    def posX(self):
        return self.__posX
        
    @posX.setter
    def posX(self, x):
        if x < 0:
            self.__posX = 0
        else:
            self.__posX = x
            
    @posX.getter
    def posX(self):
        return self.__posX
    
    def getVie(self) -> int:
        return self.vie
    
    def getArmure(self) -> int:
        return self.armure
    
    def getAtkPt(self) -> int:
        return self.atkPt

    def getNom(self) -> str:
        return self.nom
    
    def estMort(self) -> bool:
        return 0 <= self.vie
    
    def getPos(self) -> (int, int):
        return self.posX, self.posY
    
    def setPos(self, x: int, y: int):
        self.posX = x
        self.posY = y
        
test = Entite(10, "test", 10, 10, 1, 10, 10)
test.posX = -3
test.posX
    
