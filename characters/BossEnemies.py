import random

import CONFIG
from CONFIG import SCREEN_WIDTH, SCREEN_HEIGHT, SPACE_DRAGON_SHOT0, SPACE_DRAGON_SHOT1, SPACE_DRAGON_SHOT2, SPACE_DRAGON_SHOT3, SPACE_DRAGON
from characters.BasicEnemies import Enemy


class Boss(Enemy):
    def __init__(self, boss_list_element):
        sprite, self.lifes, self.speed, self.name = boss_list_element
        self.sprite = sprite
        self.rect = self.sprite.get_rect()
        x = SCREEN_WIDTH + random.randint(10, 50)
        y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
        self.rect.topleft = (x, y)

        self.arrived = False
        self.arriving_count = 550
        self.horizontal_count = random.randint(5, 10)
        self.horizontal_direction = random.choice([-1, 1])
        self.max_health = self.lifes

    def update(self):
        if self.arriving_count < 0:
            self.arrived = True
        else:
            self.rect.x -= self.speed
            self.arriving_count -= self.speed

        if self.arrived:
            if self.horizontal_count <= 0:
                self.horizontal_direction = random.choice([-1, 1])
                self.horizontal_count = random.randint(5, 10)
            else:
                if self.rect.y <= 0 or self.rect.y >= SCREEN_HEIGHT - 360:
                    self.horizontal_direction *= -1
                self.rect.y += self.speed * self.horizontal_direction

    def draw(self, screen):
        screen.blit(self.sprite, self.rect)

class SpaceDragon(Boss):
    def shoot(self):
        bullets = [
            SpaceDragonShot(self.rect.midleft, (0, 0)),
            SpaceDragonShot(self.rect.midleft, (0, -5)),  # na skos góra
            SpaceDragonShot(self.rect.midleft, (0, 5)),  # na skos dół
        ]
        return bullets

class SpaceDragonShot:
    def __init__(self, pos, direction):
        self.sprite = random.choice([SPACE_DRAGON_SHOT0, SPACE_DRAGON_SHOT1, SPACE_DRAGON_SHOT2, SPACE_DRAGON_SHOT3])
        self.rect = self.sprite.get_rect(center=pos)
        self.direction = direction
        self.distance_traveled = 0

    def update(self):
        speed = 10
        self.rect.x -= speed
        self.rect.y += self.direction[1]
        self.distance_traveled += speed

        if 100 <= self.distance_traveled <= 200:
            self.direction = (0, -self.direction[1])

    def draw(self, screen):
        screen.blit(self.sprite, self.rect)


