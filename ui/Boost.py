import random
import threading

import CONFIG
import SPRITES_CONFIG
from CONFIG import SCREEN_WIDTH, SCREEN_HEIGHT
from characters.Player import Player


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
        # player.reload_time /= 2
        # self.ammo_limit_lock = threading.Semaphore(CONFIG.AMMO_CAPACITY+3)
        return player