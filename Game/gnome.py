import pygame
from pygame.sprite import Sprite

class Gnome(Sprite):
    """A class to represent the alien and set its rect attribute"""
    def __init__(self, gp_game):
        super().__init__()
        self.screen =gp_game.screen
        self.settings =gp_game.settings

        #load the alien image
        self.image =pygame.image.load('media/gnome.png')
        self.rect= self.image.get_rect()

        #start each new alien near top of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alien's exact horizontal pos
        self.x =float(self.rect.x)

    def update(self):
        """Move the gnome right or left."""
        self.x +=(self.settings.gnome_speed *self.settings.army_direction)
        self.rect.x =self.x
    
    def check_edges(self):
        """return True is gnome is at edge of screen"""
        screen_rect=self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

        



