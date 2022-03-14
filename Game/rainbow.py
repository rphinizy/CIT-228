import pygame
from pygame.sprite import Sprite

class Rainbow(Sprite):
    """Class to manage ranbow shots"""
    def __init__(self, gp_game):
        """create rainbow object"""
        super().__init__()
        self.screen = gp_game.screen
        self.settings =gp_game.settings
        self.screen_rect =gp_game.screen.get_rect()
        #create rainbow rect at (0,0) then set correct position
        self.image =pygame.image.load('media/star.png')
        self.rect =self.image.get_rect()
        self.rect.midtop =gp_game.player.rect.midtop

        #store the rainbow value as a decimal value
        self.y =float(self.rect.y)

    def update(self):
        """Move the rainbow up the screen."""
        #update the decimal position of the rainbow.
        self.y -= self.settings.rainbow_speed
        #upate the rect position
        self.rect.y =self.y

    def blitme(self):
        """Draw the rainbow to the screen"""
        self.screen.blit(self.image, self.rect)


