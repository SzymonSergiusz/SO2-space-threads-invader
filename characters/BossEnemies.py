import random

import math

import CONFIG
import SPRITES_CONFIG
from SPRITES_CONFIG import SPACE_DRAGON_SHOT0, SPACE_DRAGON_SHOT1, SPACE_DRAGON_SHOT2, SPACE_DRAGON_SHOT3, SPACE_DRAGON, SPACE_COW_SHOT0, SPACE_COW_SHOT1, SPACE_COW_SHOT2, SPACE_COW_SHOT3
from CONFIG import SCREEN_WIDTH, SCREEN_HEIGHT
from characters.BasicEnemies import Enemy


class Boss(Enemy):
    def __init__(self, boss_list_element, arriving_count=550):
        sprite, self.lives, self.speed, self.name = boss_list_element
        self.sprite = sprite
        self.rect = self.sprite.get_rect()
        x = SCREEN_WIDTH + random.randint(10, 50)
        y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
        self.rect.topleft = (x, y)

        self.arrived = False
        self.arriving_count = arriving_count
        self.horizontal_count = random.randint(5, 10)
        self.horizontal_direction = random.choice([-1, 1])
        self.max_health = self.lives

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


class SpaceCow(Boss):
    def shoot(self):
        bullets = []

        for i in range(0, 2):
            bullets.append(SpaceCowShot(random.choice([self.rect.topleft, self.rect.midleft, self.rect.bottomleft]),
                                        (0, i)))

        return bullets

class SpaceCowShot():
    def __init__(self, pos, direction):
        self.sprite = random.choice([SPACE_COW_SHOT0, SPACE_COW_SHOT1, SPACE_COW_SHOT2, SPACE_COW_SHOT3])
        self.rect = self.sprite.get_rect(center=pos)
        self.direction = direction
        self.distance_traveled = 0
    def update(self):
        speed = 10
        self.rect.x -= speed
        self.rect.y += random.choice([-5, 5])
        self.distance_traveled += speed
    def draw(self, screen):
        screen.blit(self.sprite, self.rect)

class MegaSpaceDragon(Boss):
    def __init__(self, boss_list_element, animation_frames):
        super().__init__(boss_list_element, arriving_count=700)
        self.animation_frames = animation_frames
        self.current_frame = 0
        self.animation_speed = 0.1
        self.animation_timer = 0
        self.sprite = self.animation_frames[self.current_frame]
        self.rect = self.sprite.get_rect(topleft=self.rect.topleft)
        self.shoot_timer = 0

    def update(self):
        super().update()
        self.animation_timer += self.animation_speed
        if self.animation_timer >= 1:
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.animation_frames)
            self.sprite = self.animation_frames[self.current_frame]

        self.shoot_timer += 1

    def shoot(self):
        bullets = []
        if self.shoot_timer >= 20:
            for angle in range(0, 360, 30):
                radian = angle * (math.pi / 180)
                direction = (-10 * round(math.cos(radian), 2), 10 * round(math.sin(radian), 2))
                bullets.append(MegaSpaceDragonShot(self.rect.center, direction))


            for _ in range(10):
                direction_y = random.randint(-5, 5)
                direction_x = random.randint(-5, 5)
                bullets.append(MegaSpaceDragonShot(self.rect.midleft, (direction_x, direction_y)))


            for i in range(0, 360, 45):
                angle = i + (self.current_frame * 10) + random.randint(-5, 5)
                radian = angle * (math.pi / 180)
                direction = (-10 * round(math.cos(radian), 2), 10 * round(math.sin(radian), 2))
                bullets.append(MegaSpaceDragonShot(self.rect.center, direction))

            self.shoot_timer = 0

        return bullets

    def draw(self, screen):
        screen.blit(self.sprite, self.rect)


class MegaSpaceDragonShot:
    def __init__(self, pos, direction):
        self.sprite = random.choice([SPRITES_CONFIG.MEGA_SPACE_DRAGON_SHOT0, SPRITES_CONFIG.MEGA_SPACE_DRAGON_SHOT1,
                                     SPRITES_CONFIG.MEGA_SPACE_DRAGON_SHOT2, SPRITES_CONFIG.MEGA_SPACE_DRAGON_SHOT3])
        self.rect = self.sprite.get_rect(center=pos)
        self.direction = direction
        self.distance_traveled = 0

    def update(self):
        speed = 15
        self.rect.x += self.direction[0]
        self.rect.y += self.direction[1]
        self.distance_traveled += speed

    def draw(self, screen):
        screen.blit(self.sprite, self.rect)