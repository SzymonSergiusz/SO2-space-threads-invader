import random

from CONFIG import SCREEN_WIDTH, SCREEN_HEIGHT
from SPRITES_CONFIG import ENEMY_LIST
from characters.Projectiles import EnemyShot

ENEMY_BORDER_X = SCREEN_WIDTH // 3
ENEMY_BORDER_Y = SCREEN_HEIGHT // 3
ENEMY_BORDER_RIGHT = SCREEN_WIDTH-100
ENEMY_BORDER_LEFT = SCREEN_WIDTH - ENEMY_BORDER_X
class Enemy:
    def __init__(self):
        sprite, self.lifes, self.speed = random.choice(ENEMY_LIST)
        self.sprite = sprite
        self.rect = self.sprite.get_rect()
        x = SCREEN_WIDTH + random.randint(10, 50)
        y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
        self.rect.topleft = (x, y)

        self.horizontal_direction = 'LEFT'
        self.vertical_direction = random.choice([-1, 1])
        self.arrived = False
    def shoot(self):
        return EnemyShot(self.rect.midleft)

    def update(self):

        if (not (ENEMY_BORDER_LEFT <= self.rect.x <= ENEMY_BORDER_RIGHT)) and self.arrived:
            if self.rect.x <= ENEMY_BORDER_LEFT:
                self.horizontal_direction = 'RIGHT'
            elif self.rect.x >= ENEMY_BORDER_RIGHT:
                self.horizontal_direction = 'LEFT'
            self.vertical_direction = random.choice([-1, 1])
        if self.rect.x <= SCREEN_WIDTH-100:
            self.arrived = True
        # ruch w poziomie
        if self.horizontal_direction == 'LEFT':
            self.rect.x -= self.speed
        elif self.horizontal_direction == 'RIGHT':
            self.rect.x += self.speed

        # ruch w pionie
        if self.rect.y <= 50 or self.rect.y >= SCREEN_HEIGHT-50:
            self.vertical_direction *= -1
        self.rect.y += self.speed * self.vertical_direction

    def draw(self, screen):
        screen.blit(self.sprite, self.rect)