import pygame
#from projectile import Projectile

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
		self.all_projectiles = pygame.sprite.Group()
		
		self.image = pygame.image.load('ressources/images/persoA-10.png')

		self.rect = self.image.get_rect()
		self.rect.x = 400
		self.rect.y = 400
			
			
	def launch_projectile(self):
		#instance projectile
		self.all_projectiles.add(Projectile(self))

	def move_right(self):
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
		
		# Verifier si projectile n'est plus sur l'écran
		if self.rect.x > 1080:
			# Supprimer le projectile
			self.remove()
			
	
"""-----------------------------------------------------------------------------

		
	def __init__(self, posx_end, posy_end):
		
		pygame.sprite.Sprite.__init__(self) 
		self.image = pygame.image.load('ressources/images/tirAqua.png')
		player = Player()
		self.posx_end = posx_end
		self.posy_end = posy_end
		self.step = 5

		self.longx = self.posx_end - player.get_posx()
		self.longy = self.posy_end - player.get_posy()
		
		self.rect = self.image.get_rect()
		self.rect.x = player.get_posx()
		self.rect.y = player.get_posy()


	def compute_new_pos(self):
		""" """Mets les positions du projectile à jour sur le segment entre
		     sur le segment entre le joueur et la souris""""""
		self.posx += self.step*math.cos(math.atan2(self.longy, self.longx))
		self.posy += self.step*math.sin(math.atan2(self.longy, self.longx))
		self.ttl += 1
		print("Compute position projectile")
		return self.posx, self.posy

	def draw(self, screen):
		""" """Dessine le projectile sur la surface""" """
		print("Drawing new projectile")
		screen.blit(self.image, self.compute_new_pos())"""

    






