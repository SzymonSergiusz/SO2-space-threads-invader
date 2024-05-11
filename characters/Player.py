import pygame

from CONFIG import SCREEN_HEIGHT, SHOT_SPRITE, SCREEN_WIDTH, PLAYER_SPRITE, PLAYER_LIVES


class Player:
    def __init__(self):
        self.lifes = PLAYER_LIVES

        self.sprite = PLAYER_SPRITE.convert_alpha()
        self.rect = self.sprite.get_rect(topleft=(50, SCREEN_HEIGHT // 2))
        self.shot_sprite = SHOT_SPRITE

    def shot(self):
        return self.shot_sprite

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
