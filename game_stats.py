class GameStats():
    """ track the game statistics information """
    def __init__(self, ai_settings):
        """ initiate the statistics information """
        self.ai_setting = ai_settings
        self.reset_stats()
        # set the game_active False in the game start
        self.game_active = False

    def reset_stats(self):
        """ initiate changeable statistics information """
        self.ships_left = self.ai_setting.ship_limit
        self.score = 0
        
