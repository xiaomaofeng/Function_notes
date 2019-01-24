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

        #speed up game thythm
        self.speedup_scale = 1.1

        #speed up aliens's point
        self.score_scale =1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize settings that change as the game progresses"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.alien_points = 50

        #fleet_directiong = 1 represent go to right, '-1' represent go the left
        self.fleet_direction = 1

    def increase_speed(self):
        """increse speed settings and aliens's point"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
