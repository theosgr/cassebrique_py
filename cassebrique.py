import pygame
import time

pygame.init()

windowH = 800
windowW = 500
raquette = pygame.image.load('raquette/raquette.png')
background = (113,177,227)
window = pygame.display.set_mode((windowH,windowW))
pygame.display.set_caption("Casse-Brique")



def main() :
	
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
					dx += -2
				if event.key == pygame.K_RIGHT :
					moveRight = True
					dx += 2
			elif event.type == pygame.KEYUP :
				if event.key == pygame.K_LEFT :
					moveLeft = False
				if event.key == pygame.K_RIGHT :
					moveRight = False


		window.fill(background)
		pygame.display.update()


main()
pygame.quit()
quit()