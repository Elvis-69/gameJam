import pygame

#class projectile
class Projectile(pygame.sprite.Sprite):

    #constructeur de la class
    def __init__(self):
        super().__init__()
        self.velocyty = 5
        self.image =pygame.image.load('ressources/images/tir.png')
        self.rect = self.image.get_rect()
