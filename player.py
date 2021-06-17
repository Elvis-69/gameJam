import pygame
from projectile import Projectile

def load_image(name):
    image = pygame.image.load(name)
    return image

#classe joueur
class Player(pygame.sprite.Sprite):

		def __init__(self):
			super().__init__()
			self.health = 100
			self.max_health = 100
			self.attack = 10
			self.velocity = 5
			self.all_projectiles = pygame.sprite.Group(self)
			self.image = pygame.image.load('ressources/images/perso-10.png')


			self.rect = self.image.get_rect()
			self.rect.x = 400
			self.rect.y = 400

		def launch_projectile(self):
			#instance projectile
			self.all_projectiles.add(Projectile())

		def move_right(self):
			self.rect.x += self.velocity

		def move_left(self):
			self.rect.x -= self.velocity

		def move_up(self):
			self.rect.y -= self.velocity

		def move_down(self):
			self.rect.y += self.velocity






