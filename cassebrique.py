# Import
import pygame
import time
from random import *
from math import *

pygame.init() # initialisation du module pygame

#Variables globales initialisation

horloge = pygame.time.Clock()
windowH = 800
windowW = 500
lifeImg = pygame.image.load('img/coeurVie.png')
touchingLowerCase = True
balle = pygame.image.load('balles/balle1.png')
balleW = 18
balleH = 16
life = 0
raquette = pygame.image.load('raquette/raquette.png')
raquetteW = 204
raquetteH = 24
estLancee = False
brique = pygame.image.load('briques/brique6.png')
briqueW = 70
briqueH = 30
briques = []
background = (113,177,227)
black = (0,0,0)
white = (255,255,255)
font = pygame.font.SysFont('BradBunR.ttf', 16)
fontt = pygame.font.SysFont('CHLORINR.ttf', 16)
window = pygame.display.set_mode((windowH,windowW))
pygame.display.set_caption("Casse-Brique")
windowAccueil = pygame.display.set_mode((windowH,windowW))
backgroundAcc = pygame.image.load('img/degradeGris.jpg').convert()
lesBriques = []
CoordBrique = []


# Fonction main pour le fonctionnement du jeu
def main() :
	raquetteX = 400
	raquetteY = 470
	vX = 0
	vY = 0
	briqueX = 100 #Position de depart d'une brique qu'on implemente apres dans une boucle pour toutes les afficher
	briqueY = 50
	angle = 0
	balleX = 392
	balleY = 466 - raquetteH
	game_over = False
	moveLeft = False
	moveRight = False
	dx = 0
	#global life | je ne pense pas que le global ici soit necessaire
        
	while not game_over :
		for event in pygame.event.get() :
			if event.type == pygame.QUIT:
				#game_over = True
				quit()
			if estLancee(vX,vY) == False:
				if event.type == pygame.KEYDOWN :
					if event.key == pygame.K_LEFT :
						vX = -1
						vY = -1
					if event.key == pygame.K_RIGHT :
						vX = 1
						vY = -1
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
		displayBriques()
		displayLifes(40,0,life)
		displayBalle(balleX, balleY)
		displayRaquette(raquetteX,raquetteY)
		



		pygame.display.update()

                #Raquette revient quand elle touche les bords
		if raquetteX - raquetteW/2 == 0:
			dx = 1
		if raquetteX + raquetteW/2 == 800:
			dx = -1
		raquetteX += dx

		if estLancee(vX,vY) :
                        #La balle touche les bords
			if balleX <= 0:
				vX = -vX
			if balleX >= 790:
				vX = -vX
			if balleY <= 0:
				vY = -vY
			#La balle touche la raquette
			if balleY == 468 - raquetteH and balleX > raquetteX - raquetteW/2 and balleX < raquetteX + raquetteW/2 :
				vY = -vY

                        #La balle touche une brique
			numeroBrique = 0
			for i in lesBriques :
				if balleX-balleH/2 > i[0]-briqueW/2 and balleX+balleH/2 < i[0] + briqueW/2 and (balleY+balleH/2 == i[1]+briqueH/2 or balleY-balleH/2 == i[1]-briqueH/2) :
					vY = -vY
					del lesBriques[numeroBrique]
				if balleY-balleH/2 > i[1]-briqueH/2 and balleY+balleH/2 < i[1]+briqueH/2 and (balleX-balleW/2 == i[0]+briqueW/2 or balleX+balleW/2 == i[0]-briqueW/2) :
					vX = -vX
					del lesBriques[numeroBrique]
				numeroBrique = numeroBrique + 1

			balleX += vX
			balleY += vY





		if isOver(balleY) :
			continuer = True
			perdUneVie()
			displayMessage("Vous perdez une vie, appuyez sur espace pour continuer", 30, windowW/2+150,windowH/2)
			while continuer:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						#game_over = True
						quit()
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_SPACE:
							main()
						elif event.type == pygame.KEYDOWN:
							if event.key == pygame.K_ESCAPE:
								continuer = False
								game_over = True
		if win() :
			continuer = True
			displayMessage("Vous avez gagné !! Appuyez sur espace pour continuer", 30, windowW/2+150,windowH/2)
			while continuer:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						#game_over = True
						quit()
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_SPACE:
							accueil()
					elif event.type == pygame.KEYDOWN:
						if event.key == pygame.K_ESCAPE:
							continuer = False
							game_over = True


	if playAgain() :
		main()

# Fonction qui fait perdre une vie a un joueur, return accueil() si il n a plus de vie
def perdUneVie() :
        global life
        life = life - 1
        if life < 0 :
                accueil()

# fonction affichant la raquette
def displayRaquette(x,y) :
	img = raquette
	displayRect = img.get_rect()
	displayRect.center = (x,y)
	window.blit(img,displayRect)
	pygame.display.update()

#fonction affichant la balle
def displayBalle(x,y) :
	window.blit(balle,(x,y))

#fonction determinant si la balle touche le bord bas de l'ecran 
def isOver(by) :
	touchingLowerCase = by > 500
	return touchingLowerCase
#fonction qui determine si c'est gagne
def win() :
	if len(lesBriques) == 0 :
		return True
	else :
		return False
#fonction determinant si la balle est lancee ou non
def estLancee(vvX,vvY) :
	if vvX != 0 or vvY != 0 :
		return True
	else :
		return False

#fonction affichant les vies restantes du joueur
def displayLifes(x,y,life) :
	vie = font.render("Vies restantes : " + str(life), True, black, white)
	window.blit(vie,(x,y))

#fonction affichant un message
def displayMessage(text, fontSize, x, y) :
	font = pygame.font.Font('BradBunR.ttf', fontSize)
	img = font.render(text, True, white)
	displayRect = img.get_rect()
	displayRect.center=(x,y)
	window.blit(img,displayRect)
	pygame.display.update()
#couleur noir
def displayMessageDeux(text, fontSize, x, y) :
	font = pygame.font.Font('BradBunR.ttf', fontSize)
	img = font.render(text, True, black)
	displayRect = img.get_rect()
	displayRect.center=(x,y)
	window.blit(img,displayRect)
	pygame.display.update()

#deuxieme fonction affichant un message
def displayTitleMessage(text, fontSize, x, y) :
	font = pygame.font.Font('BradBunR.ttf', fontSize)
	img = font.render(text, True, white)
	displayRect = img.get_rect()
	displayRect.center=(x,y)
	window.blit(img,displayRect)
	pygame.display.update()

#fonction permettant au joueur de rejouer
def playAgain() :
	time.sleep(2)
	while True :
		for event in pygame.event.get([pygame.KEYDOWN,pygame.QUIT]) :
			if event.type == pygame.QUIT :
				return False
			elif event.type == pygame.KEYDOWN :
				return True
		horloge.tick()

#fonction permettant d'afficher les briques
def displayBriques() :
        for i in lesBriques :
                pygame.draw.rect(window,black,[i[0],i[1],briqueW,briqueH])
		

#fonction contenant les composants de la page d'accueil du jeu
def accueil() :
	continuer = True
	global life
	life = 2
	global lesBriques
	lesBriques = []
	listei = (40,75,110,145)
	listej = (40,115,190,265)
	for i in listei:
                for j in listej:
                        lesBriques.append([j,i])

	while continuer:
		windowAccueil.blit(backgroundAcc,(0,0))
		displayTitleMessage("Jeu du casse brique", 60, windowW/2+150, windowH-600)
		displayMessageDeux("Jeu développé par PEDICONE Doucelin - GROLLIER Théo - BEN MOUSSA Aurian", 20, windowW/2+150, windowH-770)
		displayMessage("Appuyez sur espace pour lancer la partie", 30, windowW/2+150,windowH-530)
		displayMessage("[<-] pour deplacer la raquette a gauche et [->] pour la deplacer a droite",25,windowW/2+150,windowH-350)
		pygame.display.flip()
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				#game_over = True
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					main()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					continuer = False
					game_over = True


accueil()
pygame.quit()
quit()
