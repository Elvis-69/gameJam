import pygame
import random

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