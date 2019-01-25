import pygame.sysfont
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """a class that display the score"""

    def __init__(self, ai_settings, screen, stats):
        """initialize the properity of the score"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #display the font settings about score
        self.text_color = (30, 30, 30)
        self.font =  pygame.font.SysFont("arial", 48)

        #ready score image for first use.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """transform score to a render image"""
        #score_str = str(self.stats.score)
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings)

        #set score in the upper right corner of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right =self.screen_rect.right -20
        self.score_rect. top = 20

    def show_score(self):
        """show score"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        #draw ship
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """transform the highest score to a render image"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        #set the highest score in the upper middle of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

        #write higi_score to file
        self.storage_score(str(high_score))

    def prep_level(self):
        """transform level to a render image"""
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)

        #put the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """display the remaining number of spacecraft """
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 +ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def storage_score(self, str):
        filename = 'high_score.txt'
        with open(filename, 'w') as file:
            file.write(str)



