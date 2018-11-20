import pygame
import time

pygame.init()

windowH = 800
windowW = 500
raquette = pygame.image.load('raquette/raquette.png')
raquetteW = 204
raquetteH = 24
background = (113,177,227)
window = pygame.display.set_mode((windowH,windowW))
pygame.display.set_caption("Casse-Brique")



def main() :
	raquetteX = 400
	raquetteY = 470
	game_over = False
	moveLeft = False
	moveRight = False
	dx = 0
	while not game_over :
		for event in pygame.event.get() :
			if event.type == pygame.QUIT :
				game_over = True
			#Mouvement raquette
			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_LEFT :
					moveLeft = True
					dx = -2
				if event.key == pygame.K_RIGHT :
					moveRight = True
					dx = 2
			elif event.type == pygame.KEYUP :
				if event.key == pygame.K_LEFT :
					moveLeft = False
				if event.key == pygame.K_RIGHT :
					moveRight = False


		window.fill(background)
		displayRaquette(raquetteX,raquetteY)
		pygame.display.update()

		if raquetteX - raquetteW/2 == 0:
			dx = 2
		if raquetteX + raquetteW/2 == 800:
			dx = -2
		raquetteX += dx

def displayRaquette(x,y) :
	img = raquette
	displayRect = img.get_rect()
	displayRect.center = (x,y)
	window.blit(img,displayRect)
	pygame.display.update()

main()
pygame.quit()
quit()
