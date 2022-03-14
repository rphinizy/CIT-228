import pygame
from pygame.sprite import Sprite
import random

class Meteor(Sprite):
    """A class to represent the alien and set its rect attribute"""
    def __init__(self, gp_game):
        super().__init__()
        self.screen =gp_game.screen
        self.settings =gp_game.settings

        #load the alien image
        self.image =pygame.image.load('media/meteor.png')
        
        self.rect= self.image.get_rect()
        
        self.meteor_y_loc = [200, 300, 400,700, 800, 900, 1000]
        #start each new alien near top of screen

        self.rect.x = self.meteor_y_loc[random.randint(0,6)]
        self.rect.y = 525

        


        



