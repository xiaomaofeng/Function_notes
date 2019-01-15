import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien  import Alien
from game_stats import GameStats

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

    #create an object use to storage the statistical imformation
    stats = GameStats(ai_settings)

    #create a ship, a bullet group and a alien group
    #create a ship
    ship = Ship(ai_settings, screen)
    #create a group to storage bullet
    bullets = Group()
    aliens =Group()

    #create alien object
    #alien = Alien(ai_settings, screen)
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #start the game main loop.
    while True:
        #Monitor the keyboard and mouse event.

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        if stats.game_active:
            # center = ship.center
            # cenerx = ship.rect.centerx
            #redraw srcreen
            # screen.fill(ai_settings.bg_color)
            # ship.blitme()
            #
            # #display the screen which was drew recently.
            # pygame.display.flip()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            # bullets.update()
            # #delete missing bullets
            # #for bullet in bullets:
            # for bullet in bullets.copy():
            #     if bullet.rect.bottom <= 0:
            #         bullets.remove(bullet)
            #print(len(bullets))
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
