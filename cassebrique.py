import pygame
import time
from random import *
from math import *

pygame.init()

windowH = 800
windowW = 500
life = 3;
lifeImg = pygame.image.load('img/coeurVie.png')
touchingLowerCase = True
balle = pygame.image.load('balles/balle1.png')
balleW = 18
balleH = 16
raquette = pygame.image.load('raquette/raquette.png')
raquetteW = 204
raquetteH = 24
estLancee = False
background = (113,177,227)
window = pygame.display.set_mode((windowH,windowW))
pygame.display.set_caption("Casse-Brique")




def main() :
	raquetteX = 400
	raquetteY = 470
	vX = 0
	vY = 0
	vitesse_balle = 0
	angle = 0
	balleX = 392
	balleY = 466 - raquetteH
	game_over = False
	moveLeft = False
	moveRight = False
	dx = 0
	while not game_over :
		for event in pygame.event.get() :
			if event.type == pygame.QUIT & life == 0:
				game_over = True
			if estLancee(vX,vY) == False:
				if event.type == pygame.KEYDOWN :
					vX = randint(0,10)
					vY = randint(0,50)
			if estLancee(vX,vY):
				if event.type == pygame.KEYDOWN :
					if event.key == pygame.K_LEFT :
						moveLeft = True
						dx = -1
					if event.key == pygame.K_RIGHT :
						moveRight = True
						dx = 1
				elif event.type == pygame.KEYUP :
					if event.key == pygame.K_LEFT :
						moveLeft = False
					if event.key == pygame.K_RIGHT :
						moveRight = False


		window.fill(background)
		displayBalle(balleX, balleY)
		displayRaquette(raquetteX,raquetteY)

		pygame.display.update()

		if raquetteX - raquetteW/2 == 0:
			dx = 1
		if raquetteX + raquetteW/2 == 800:
            dx = -1
        raquetteX += dx
        balleY += vY
        balleX += vX
        if isOver(balleY) :
            life = life - 1



def displayRaquette(x,y) :
	img = raquette
	displayRect = img.get_rect()
	displayRect.center = (x,y)
	window.blit(img,displayRect)
	pygame.display.update()

def displayBalle(x,y) :
	window.blit(balle,(x,y))

def isOver(by) :
	touchingLowerCase = by > 500
	return touchingLowerCase

def estLancee(vvX,vvY) :
	if vvX != 0 or vvY != 0 :
		return True
	else :
		return False

main()
pygame.quit()
quit()
