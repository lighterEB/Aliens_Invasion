
#coding:utf-8

import pygame.font

class ScoreBoard():
    """显示得分信息的类"""

    def __init__(self, ai_settings, screen, stats):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont('SimHei',15)

        #准备初始得分图像和最高分图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        """将得分转换为一幅渲染的图像"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{}:{:,}".format("分数",rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)

        #将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = self.screen_rect.top

    def prep_high_score(self):
        """将最高分转换为一幅渲染的图像"""
        rounded_score = int(round(int(self.ai_settings.high_score), -1))
        high_score_str = "{}:{:,}".format("历史最高分",rounded_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color,
                                            self.ai_settings.bg_color)
        #将得分放在屏幕中间顶部
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def prep_level(self):
        """等级渲染图像"""
        rounded_score = int(self.stats.level)
        level_str = "{}:{:}".format("等级",rounded_score)
        self.level_image = self.font.render(level_str, True, self.text_color,
                                            self.ai_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = 20

    def show_score(self):
        """在屏幕上显示分数和等级"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)