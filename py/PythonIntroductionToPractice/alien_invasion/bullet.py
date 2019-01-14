import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """a class designer for managing bullet"""

    def __init__(self, ai_settings, screen, ship):
        """create a bullet object in the ship's positon"""
        super(Bullet, self).__init__()
        self.screen =screen

        #create a rect for bullte in (0, 0),and set it's position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #storage bullet in float
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """move bullet up"""
        #update bullet position
        self.y -= self.speed_factor
        #update bullet's rect position
        self.rect.y =self.y

    def draw_bullet(self):
        """draw bullet in screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)