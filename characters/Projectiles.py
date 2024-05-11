import pygame

from CONFIG import SHOT_SPRITE, ENEMY_SHOT_SPRITE

# TODO dać do klas które z nich korzystają?
class Shot:
    def __init__(self, pos):
        self.sprite = SHOT_SPRITE
        self.rect = self.sprite.get_rect(center=pos)

    def update(self):
        self.rect.x -= 10

class PlayerShot(Shot):
    def update(self):
        self.rect.x -= 10
class EnemyShot(Shot):
    def __init__(self, pos):
        self.sprite = ENEMY_SHOT_SPRITE
        self.rect = self.sprite.get_rect(center=pos)
