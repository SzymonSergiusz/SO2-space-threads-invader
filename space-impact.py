import pygame
import random
import threading
import pygame.mixer

import CONFIG
import SPRITES_CONFIG
from CONFIG import SHOT_SPEED, SCREEN_WIDTH, BLACK, WHITE, SCREEN_HEIGHT, FPS, PLAYER_SPEED
from Level import Level
from ui.Slider import Slider
from characters.BasicEnemies import Enemy
from characters.Player import Player
from characters.Projectiles import Shot
from characters.BossEnemies import Boss, SpaceDragon, SpaceCow, MegaSpaceDragon
from ui.BackgroundItems import BackgroundItems
from ui.Boost import Boost
from ui.Timer import Timer

LEVELS = [
    Level(0, SPRITES_CONFIG.BACKGROUND1, 20,
          SpaceDragon((SPRITES_CONFIG.SPACE_DRAGON, 40, 8, 'Rayquaza z Pokemonów')), ),
    Level(1, SPRITES_CONFIG.BACKGROUND2, 50, SpaceCow((SPRITES_CONFIG.SPACE_COW, 40, 8, 'Kosmiczna krowa')), ),
    Level(2, SPRITES_CONFIG.BACKGROUND3, 70,
          MegaSpaceDragon((SPRITES_CONFIG.MEGA_SPACE_DRAGON_FRAMES[0], 40, 8, 'MegaSmok'),
                          SPRITES_CONFIG.MEGA_SPACE_DRAGON_FRAMES))
]


class Game:
    def __init__(self):
        self.timer = Timer()
        self.player = Player()
        self.volume_slider = Slider(800, 30, 300, 20, 0, 1, 0.1)
        self.game_over = False
        self.shots = []
        self.enemy_shots = []
        self.enemies = []
        self.bosses = []
        self.points = 0
        self.life_sprite = SPRITES_CONFIG.LIFE_SPRITE
        self.boss_spawned = False
        self.level = LEVELS[0]
        self.points_to_beat = self.level.points_to_boss
        self.background = self.level.background
        self.background_elements = []
        self.last_background_element_spawn_time = 0


        self.boosts = []
        self.boosts_lock = threading.Semaphore(CONFIG.BOOSTS_LIMIT) # SEMAPHORE

        self.enemies_lock = threading.Semaphore(CONFIG.MAX_ENEMY_NUMBER) # SEMAPHORE

        self.points_lock = threading.Lock() # MUTEX

    def new_level(self, new_level):
        self.level = new_level
        self.points_to_beat = new_level.points_to_boss
        self.background = new_level.background
        self.boss_spawned = False

    def add_enemy(self, enemy: Enemy):
        if not self.boss_spawned:
            self.enemies.append(enemy)

    def add_backround_element(self):
        if SPRITES_CONFIG.DYNAMIC_BACKGROUND_ITEMS:
            element = random.choice(SPRITES_CONFIG.DYNAMIC_BACKGROUND_ITEMS)
            self.background_elements.append(BackgroundItems(element))
            SPRITES_CONFIG.DYNAMIC_BACKGROUND_ITEMS.remove(element)

    def add_boss(self, boss: Boss):
        self.bosses.append(boss)

    def shots_physic(self):
        for shot in self.shots[:]:
            shot.rect.x += SHOT_SPEED
            if shot.rect.x > SCREEN_WIDTH:
                self.shots.remove(shot)

        for shot in self.enemy_shots[:]:
            shot.rect.x -= SHOT_SPEED
            if shot.rect.x < 0 or shot.rect.y < 0 or shot.rect.y > SCREEN_HEIGHT:
                self.enemy_shots.remove(shot)

    def check_collisions(self):
        shots_to_remove = []
        enemies_to_remove = []
        bosses_to_remove = []

        for shot in self.shots[:]:
            for enemy in self.enemies[:]:
                if shot.rect.colliderect(enemy.rect):
                    if shot not in shots_to_remove:
                        shots_to_remove.append(shot)
                    enemy.lifes -= 1
                    if enemy.lifes <= 0 and enemy not in enemies_to_remove:
                        enemies_to_remove.append(enemy)

            for boss in self.bosses[:]:
                if shot.rect.colliderect(boss.rect):
                    if shot not in shots_to_remove:
                        shots_to_remove.append(shot)
                    boss.lifes -= 1
                    if boss.lifes <= 0 and boss not in bosses_to_remove:
                        bosses_to_remove.append(boss)

        for shot in shots_to_remove:
            if shot in self.shots:
                self.shots.remove(shot)

        for enemy in enemies_to_remove:
            if enemy in self.enemies:
                self.enemies.remove(enemy)
                with self.points_lock:
                    self.points += 1
                self.enemies_lock.release()

        for boss in bosses_to_remove:
            if boss in self.bosses:
                self.bosses.remove(boss)
                with self.points_lock:
                    self.points += 10
                if self.level.level_number < len(LEVELS) - 1:
                    self.new_level(LEVELS[self.level.level_number + 1])
                else:
                    self.game_over = True
        for shot in self.enemy_shots[:]:
            if shot.rect.colliderect(self.player.rect):
                self.enemy_shots.remove(shot)
                self.player.lifes -= 1
                if self.player.lifes <= 0:
                    self.game_over = True

    def refresh(self):
        self.timer.refresh()
        self.shots_physic()
        self.check_collisions()


        for boost in self.boosts:
            boost.update()
        for planet in self.background_elements[:]:
            planet.update()
            if planet.rect.right < 0:
                self.background_elements.remove(planet)

        if random.choice([False, True]):
            self.add_boost()

        if not self.boss_spawned and self.points >= self.points_to_beat:
            self.boss_spawned = True
            self.enemies = []
            self.enemies_lock = threading.Semaphore(CONFIG.MAX_ENEMY_NUMBER)
            self.spawn_boss()

        if not self.boss_spawned:
            for enemy in self.enemies[:]:
                enemy.update()
                if random.random() < 0.02:
                    self.enemy_shots.append(enemy.shoot())

        for boss in self.bosses[:]:
            boss.update()
            if random.random() < 0.05:
                new_shots = boss.shoot()
                self.enemy_shots.extend(new_shots)

        for shot in self.enemy_shots:
            shot.update()

        self.game_over = self.player.lifes == 0

    def draw(self, screen):
        screen.blit(self.background, (0, 0))

        for boost in self.boosts:
            boost.draw(screen)

        for planet in self.background_elements:
            planet.draw(screen)

        for shot in self.shots:
            screen.blit(shot.sprite, shot.rect)

        for shot in self.enemy_shots:
            screen.blit(shot.sprite, shot.rect)

        for enemy in self.enemies:
            enemy.draw(screen)

        for boss in self.bosses:
            boss.draw(screen)

        font = pygame.font.Font(None, 36)
        timer_surf = font.render(f"Time: {self.timer}", True, WHITE)
        screen.blit(timer_surf, (10, 10))

        for i in range(self.player.lifes):
            screen.blit(self.life_sprite, (10 + i * 36, 50))

        points_surf = font.render(f"Points: {self.points}", True, WHITE)
        screen.blit(points_surf, (10, 90))

        quit_button = pygame.Rect(SCREEN_WIDTH - 100, 10, 80, 40)
        pygame.draw.rect(screen, WHITE, quit_button)
        quit_text = font.render("Quit", True, BLACK)
        screen.blit(quit_text, (
            quit_button.centerx - quit_text.get_width() // 2, quit_button.centery - quit_text.get_height() // 2))
        screen.blit(self.player.sprite, self.player.rect)
        self.draw_boss_health_bar(screen)
        self.volume_slider.draw(screen)
        return quit_button

    def move_player(self, dx, dy):
        self.player.move(dx, dy)

    def add_boost(self):
        if self.boosts_lock.acquire(blocking=False):
            self.boosts.append(Boost())
            threading.Timer(random.randint(5, 20), self.boosts_lock.release).start()

    def shoot(self):
        if self.player.ammo_limit_lock.acquire(blocking=False):
            # TODO urozmaicić
            shot = Shot(self.player.rect.midright)
            self.shots.append(shot)
            threading.Timer(self.player.reload_time, self.player.ammo_limit_lock.release).start()

    def spawn_boss(self):
        boss = self.level.boss_class
        self.add_boss(boss)

    def draw_boss_health_bar(self, screen):
        if self.bosses:
            boss = self.bosses[0]
            max_lifes = boss.max_health
            bar_width = 1200
            bar_height = 20
            fill_width = int(bar_width * boss.lifes / max_lifes)
            bar_x = (SCREEN_WIDTH - bar_width) // 2
            bar_y = SCREEN_HEIGHT - 30
            screen.blit(pygame.font.Font(None, 50).render(boss.name, True, WHITE),
                        (bar_x + bar_width // 3, SCREEN_HEIGHT - 80))
            pygame.draw.rect(screen, CONFIG.RED, (bar_x, bar_y, bar_width, bar_height))
            pygame.draw.rect(screen, CONFIG.GREY, (bar_x, bar_y, fill_width, bar_height))


def spawn_enemy(game):
    while not game.game_over:
        if not game.boss_spawned and game.enemies_lock.acquire(blocking=False):
            enemy = Enemy()
            game.add_enemy(enemy)
        pygame.time.wait(2000)


def timer(game):
    while not game.game_over:
        pygame.time.wait(10)
        game.timer.refresh()


def spawn_background_element(game):
    while not game.game_over:
        pygame.time.wait(random.randint(5, 30) * 1000)
        game.add_backround_element()


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Threads Impact")

    pygame.mixer.init()
    pygame.mixer.music.load("assets/background_music.mp3")
    pygame.mixer.music.set_volume(0.1)
    if CONFIG.MUSIC_ON:
        pygame.mixer.music.play(-1)

    clock = pygame.time.Clock()
    game = Game()

    enemy_spawner = threading.Thread(target=spawn_enemy, args=(game,))
    enemy_spawner.start()

    timer_thread = threading.Thread(target=timer, args=(game,))
    timer_thread.start()

    ui_background_items_thread = threading.Thread(target=spawn_background_element, args=(game,))
    ui_background_items_thread.start()

    dx, dy = 0, 0

    while not game.game_over:
        quit_button = game.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    dy = -PLAYER_SPEED
                elif event.key == pygame.K_a:
                    dx = -PLAYER_SPEED
                elif event.key == pygame.K_s:
                    dy = PLAYER_SPEED
                elif event.key == pygame.K_d:
                    dx = PLAYER_SPEED
                elif event.key == pygame.K_SPACE:
                    game.shoot()

                # CHEAT CODES
                elif event.key == pygame.K_p:
                    with game.points_lock:
                        game.points += 10
                elif event.key == pygame.K_x:
                    if game.boss_spawned:
                        game.bosses[0].lifes = 1


                elif event.key == pygame.K_ESCAPE:
                    game.game_over = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    dy = 0
                elif event.key == pygame.K_a or event.key == pygame.K_d:
                    dx = 0
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if quit_button.collidepoint(event.pos):
                    game.game_over = True
                elif game.volume_slider.handle_rect.collidepoint(event.pos):
                    game.volume_slider.dragging = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                game.volume_slider.dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if game.volume_slider.dragging:
                    new_x = max(game.volume_slider.rect.left, min(event.pos[0] - 10, game.volume_slider.rect.right - 20))
                    game.volume_slider.handle_rect.x = new_x
                    game.volume_slider.value = game.volume_slider.min_val + (new_x - game.volume_slider.rect.left) / (game.volume_slider.rect.width) * (game.volume_slider.max_val - game.volume_slider.min_val)
                    pygame.mixer.music.set_volume(game.volume_slider.get_value())


        game.move_player(dx, dy)
        game.refresh()
        pygame.display.flip()
        clock.tick(FPS)

    enemy_spawner.join()
    timer_thread.join()
    ui_background_items_thread.join()
    pygame.quit()


if __name__ == "__main__":
    main()