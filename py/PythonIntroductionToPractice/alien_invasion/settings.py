class Settings():
    """storage all settings for alien_invasion"""
    def __init__(self):
        """initialize the game settings."""
        #screen settings.
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        #ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height =15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5

        #alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direction = 1 respresent moving to the right,and fleet_direction = -1 respresent moving to the left.
        self.fleet_direction = 1
