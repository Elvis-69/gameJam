import pygame
pygame.init()
from game import Game

#fenetre du jeu
pygame.display.set_caption("psycoatak")
screen = pygame.display.set_mode((1000,1000))

# arriere plan
background = pygame.image.load('ressources/images/plage_sable.jpg')

#charger PJ
game = Game()

running = True

#boucle pour laisser la fenetre ouverte

currentFrame = 'ressources/images/perso-10.png'

while running:
	#appliquer l'arriere plan
	screen.blit(background, (0, 0))

	# appliquer joueur
	
	allFrame = pygame.image.load(currentFrame)
	
	screen.blit(allFrame, game.player.rect)
	if (currentFrame == 'ressources/images/perso-10.png'):
        	currentFrame = 'ressources/images/persoB-10.png'

	else:
        	currentFrame = 'ressources/images/perso-10.png'
        	
	pygame.display.update()
	
	screen.blit(game.player.image, game.player.rect)


	# Recuperer les projectiles du player
	for projectile in game.player.all_projectiles:
		projectile.move()
		
	#image projectile (appliquer l'ensemble des images du groupe)	
	game.player.all_projectiles.draw(screen)

	# verifier direction PJ
	if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
		game.player.move_right()

	if game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
		game.player.move_left()

	if game.pressed.get(pygame.K_UP) and game.player.rect.y > 0:
		game.player.move_up()

	if game.pressed.get(pygame.K_DOWN) and game.player.rect.y + game.player.rect.width < screen.get_width():
		game.player.move_down()



	#mettre l'ecran an jour
	pygame.display.flip()

	#si le joueur ferme cette fenetre
	for event in pygame.event.get():
		# evenement et fermeture fenetre
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			print("fermeture du jeux")

		#detection que le joueur lache les touche
		elif event.type == pygame.KEYDOWN:
			game.pressed[event.key] = True

			#detecter espace
			if event.key == pygame.K_SPACE:
				game.player.launch_projectile()

		elif event.type == pygame.KEYUP:
			game.pressed[event.key] = False


