class Alien:
	def __init__(self, game, x, y):
		self.x = x
		self.game = game
		self.y = y
		
	def draw(self):
		pygame.draw.rect(self.game.screen, (81, 43, 88), pygame.Rect(self.x, self.y, 30, 30))
		self.y += 0.05
		
alien = Alien(self, 30, 30)

alien.draw()
		
