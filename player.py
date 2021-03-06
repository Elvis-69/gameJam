import pygame

def load_image(name):
    image = pygame.image.load(name)
    return image

#classe joueur
class Player(pygame.sprite.Sprite):

	def __init__(self, game):
		super().__init__()
		self.game = game
		self.health = 1
		self.max_health = 1
		self.attack = 1
		self.velocity = 5
		self.all_projectiles = pygame.sprite.Group()
		
		self.image = pygame.image.load('ressources/images/persoA-10.png')

		self.rect = self.image.get_rect()
		self.rect.x = 400
		self.rect.y = 400
			
#	def damage(self, amount):
#		self.health -= amount
#	
#		# Verifier si vie <= 0
#		if self.health <= 0 :
			# reapparait comme nouveau monstre
#			self.rect.x = 1000 + random.randint(0, 100)
#			self.rect.y = 100 + random.randint(0, 700)
#			self.health = self.max_health
				
	def launch_projectile(self):
		#instance projectile
		self.all_projectiles.add(Projectile(self))

	def move_right(self):
		# Si pas de collision monstre/player
		if not self.game.check_collision(self, self.game.all_monsters):
			self.rect.x += self.velocity

	def move_left(self):
		self.rect.x -= self.velocity

	def move_up(self):
		self.rect.y -= self.velocity

	def move_down(self):
		self.rect.y += self.velocity
			
"""----------------------------------------------------------------------------------------"""

#class projectile
class Projectile(pygame.sprite.Sprite):



	#constructeur de la class
	def __init__(self, player):
		super().__init__()
		self.velocity = 5
		self.player = player
		self.image =pygame.image.load('ressources/images/tirAqua.png')
		self.rect = self.image.get_rect()
		self.rect.x = player.rect.x +100
		self.rect.y = player.rect.y +60
	
	def remove(self):
		self.player.all_projectiles.remove(self)
		
				
	def move(self) :
		self.rect.x += self.velocity
		
		# collision avec monstre
		for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
			# suppression projectile
			self.remove()
			# infliger dégats
			monster.damage(self.player.attack)
		
		# Verifier si projectile n'est plus sur l'écran
		if self.rect.x > 1080:
			# Supprimer le projectile
			self.remove()
			






