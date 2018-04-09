# coding:utf-8

import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard


def run_game():
    #初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                       ai_settings.screen_height))
    pygame.display.set_caption("外星人入侵！             Author: Cheng_CN")
    #创建按钮
    play_button = Button(ai_settings, screen, u"开始游戏")
    #创建存储游戏统计信息的实例，并创建计分牌
    stats = GameStats(ai_settings)
    sb = ScoreBoard(ai_settings, screen, stats)
    #创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    ships = Group()
    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    gf.ship_lefts(ai_settings, stats, screen, ships)


    #开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, ships, aliens, bullets)
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, ships, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, ships, aliens, bullets,
                        play_button)
run_game()
