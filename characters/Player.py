import threading

import pygame

import CONFIG
from CONFIG import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_LIVES
from SPRITES_CONFIG import SHOT_SPRITE, PLAYER_SPRITE
from characters.Projectiles import Shot, AnimatedShot


class Player:
    def __init__(self):
        self.lifes = PLAYER_LIVES
        self.sprite = PLAYER_SPRITE.convert_alpha()
        self.rect = self.sprite.get_rect(topleft=(50, SCREEN_HEIGHT // 2))
        self.shot_sprite = SHOT_SPRITE
        self.ammo_capacity = CONFIG.AMMO_CAPACITY
        self.ammo_limit_lock = threading.Semaphore(self.ammo_capacity)  # SEMAPHOORE
        self.reload_time = CONFIG.AMMO_RELOAD_TIME

        self.damage = 1
        self.weapon_level = 0
        self.shot_speed = CONFIG.SHOT_SPEED

    def shoot(self):

        match self.weapon_level:
            case 0:
                return [Shot(self.rect.midright, damage=self.damage, shot_speed=self.shot_speed)]
            case 1:
                return [Shot(self.rect.topright, 'top', damage=self.damage, shot_speed=self.shot_speed),
                        Shot(self.rect.bottomright, 'bottom', damage=self.damage, shot_speed=self.shot_speed)]
            case 2:
                return [Shot(self.rect.topright, 'top', y=2, damage=self.damage, shot_speed=self.shot_speed), Shot(self.rect.midright,
                                                                                       'mid', damage=self.damage, shot_speed=self.shot_speed),
                        Shot(self.rect.bottomright, 'bottom', y=2, damage=self.damage, shot_speed=self.shot_speed)]

            case _:
                return [Shot(self.rect.midright)]

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
