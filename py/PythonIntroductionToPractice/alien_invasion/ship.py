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

        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        #moving flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        #change ship's positon based on moving flag;


        # if self.moving_right:
        #     self.rect.centerx += 1
        # if self.moving_left:
        #     self.rect.centerx -= 1

        #update the center value,rather than rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.bottom -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_settings.ship_speed_factor

        #update rect object based on self.center
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom



    def blitme(self):
        """draw snip in designated location"""
        self.screen.blit(self.image, self.rect)
