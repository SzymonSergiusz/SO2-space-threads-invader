import pygame


class Level:
    def __init__(self, level_number,background, points_to_boss, boss_class):
        self.background = background
        self.points_to_boss = points_to_boss
        self.boss_class = boss_class
        self.level_number = level_number