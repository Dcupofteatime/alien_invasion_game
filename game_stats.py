class GameStats():
    """ track the game statistics information """
    def __init__(self, ai_settings):
        """ initiate the statistics information """
        self.ships_left = None
        self.ai_setting = ai_settings
        self.reset_stats()
        # game_active in the
        self.game_active = True

    def reset_stats(self):
        """ initiate changeable statistics information """
        self.ships_left = self.ai_setting.ship_limit
