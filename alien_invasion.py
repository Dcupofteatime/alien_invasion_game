import sys

import pygame

from alien import Alien
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # new a ship
    ship = Ship(ai_settings, screen)
    # new a bullet
    bullets = Group()
    # new an alien
    alien = Alien(ai_settings, screen)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        # print(len(bullets)) test the remove work

        # # reform screen every times
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
        # change to use game_function
        gf.update_screen(ai_settings, screen, ship, alien, bullets)

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
