import pygame
class Ship():
    def __init__(self,screen):
        """initialize snip and set its initital positon"""
        self.screen = screen

        #loading snip picture and get its external rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #set every ship in the bottom center center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """draw snip in designated location"""
        self.screen.bit(self.image, self.rect)
