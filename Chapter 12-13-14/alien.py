import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent the alien and set its rect attribute"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen =ai_game.screen
        self.settings =ai_game.settings

        #load the alien image
        self.image =pygame.image.load('images/alien.bmp')
        self.rect= self.image.get_rect()

        #start each new alien near top of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alien's exact horizontal pos
        self.x =float(self.rect.x)

    def update(self):
        """Move the alien right or left."""
        self.x +=(self.settings.alien_speed *self.settings.fleet_direction)
        self.rect.x =self.x
    
    def check_edges(self):
        """return True is alien is at edge of screen"""
        screen_rect=self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

        



