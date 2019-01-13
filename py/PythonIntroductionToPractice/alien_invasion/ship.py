import pygame
class Ship():
    def __init__(self, ai_settings, screen):
        """initialize snip and set its initital positon"""
        self.screen = screen
        self.ai_settings = ai_settings

        #loading snip picture and get its external rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #set every ship in the bottom center center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center =float(self.rect.centerx)

        #moving flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #change ship's positon based on moving flag;

        # if self.moving_right:
        #     self.rect.centerx += 1
        # if self.moving_left:
        #     self.rect.centerx -= 1

        #update the center value,rather than rect.
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor

        #update rect object based on self.center
        self.rect.centerx = self.center



    def blitme(self):
        """draw snip in designated location"""
        self.screen.blit(self.image, self.rect)
