import random

import pygame
import CONFIG
import SPRITES_CONFIG
from SPRITES_CONFIG import SHOT_SPRITE, ENEMY_SHOT_SPRITE

class Shot:
    def __init__(self, pos, position='', y=0, damage=0, shot_speed = CONFIG.SHOT_SPEED):
        self.damage = damage
        if self.damage > 2:
            self.sprite = SPRITES_CONFIG.UPGRADED_SHOT1
        else:
            self.sprite = SHOT_SPRITE
        self.rect = self.sprite.get_rect(center=pos)
        self.speed = shot_speed
        self.position = position
        self.y = y

    import random
    def update(self):
        if self.damage > 2:
            self.sprite = random.choice([SPRITES_CONFIG.UPGRADED_SHOT1, SPRITES_CONFIG.UPGRADED_SHOT2])
        match self.position:
            case 'top':
                self.rect.x += self.speed
                self.rect.y -= self.y
            case 'mid':
                self.rect.x += self.speed
            case 'bottom':
                self.rect.x += self.speed
                self.rect.y += self.y
            case _:
                self.rect.x += self.speed

class AnimatedShot(Shot):
    def __init__(self, pos, position='', y=0):
        super().__init__(pos, position, y)
        self.current_frame = 0
        self.animation_frames = SPRITES_CONFIG.UPGRADED_SHOT_FRAMES
        self.sprite = self.animation_frames[self.current_frame]
        self.animation_speed = 0.1
        self.animation_timer = 0

    def update(self):
        super().update()
        self.animation_timer += self.animation_speed
        if self.animation_timer >= 1:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.animation_frames)
            self.sprite = self.animation_frames[self.current_frame]


class EnemyShot:
    def __init__(self, pos):
        self.sprite = ENEMY_SHOT_SPRITE
        self.rect = self.sprite.get_rect(center=pos)
        self.speed = CONFIG.SHOT_SPEED

    def update(self):
        self.rect.x -= self.speed