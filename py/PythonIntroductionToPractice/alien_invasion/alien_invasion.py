import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # screen = pygame.display.set_mode((1200,800))
    #
    # #set the background color
    # bg_color = (230, 230, 230)

    pygame.display.set_caption("Alien Invasion")

    #create a ship
    ship = Ship(ai_settings, screen)

    #start the game main loop.
    while True:
        #Monitor the keyboard and mouse event.

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gf.check_events(ship)
        ship.update()
        # center = ship.center
        # cenerx = ship.rect.centerx

        #redraw srcreen
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
        #
        # #display the screen which was drew recently.
        # pygame.display.flip()
        gf.update_screen(ai_settings, screen, ship)

run_game()
