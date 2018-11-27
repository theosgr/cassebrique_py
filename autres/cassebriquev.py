import pygame
import numpy as np
from random import *
from math import *

# Dimensions jeu

windowW = 900
windowH = 800

class Jeu :
    def __init__(self):
        self.game_over = False
        self.playing = False
        self.restart = True
        self.vies = 3 # On initialise le nombre de vies à 3
        self.imgVies = pygame.image.load('img/coeurVie.png')

        def afficherScores() :
            surf = self.imgVies
            window.blit(surf, (x,y))
            window.blit(surf, (x+10,y))
            window.blit(surf, (x+10,y))

        def distCoinGauche(balle, raquette):
            return np.sqrt((balle.x - paddle.x)**2 + (balle.y - paddle.y)**2)

        def distCoinGauche(balle, raquette):
            return np.sqrt((balle.x - paddle.x)**2 + (balle.y - paddle.y)**2)
