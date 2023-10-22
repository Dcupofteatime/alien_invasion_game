import pygame
class Ship():

    def __init__(self, ai_settings, screen):
        """ initiate ship and setting ship position """
        self.screen = screen
        self.ai_settings = ai_settings

        # load ship image and get square position
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put every new ship in the middle of the underneath screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store float number in ship center
        self.center = float(self.rect.centerx)

        # movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """move the ship with the movement flag """
        # refine the center, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # refine rect by self.center
        self.rect.centerx = self.center

    def center_ship(self):
        """ put the ship in the middle of the screen """
        self.center = self.screen_rect.centerx

    def blitme(self):
        """ draw ships at the pro-descript position """
        self.screen.blit(self.image, self.rect)
