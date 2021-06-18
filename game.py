import pygame
import random
from player import Player
from sounds import SoundManager

import pygame

#class representele jeu
class Game:

	def __init__(self):
		#generation PJ
		self.all_players = pygame.sprite.Group()
		self.player = Player(self)
		self.all_players.add(self.player)
		# groupe de monstres
		self.all_monsters = pygame.sprite.Group()
		# gerer le son
		self.sound_manager = SoundManager()
		
		self.pressed = {
			"Touche_fleche_droite": True,
			"Touche_fleche_gauche": True,
			"Touche_fleche_haut": True,
			"Touche_fleche_bas": True,
        	}
		self.spawn_monster()
		self.spawn_monster()
		self.spawn_monster()
		self.spawn_monster()
		self.spawn_monster()
		
	def check_collision(self, sprite, group):
		return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
        
	def spawn_monster(self):
        	monster = Monster(self)
        	self.all_monsters.add(monster)
        	
class Monster(pygame.sprite.Sprite):

	def __init__(self, game):
		super().__init__()
		self.game = game
		self.health = 1
		self.max_health = 1
		self.attack = 1
		self.image = pygame.image.load('ressources/images/Spectrum.png')
		self.image = pygame.transform.scale(self.image, (107, 93))

		self.rect = self.image.get_rect()
		self.rect.x = 1000 + random.randint(0, 400)
		self.rect.y = 100 + random.randint(0, 700)
		self.velocity = 1 + random.randint(0, 2)
		
	def damage(self, amount):
#		if self.health - amount > amount:
		self.health -= amount
		
		# Verifier si vie <= 0
		if self.health <= 0 :	
			#game = Game()
			#game.sound_manager.play('mort')	
			# reapparait comme nouveau monstre
			self.rect.x = 1000 + random.randint(0, 100)
			self.rect.y = 100 + random.randint(0, 700)
			self.velocity = 1 + random.randint(0, 2)
			self.health = self.max_health
		
	def forward(self):
		
		if self.rect.left <= 0 :
			self.rect.x = 1000 + random.randint(0, 100)
			self.rect.y = 100 + random.randint(0, 700)
			self.velocity = 1 + random.randint(0, 2)
			self.health = self.max_health
		# si collision : pas de deplacement
		if not self.game.check_collision(self, self.game.all_players):
			self.rect.x -= self.velocity
#		else :
#			self.game.player.damage(self.attack)
