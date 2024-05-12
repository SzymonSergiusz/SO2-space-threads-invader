import random

from CONFIG import SCREEN_WIDTH, SCREEN_HEIGHT


class BackgroundItems:
    def __init__(self, planet_sprite):
        self.sprite = planet_sprite
        x = SCREEN_WIDTH + random.randint(100, 300)
        y = random.randint(200, SCREEN_HEIGHT - self.sprite.get_height())
        self.rect = self.sprite.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.x -= 5

    def draw(self, screen):
        screen.blit(self.sprite, self.rect)
