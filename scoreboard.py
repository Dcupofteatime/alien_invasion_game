import pygame.font


class Scoreboard():
    """ the class to show the score """

    def __init__(self, ai_settings, screen, stats):
        """ initiate the properties of the related """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # set the font and fontsize for the score
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # prepare the initiation image for the game start
        self.prep_score()

    def prep_score(self):
        """ change the score to the rendered image """
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # put the image to the right upside in the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """ show the score on the screen """
        self.screen.blit(self.score_image, self.score_rect)
