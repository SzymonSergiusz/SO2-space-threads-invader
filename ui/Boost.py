import random
import threading

import pygame

import CONFIG
import SPRITES_CONFIG
from CONFIG import SCREEN_WIDTH, SCREEN_HEIGHT
from characters.Player import Player

UPGRADES_LIST = [
    'reload',
    'damage',
    'weapon_level',
    'capacity',
    'speed'
]


class Boost:
    def __init__(self):
        self.sprite = SPRITES_CONFIG.STAR
        x = SCREEN_WIDTH + random.randint(100, 300)
        y = random.randint(200, SCREEN_HEIGHT - self.sprite.get_height())
        self.rect = self.sprite.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.x -= 20
        self.rect.y -= random.randint(-1, 1) * 5

    def draw(self, screen):
        screen.blit(self.sprite, self.rect)

    def upgrade(self, player: Player):

        upgrade = random.choice(UPGRADES_LIST)

        match upgrade:
            case 'reload':
                player.reload_time /= 2
            case 'damage':
                player.damage += 1
            case 'capacity':
                player.ammo_capacity += 1
                player.ammo_limit_lock = threading.Semaphore(player.ammo_capacity)
            case 'weapon_level':
                player.weapon_level += 1
                if player.weapon_level == 2:
                    UPGRADES_LIST.remove('weapon_level')
            case 'speed':
                player.shot_speed += 2
            case _:
                pass

        player.reload_time /= 2

        return player, upgrade
