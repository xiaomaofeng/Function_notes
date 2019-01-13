import sys
import pygame


def check_events(ship):
    """response key and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
            # # move ship to the right;
            #    ship.rect.centerx += 1
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """update the image from screen,and refresh"""
    # redraw the screen when goto loop;
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # display the lastest screen;
    pygame.display.flip()