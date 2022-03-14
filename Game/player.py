import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    """A class to mamage the player"""
    def __init__(self, gp_game):
        super().__init__()
        """Initialize the player at the starting location"""
        self.screen = gp_game.screen
        self.screen_rect =gp_game.screen.get_rect()
        self.settings =gp_game.settings
        #load the player image and get its rect.
        imageLEFT=pygame.image.load('media/unicornleft.png')
        imageRIGHT=pygame.image.load('media/unicornright.png')
        self.image=imageLEFT
        self.rect =self.image.get_rect()

        #start player at the bottom center of screen.
        self.rect.midbottom =(600, 600)

        #movement flag
        self.moving_right =False
        self.moving_left =False
        self.jump_up =False
        self.fall_down =False
        self.count =self.rect.height/1.2

    def blitme(self):
        """Draw the player at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update player position"""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x +=1
            self.image=pygame.image.load('media/unicornright.png')

        if self.moving_left and self.rect.left >0:
            self.rect.x -=1
            self.image=pygame.image.load('media/unicornleft.png')
        
        if self.jump_up:
            while self.count >0:
                self.rect.y -=1
                self.count -=1
   
        if self.fall_down:
            while self.count <self.rect.height/1.2:
                self.rect.y +=1
                self.count +=1
    
    def center_player(self):
        #fixed bug where player hit while jumpng caused player to respawn lower than the default position
        if self.jump_up == True:
            self.rect.midbottom =(600,600 -self.rect.height/1.2)
            self.jump_up = False
        else:
            self.rect.midbottom =(600,600)