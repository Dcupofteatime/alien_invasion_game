import sys

import pygame

from game_stats import GameStats
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

    # create a flag to save statistics information
    stats = GameStats(ai_settings)

    # new a ship
    ship = Ship(ai_settings, screen)
    # new a bullet
    bullets = Group()
    # new an alien
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        # print(len(bullets)) test the remove work

        # # reform screen every times
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
        # change to use game_function
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        # 让最近绘制的屏幕可见
        pygame.display.flip()


run_game()
