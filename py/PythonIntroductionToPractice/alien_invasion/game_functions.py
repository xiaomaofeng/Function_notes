import sys
from time import sleep
import pygame

from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """response key down"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        # create a bullet,and put it in group
        # if len(bullets) < ai_settings.bullets_allowed:
        #     new_bullet = Bullet(ai_settings, screen, ship)
        #     bullets.add(new_bullet)
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """response key up"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """response key and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

        elif event.type == pygame.KEYDOWN:
            # # # move ship to the right;
            # #    ship.rect.centerx += 1
            #     ship.moving_right = True
            # elif event.key == pygame.K_LEFT:
            #     ship.moving_left = True
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            # if event.key == pygame.K_RIGHT:
            #     ship.moving_right = False
            # elif event.key == pygame.K_LEFT:
            #     ship.moving_left = False
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """update the image from screen,and refresh"""
    # redraw the screen when goto loop;
    screen.fill(ai_settings.bg_color)

    # redraw all bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # alien.blitme()
    aliens.draw(screen)

    #display score
    sb.show_score()

    # if game is in the inactivity, draw the 'play' button
    if not stats.game_active:
        play_button.draw_button()

    # display the lastest screen;
    pygame.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """update bullets positon and delete missing bullets"""
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen,stats, sb, ship, aliens, bullets):
    """check for bullets hitting aliens"""
    # if Ture, delete bullet and aliens
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # delete existing bullets and create a new group aliens
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)

        #increase level
        stats.level += 1
        sb.prep_level()



def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """cal how many alien can be set in a lines"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """cal the whole screen can contain the lines can storage aliens."""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # creat an alien,and cal how many alien can be set in a row
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    # create alien group
    # alien's spacing is alien's width
    alien = Alien(ai_settings, screen)
    # alien_width =alien.rect.width
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # create aliens group
    for row_number in range(number_rows):
        # create a lines of aliens
        for alien_number in range(number_aliens_x):
            # create an alien and jion it in current lines.
            # alien = Alien(ai_settings, screen)
            # alien.x = alien_width + 2 * alien_width * alien_number
            # alien.rect.x = alien.x
            # aliens.add(alien)
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """take action when alien reach the edge of the screen"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """the whole rows alines move down,and change its direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """response the ship hit by aliens"""
    if stats.ships_left > 0:
        # reduce ships_left by one
        stats.ships_left -= 1

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

    # clear all aliens and bullets
    aliens.empty()
    bullets.empty()

    # create a new group of aliens, and put the ship in the bottom of the screen.
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

    # pause
    sleep(0.5)


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """check for aliens reach the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            """handel as if a spaceship had been hit."""
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    # check whether if have aliens located the edge of the screen, and update the aliens position
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # check ship's collision with aliens
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    """check for aliens reach the bottom of the screen"""
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """start play game when the player click the button"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #reset game settings
        ai_settings.initialize_dynamic_settings()
        # set the mouse invisible
        pygame.mouse.set_visible(False)

        # reset game statistic information
        stats.reset_stats()
        stats.game_active = True

        #reset score image
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()

        # clear alien and bullet list
        aliens.empty()
        bullets.empty()

        # create a new group aliens, and set the ship in the middle of tht screen
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def check_high_score(stats, sb):
    """check if a new top score is born"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
