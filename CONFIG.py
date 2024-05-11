import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PLAYER_LIVES = 100

PLAYER_SPRITE_LOAD = pygame.image.load("assets/player.png")
PLAYER_SPRITE_SCALED = pygame.transform.scale(PLAYER_SPRITE_LOAD, (100, 100))
PLAYER_SPRITE = pygame.transform.rotate(PLAYER_SPRITE_SCALED, 270)

SHOT_SPRITE = pygame.image.load("assets/shot.png")
SHOT_SPRITE = pygame.transform.scale(SHOT_SPRITE, (100, 50))

ENEMY_SHOT_SPRITE_LOAD = pygame.image.load("assets/enemy_shot.png")
ENEMY_SHOT_SPRITE = pygame.transform.scale(ENEMY_SHOT_SPRITE_LOAD, (100, 50))


ENEMY_SPRITE1_LOAD = pygame.image.load("assets/enemies/ufo.png")
ENEMY_SPRITE1_SCALED = pygame.transform.scale(ENEMY_SPRITE1_LOAD, (100, 100))
ENEMY_SPRITE1 = pygame.transform.rotate(ENEMY_SPRITE1_SCALED, 90)

ENEMY_SPRITE2_LOAD = pygame.image.load("assets/enemies/alien.png")
ENEMY_SPRITE2_SCALED = pygame.transform.scale(ENEMY_SPRITE2_LOAD, (100, 100))
ENEMY_SPRITE2 = pygame.transform.rotate(ENEMY_SPRITE2_SCALED, 90)

ENEMY_SPRITE3_LOAD = pygame.image.load("assets/enemies/monster.png")
ENEMY_SPRITE3_SCALED = pygame.transform.scale(ENEMY_SPRITE3_LOAD, (100, 100))
ENEMY_SPRITE3 = pygame.transform.rotate(ENEMY_SPRITE3_SCALED, 90)

ENEMY_SPRITE4_LOAD = pygame.image.load("assets/enemies/demon.png")
ENEMY_SPRITE4_SCALED = pygame.transform.scale(ENEMY_SPRITE4_LOAD, (100, 100))
ENEMY_SPRITE4 = pygame.transform.rotate(ENEMY_SPRITE4_SCALED, 90)

ENEMY_LIST = [
    (ENEMY_SPRITE1, 1, 5),
    (ENEMY_SPRITE2, 1, 6),
    (ENEMY_SPRITE3, 2, 7),
    (ENEMY_SPRITE4, 3, 8)
]

RED = (255, 0, 0)
GREEN = (0, 255, 0)
GREY = (220,220,220)


SHOT_SPEED = 15
FPS = 30

MUSIC_ON = True

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

BACKGROUND1_LOAD = pygame.image.load("assets/backgrounds/background1.png")
BACKGROUND1 = pygame.transform.scale(BACKGROUND1_LOAD, (SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND2_LOAD = pygame.image.load("assets/backgrounds/background2.png")
BACKGROUND2 = pygame.transform.scale(BACKGROUND2_LOAD, (SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND3_LOAD = pygame.image.load("assets/backgrounds/background3.jpg")
BACKGROUND3 = pygame.transform.scale(BACKGROUND3_LOAD, (SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND4_LOAD = pygame.image.load("assets/backgrounds/background4.jpg")
BACKGROUND4 = pygame.transform.scale(BACKGROUND4_LOAD, (SCREEN_WIDTH, SCREEN_HEIGHT))