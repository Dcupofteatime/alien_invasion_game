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

    def blitme(self):
        """ draw aliens in allocated position """
        self.screen.blit(self.image, self.rect)
