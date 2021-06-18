
from player import Player
from monster import Monster

import pygame

#class representele jeu
class Game:

	def __init__(self):
		#generation PJ
		self.all_players = pygame.sprite.Group()
		self.player = Player(self)
		self.all_players.add(self.player)
		self.all_monsters = pygame.sprite.Group()
		self.pressed = {
			"Touche_fleche_droite": True,
			"Touche_fleche_gauche": True,
			"Touche_fleche_haut": True,
			"Touche_fleche_bas": True,
        	}
		self.spawn_monster()
		self.spawn_monster()
		self.spawn_monster()
		
	def check_collision(self, sprite, group):
		return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
        
	def spawn_monster(self):
        	monster = Monster(self)
        	self.all_monsters.add(monster)
