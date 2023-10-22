import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """ a class abut ship bullets """

    def __init__(self, ai_settings, screen, ship):
        """ creat a bullet in ship's position """
        super(Bullet, self).__init__()
        self.screen = screen

        # create a rectangle as bullets, and setting right position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store bullets position by float
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """move bullets up """
        # update the bullets position in float
        self.y -= self.speed_factor
        # update the bullets' rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """ draw bullets on screen """
        pygame.draw.rect(self.screen, self.color, self.rect)
