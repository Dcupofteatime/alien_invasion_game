import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Alien class"""

    def __init__(self, ai_settings, screen):
        """init alien and set the position """
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # upload alien image, setting its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # every alien are near left upper corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # save aliens correct position
        self.x = float(self.rect.x)

    def check_edges(self):
        """ if aliens over the edges return true """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """ move aliens to right """
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """ draw aliens in allocated position """
        self.screen.blit(self.image, self.rect)
