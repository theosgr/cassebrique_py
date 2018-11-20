class Brique(object):
    """Classe des brique"""
    def __init__(self, cordX, cordY, resistance):
        self.cordX = cordX
        self.cordX = cordX
        self.resistance = resistance

    def afficher():
        if self.resistance == 1 :
            window.blit(brique1,(self.cordX,self.cordY))
        if self.resistance == 2 :
            window.blit(brique2,(self.cordX,self.cordY))
        if self.resistance == 3 :
            window.blit(brique3,(self.cordX,self.cordY))
        if self.resistance == 4 :
            window.blit(brique4,(self.cordX,self.cordY))
        if self.resistance == 5 :
            window.blit(brique5,(self.cordX,self.cordY))
        if self.resistance == 6 :
            window.blit(brique6,(self.cordX,self.cordY))
        if self.resistance == 7 :
            window.blit(brique7,(self.cordX,self.cordY))
