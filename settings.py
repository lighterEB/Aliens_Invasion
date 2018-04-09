#coding:utf-8

class Settings():
    """存储《Alien Invasion》的所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (255,255,255)

        #飞船的设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 3

        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direction为1表示向右移动，-1表示向左移动
        self.fleet_direction = 1

        #以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

        #最高分
        f = open("history_high_score.txt","r")
        history_high_score = f.read()
        f.close()
        self.high_score = history_high_score

    def initialize_dynamic_settings(self):
        """初始化游戏动态设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.ship_limit = 3
        self.alien_speed_factor = 1
        self.alien_points = 50

        #fleet_direction为1表示向右；-1表示向左
        self.fleet_direction = 1

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

