import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    
    def __init__(self, ai_game):
        """Create a bullet objet"""
        super().__init__()
        self.screen =ai_game.screen
        self.settings =ai_game.settings
        self.color =self.settings.bullet_color

        #create a bullet rect
        self.rect =pygame.Rect(0,0, self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop= ai_game.ship.rect.midtop

        #store the bullet's position
        self.y=float(self.rect.y)

    def update(self):
        """move the bullet"""
        #update decimal position
        self.y -= self.settings.bullet_speed
        #update rect position
        self.rect.y =self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

