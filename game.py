import pygame
from player import Player

#class representele jeu
class Game:

	def __init__(self):
		#generation PJ
		self.player = Player()
		self.pressed = {
			"Touche_fleche_droite": True,
			"Touche_fleche_gauche": True,
			"Touche_fleche_haut": True,
			"Touche_fleche_bas": True,
        }