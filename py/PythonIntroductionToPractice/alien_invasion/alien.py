import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """a class represent alien"""

    def __init__(self, ai_settings, screen):
        """initialize alien and set its starting positon"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load alien image, and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #every alien appear in the upper left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #storage alien's accuarte position
        self.x = float(self.rect.x)

    def blitme(self):
        """draw alien in the designated position"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """if alien is located at the edge of the screen, return true"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """move aliens to the right or left"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
