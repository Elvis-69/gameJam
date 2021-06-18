import pygame

#class projectile
class Projectile(pygame.sprite.Sprite):


	#constructeur de la class
	"""def __init__(self):
		super().__init__()
		self.velocity = 5
		self.image =pygame.image.load('ressources/images/tirAqua.png')
		self.rect = self.image.get_rect()

-----------------------------------------------------------------------------"""
		
	def __init__(self, posx_end, posy_end):	
		player = Player()
		pygame.sprite.Sprite.__init__(self) 
		self.image = pygame.image.load('ressources/images/tirAqua.png')
		self.posx_end = posx_end
		self.posy_end = posy_end
		self.step = 5

		self.longx = self.posx_end - player.get_posx()
		self.longy = self.posy_end - player.get_posy()

	def compute_new_pos(self):
		""" Mets les positions du projectile à jour sur le segment entre
		     sur le segment entre le joueur et la souris"""
		self.posx += self.step*math.cos(math.atan2(self.longy, self.longx))
		self.posy += self.step*math.sin(math.atan2(self.longy, self.longx))
		self.ttl += 1
		print("Compute position projectile")
		return self.posx, self.posy

	def draw(self, screen):
		""" Dessine le projectile sur la surface """
		print("Drawing new projectile")
		screen.blit(self.image, self.compute_new_pos())

    
	

		
