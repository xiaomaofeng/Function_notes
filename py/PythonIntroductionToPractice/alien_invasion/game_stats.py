class GameStats():
    """tracking game statistics"""

    def __init__(self,ai_settings):
        """initialize statistics infomation"""
        self.ai_setiings = ai_settings
        self.reset_stats()
        # the game is active when it just started
        self.game_active = True

    def reset_stats(self):
        """initialize possible changes statistical information in the game running period"""
        self.ships_left = self.ai_setiings.ship_limit