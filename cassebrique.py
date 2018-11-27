import pygame
import time
from random import *
from math import *

pygame.init()

horloge = pygame.time.Clock()
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
black = (0,0,0)
white = (255,255,255)
font = pygame.font.SysFont('BradBunR.ttf', 16)
window = pygame.display.set_mode((windowH,windowW))
pygame.display.set_caption("Casse-Brique")




def main() :
	raquetteX = 400
	raquetteY = 470
	vX = 0
	vY = 0
	angle = 0
	balleX = 392
	balleY = 466 - raquetteH
	game_over = False
	moveLeft = False
	moveRight = False
	dx = 0
	rectX = 0
	rectY = 0
	rectW = 0
	rectH = 0
	life = 3
	while not game_over :
		for event in pygame.event.get() :
<<<<<<< Updated upstream
			if event.type == pygame.QUIT:
				game_over = True
			if estLancee(vX,vY) == False:
				if event.type == pygame.KEYDOWN :
					if event.key == pygame.K_LEFT :
						vX = -1
						vY = -1
					if event.key == pygame.K_RIGHT :
						vX = 1
						vY = -1
=======
			if event.type == pygame.QUIT & life == 0:
				game_over = True
			if estLancee(vX,vY) == False:
				if event.type == pygame.KEYDOWN :
					vX = randint(0,10)
					vY = randint(0,50)
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
		displayLifes(40,0,life)

		pygame.draw.rect(window,black ,[100,50,50,15])
		pygame.draw.rect(window,black ,[100,70,50,15])
		pygame.draw.rect(window,black ,[100,90,50,15])
		pygame.draw.rect(window,black ,[100,110,50,15])
		pygame.draw.rect(window,black ,[100,130,50,15])
		pygame.draw.rect(window,black ,[100,150,50,15])
		pygame.draw.rect(window,black ,[100,170,50,15])

		pygame.draw.rect(window,black ,[160,50,50,15])
		pygame.draw.rect(window,black ,[160,70,50,15])
		pygame.draw.rect(window,black ,[160,90,50,15])
		pygame.draw.rect(window,black ,[160,110,50,15])
		pygame.draw.rect(window,black ,[160,130,50,15])
		pygame.draw.rect(window,black ,[160,150,50,15])
		pygame.draw.rect(window,black ,[160,170,50,15])

		pygame.draw.rect(window,black ,[220,50,50,15])
		pygame.draw.rect(window,black ,[220,70,50,15])
		pygame.draw.rect(window,black ,[220,90,50,15])
		pygame.draw.rect(window,black ,[220,110,50,15])
		pygame.draw.rect(window,black ,[220,130,50,15])
		pygame.draw.rect(window,black ,[220,150,50,15])
		pygame.draw.rect(window,black ,[220,170,50,15])

		pygame.draw.rect(window,black ,[280,50,50,15])
		pygame.draw.rect(window,black ,[280,70,50,15])
		pygame.draw.rect(window,black ,[280,90,50,15])
		pygame.draw.rect(window,black ,[280,110,50,15])
		pygame.draw.rect(window,black ,[280,130,50,15])
		pygame.draw.rect(window,black ,[280,150,50,15])
		pygame.draw.rect(window,black ,[280,170,50,15])

		pygame.draw.rect(window,black ,[340,50,50,15])
		pygame.draw.rect(window,black ,[340,70,50,15])
		pygame.draw.rect(window,black ,[340,90,50,15])
		pygame.draw.rect(window,black ,[340,110,50,15])
		pygame.draw.rect(window,black ,[340,130,50,15])
		pygame.draw.rect(window,black ,[340,150,50,15])
		pygame.draw.rect(window,black ,[340,170,50,15])
=======
>>>>>>> Stashed changes

		pygame.display.update()

		if raquetteX - raquetteW/2 == 0:
			dx = 1
		if raquetteX + raquetteW/2 == 800:
<<<<<<< Updated upstream
			dx = -1
		raquetteX += dx

		if estLancee(vX,vY) :

			if balleX <= 0:
				vX = -vX
			if balleX >= 790:
				vX = -vX
			if balleY <= 0:
				vY = -vY
			#if balleY == raquetteY & raquetteX + dx<= balleX <= raquetteX - dx : # A modifier
			#	vY = -vY

			balleX += vX
			balleY += vY




		if isOver(balleY) :
			life = life - 1
			if life == -1 :
				game_over = True


	if playAgain() :
		main()
=======
            dx = -1
        balleY += vY
        balleX += vX
        if isOver(balleY) :
            life = life - 1


>>>>>>> Stashed changes

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

def displayLifes(x,y,life) :
	vie = font.render("Vies restantes: " + str(life), False, black, white)
	window.blit(vie,(x,y))



def playAgain() :
	time.sleep(2)
	while True :
		for event in pygame.event.get([pygame.KEYDOWN,pygame.QUIT]) :
			if event.type == pygame.QUIT :
				return False
			elif event.type == pygame.KEYDOWN :
				return True
		horloge.tick()

main()
pygame.quit()
quit()
