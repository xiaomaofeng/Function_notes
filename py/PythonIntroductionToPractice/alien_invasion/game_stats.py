class GameStats():
    """tracking game statistics"""

    def __init__(self,ai_settings):
        """initialize statistics infomation"""
        self.ai_setiings = ai_settings
        self.reset_stats()
        # the game is inactive when it just started
        self.game_active = False
        #under no circumstances should the highest score be reset
        self.high_score = 0
        self.level = 1

    def reset_stats(self):
        """initialize possible changes statistical information in the game running period"""
        self.ships_left = self.ai_setiings.ship_limit
        self.score = 0