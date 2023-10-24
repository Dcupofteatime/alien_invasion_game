class Settings():
    """ store alien_invasion's every setting """

    def __init__(self):
        """ initiate game setting """
        # screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship setting
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # bullet setting
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        # aliens setting
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction 1 for right, -1 for left
        self.fleet_direction = 1

        # find a way to accelerate the game speed
        self.speedup_scale = 1.1

        # increase the score of the aliens
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ initiate the settings by game develop """
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction 1 for right, -1 for left
        self.fleet_direction = 1

        # score
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
