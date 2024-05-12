import pygame

from CONFIG import SCREEN_WIDTH, SCREEN_HEIGHT

PLAYER_SPRITE_LOAD = pygame.image.load("assets/player.png")
PLAYER_SPRITE_SCALED = pygame.transform.scale(PLAYER_SPRITE_LOAD, (100, 100))
PLAYER_SPRITE = pygame.transform.rotate(PLAYER_SPRITE_SCALED, 270)

SHOT_SPRITE = pygame.image.load("assets/shot.png")
SHOT_SPRITE = pygame.transform.scale(SHOT_SPRITE, (100, 50))

ENEMY_SHOT_SPRITE_LOAD = pygame.image.load("assets/enemy_shot.png")
ENEMY_SHOT_SPRITE = pygame.transform.scale(ENEMY_SHOT_SPRITE_LOAD, (100, 50))

ENEMY_SPRITE1_LOAD = pygame.image.load("assets/enemies/ship0.png")
ENEMY_SPRITE1_SCALED = pygame.transform.scale(ENEMY_SPRITE1_LOAD, (100, 100))
ENEMY_SPRITE1 = pygame.transform.rotate(ENEMY_SPRITE1_SCALED, 90)

ENEMY_SPRITE2_LOAD = pygame.image.load("assets/enemies/ship1.png")
ENEMY_SPRITE2_SCALED = pygame.transform.scale(ENEMY_SPRITE2_LOAD, (100, 100))
ENEMY_SPRITE2 = pygame.transform.rotate(ENEMY_SPRITE2_SCALED, 90)

ENEMY_SPRITE3_LOAD = pygame.image.load("assets/enemies/ship2.png")
ENEMY_SPRITE3_SCALED = pygame.transform.scale(ENEMY_SPRITE3_LOAD, (100, 100))
ENEMY_SPRITE3 = pygame.transform.rotate(ENEMY_SPRITE3_SCALED, 90)

ENEMY_SPRITE4_LOAD = pygame.image.load("assets/enemies/ship3.png")
ENEMY_SPRITE4_SCALED = pygame.transform.scale(ENEMY_SPRITE4_LOAD, (100, 100))
ENEMY_SPRITE4 = pygame.transform.rotate(ENEMY_SPRITE4_SCALED, 90)

ENEMY_LIST = [
    (ENEMY_SPRITE1, 1, 5),
    (ENEMY_SPRITE2, 1, 6),
    (ENEMY_SPRITE3, 2, 7),
    (ENEMY_SPRITE4, 3, 8)
]

LIFE_SPRITE_LOAD = pygame.image.load("assets/life.png")
LIFE_SPRITE = pygame.transform.scale(LIFE_SPRITE_LOAD, (50, 50))

SPACE_DRAGON_SPRITE_LOAD = pygame.image.load("assets/boss/pokemon/rayquaza_ten_z_pokemon.png")
SPACE_DRAGON = pygame.transform.scale(SPACE_DRAGON_SPRITE_LOAD, (500, 500))

SPACE_DRAGON_SHOT0_LOAD = pygame.image.load("assets/boss/pokemon/laser0.png")
SPACE_DRAGON_SHOT1_LOAD = pygame.image.load("assets/boss/pokemon/laser1.png")
SPACE_DRAGON_SHOT2_LOAD = pygame.image.load("assets/boss/pokemon/laser2.png")
SPACE_DRAGON_SHOT3_LOAD = pygame.image.load("assets/boss/pokemon/laser3.png")

dragon_shots = (100, 100)
SPACE_DRAGON_SHOT0 = pygame.transform.scale(SPACE_DRAGON_SHOT0_LOAD, dragon_shots)
SPACE_DRAGON_SHOT1 = pygame.transform.scale(SPACE_DRAGON_SHOT1_LOAD, dragon_shots)
SPACE_DRAGON_SHOT2 = pygame.transform.scale(SPACE_DRAGON_SHOT2_LOAD, dragon_shots)
SPACE_DRAGON_SHOT3 = pygame.transform.scale(SPACE_DRAGON_SHOT3_LOAD, dragon_shots)

SPACE_DRAGON_SHOT0 = pygame.transform.rotate(SPACE_DRAGON_SHOT0, 180)
SPACE_DRAGON_SHOT1 = pygame.transform.rotate(SPACE_DRAGON_SHOT1, 180)
SPACE_DRAGON_SHOT2 = pygame.transform.rotate(SPACE_DRAGON_SHOT2, 180)
SPACE_DRAGON_SHOT3 = pygame.transform.rotate(SPACE_DRAGON_SHOT3, 180)

SPACE_COW_SPRITE_LOAD = pygame.image.load("assets/boss/cow/kosmiczna_krowa.png")
SPACE_COW = pygame.transform.scale(SPACE_COW_SPRITE_LOAD, (400, 400))

SPACE_COW_SHOT0_LOAD = pygame.image.load("assets/boss/cow/laser0.png")
SPACE_COW_SHOT1_LOAD = pygame.image.load("assets/boss/cow/laser1.png")
SPACE_COW_SHOT2_LOAD = pygame.image.load("assets/boss/cow/laser2.png")
SPACE_COW_SHOT3_LOAD = pygame.image.load("assets/boss/cow/laser3.png")
space_shots = (100, 100)
SPACE_COW_SHOT0 = pygame.transform.scale(SPACE_COW_SHOT0_LOAD, space_shots)
SPACE_COW_SHOT1 = pygame.transform.scale(SPACE_COW_SHOT1_LOAD, space_shots)
SPACE_COW_SHOT2 = pygame.transform.scale(SPACE_COW_SHOT2_LOAD, space_shots)
SPACE_COW_SHOT3 = pygame.transform.scale(SPACE_COW_SHOT3_LOAD, space_shots)

SPACE_COW_SHOT0 = pygame.transform.rotate(SPACE_COW_SHOT0, 180)
SPACE_COW_SHOT1 = pygame.transform.rotate(SPACE_COW_SHOT1, 180)
SPACE_COW_SHOT2 = pygame.transform.rotate(SPACE_COW_SHOT2, 180)
SPACE_COW_SHOT3 = pygame.transform.rotate(SPACE_COW_SHOT3, 180)

MSDF0_LOAD = pygame.image.load("assets/boss/dragon/smok0.png")
MSDF1_LOAD = pygame.image.load("assets/boss/dragon/smok1.png")
MSDF2_LOAD = pygame.image.load("assets/boss/dragon/smok2.png")

mega_dragon_size = (600, 500)
MSDF0_SCALED = pygame.transform.scale(MSDF0_LOAD, mega_dragon_size)
MSDF1_SCALED = pygame.transform.scale(MSDF1_LOAD, mega_dragon_size)
MSDF2_SCALED = pygame.transform.scale(MSDF2_LOAD, mega_dragon_size)

MSDF0_ROTATED = pygame.transform.flip(MSDF0_SCALED, 1, 0)
MSDF1_ROTATED = pygame.transform.flip(MSDF1_SCALED, 1, 0)
MSDF2_ROTATED = pygame.transform.flip(MSDF2_SCALED, 1, 0)

MEGA_SPACE_DRAGON_FRAMES = [
    MSDF0_ROTATED,
    MSDF1_ROTATED,
    MSDF2_ROTATED,
]

BACKGROUND1_LOAD = pygame.image.load("assets/backgrounds/background1.png")
BACKGROUND1 = pygame.transform.scale(BACKGROUND1_LOAD, (SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND2_LOAD = pygame.image.load("assets/backgrounds/background2.png")
BACKGROUND2 = pygame.transform.scale(BACKGROUND2_LOAD, (SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND3_LOAD = pygame.image.load("assets/backgrounds/background3.jpg")
BACKGROUND3 = pygame.transform.scale(BACKGROUND3_LOAD, (SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND4_LOAD = pygame.image.load("assets/backgrounds/background4.jpg")
BACKGROUND4 = pygame.transform.scale(BACKGROUND4_LOAD, (SCREEN_WIDTH, SCREEN_HEIGHT))


MEGA_SPACE_DRAGON_SHOT0_LOAD = pygame.image.load("assets/boss/dragon/laser0.png")
MEGA_SPACE_DRAGON_SHOT1_LOAD = pygame.image.load("assets/boss/dragon/laser1.png")
MEGA_SPACE_DRAGON_SHOT2_LOAD = pygame.image.load("assets/boss/dragon/laser2.png")
MEGA_SPACE_DRAGON_SHOT3_LOAD = pygame.image.load("assets/boss/dragon/laser3.png")

MEGA_dragon_shots = (50, 50)
MEGA_SPACE_DRAGON_SHOT0 = pygame.transform.scale(MEGA_SPACE_DRAGON_SHOT0_LOAD, MEGA_dragon_shots)
MEGA_SPACE_DRAGON_SHOT1 = pygame.transform.scale(MEGA_SPACE_DRAGON_SHOT1_LOAD, MEGA_dragon_shots)
MEGA_SPACE_DRAGON_SHOT2 = pygame.transform.scale(MEGA_SPACE_DRAGON_SHOT2_LOAD, MEGA_dragon_shots)
MEGA_SPACE_DRAGON_SHOT3 = pygame.transform.scale(MEGA_SPACE_DRAGON_SHOT3_LOAD, MEGA_dragon_shots)


MEGA_SPACE_DRAGON_SHOT0 = pygame.transform.rotate(MEGA_SPACE_DRAGON_SHOT0, 180)
MEGA_SPACE_DRAGON_SHOT1 = pygame.transform.rotate(MEGA_SPACE_DRAGON_SHOT1, 180)
MEGA_SPACE_DRAGON_SHOT2 = pygame.transform.rotate(MEGA_SPACE_DRAGON_SHOT2, 180)
MEGA_SPACE_DRAGON_SHOT3 = pygame.transform.rotate(MEGA_SPACE_DRAGON_SHOT3, 180)

DYNAMIC_BACKGROUND_ITEMS = []
for i in range(0, 10):
    path = f"assets/backgrounds/elements/planet{i}.png"
    load = pygame.image.load(path)
    scale = pygame.transform.scale(load, (500, 500))
    DYNAMIC_BACKGROUND_ITEMS.append(scale)
for i in range(0, 9):
    path = f"assets/backgrounds/elements/easteregg{i}.png"
    load = pygame.image.load(path)
    scale = pygame.transform.scale(load, (500, 500))
    DYNAMIC_BACKGROUND_ITEMS.append(scale)