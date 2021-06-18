import pygame

class SoundManager:

	def __init__(self):
		self.sounds = {
			'zik': pygame.mixer.Sound("ressources/sons/poke.ogg"),
			'tir': pygame.mixer.Sound("ressources/sons/water.ogg"),
			'mort': pygame.mixer.Sound("ressources/sons/spectrum.ogg")
		}
		
	def play(self, name):
		self.sounds[name].play()
