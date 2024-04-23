import curses
import time
import threading
import random

COLUMNS = 50
ROWS = 25
SHOT_SPEED = 2
"""
🛸
👾
👽
👹

"""
ENEMY_LIST = {'🛸': 1, '👾': 1, '👽': 2, '👹': 3}


class Enemy:
    def __init__(self):
        sprite, lifes = random.choice(list(ENEMY_LIST.items()))
        self.sprite = sprite
        self.lifes = lifes
        x = random.randint(3, 13)
        y = random.randint(3, 13)
        self.position = (COLUMNS * 2 - x, ROWS - y)

class Player:
    def __init__(self, lifes):
        self.lifes = lifes
        self.sprite = '🚀'
        # self.shot_sprite = '🔥'
        # self.shot_sprite = '⌁'
        # self.shot_sprite = '➢'
        self.shot_sprite = '⏤'
        self.position = [(10, 10)]

    def shot(self):
        return self.shot_sprite


class Timer:
    start_time = time.perf_counter()
    actual_time = '0:0:0'
    times= ['🕛', '🕐', '🕑', '🕒', '🕓', '🕔', '🕕', '🕖', '🕗', '🕘', '🕙', '🕚']
    times_index = 0
    def refresh(self):
        now = time.perf_counter() - self.start_time
        minutes = int(now // 60)
        seconds = int(now % 60)
        milliseconds = f'{(int((now - int(now)) * 1000)):02d}'[:2]

        self.actual_time = f'{self.times[self.times_index]} {minutes}:{seconds:02d}:{milliseconds}'
        self.times_index += 1
        if self.times_index == len(self.times):
            self.times_index = 0

    def __str__(self):
        return self.actual_time


class Space:
    def __init__(self):
        self.timer = Timer()
        self.timer_thread = threading.Thread()
        self.timer_thread.start()

        self.player = Player(3)
        self.game_over = False
        self.area_border_sprite = '🌌'
        self.field = [[" " for _ in range(COLUMNS * 2)] for _ in range(ROWS)]
        self.condition_move = threading.Condition()

        self.logs = ""

        self.shots = {}
        self.lock_shots = threading.Lock()

        self.enemies = {}
        self.lock_enemies = threading.Lock()

    def add_enemy(self, enemy: Enemy):
        self.lock_enemies.acquire()
        self.enemies[enemy.position] = enemy.sprite
        self.lock_enemies.release()


    def shots_physic(self):
        shots_copy = self.shots.copy()
        for (x, y), typ in shots_copy.items():
            del self.shots[(x, y)]
            x += SHOT_SPEED

            if x < (COLUMNS - 1) * 2:
                self.shots[(x, y)] = typ

        for (x, y), typ in self.shots.items():
            self.field[y][x] = typ

    def refresh(self):
        self.field = [[" " for _ in range(COLUMNS * 2)] for _ in range(ROWS)]
        self.timer.refresh()
        self.game_over = self.player.lifes == 0
        for x, y in self.player.position:
            self.field[y][x] = self.player.sprite

        for (x, y), sprite in self.enemies.items():
            self.field[y][x] = sprite

        self.shots_physic()
        if len(self.logs.splitlines()) > 30:
            self.logs = ""
    def __str__(self):
        area = f'Czas gry: {self.timer}\t'
        area += f'Pozostałe życia: {self.player.lifes * '💜'}\n'

        area += self.area_border_sprite * (COLUMNS + 1) + "\n"

        for row in self.field:
            area += self.area_border_sprite
            for slot in row:
                area += slot
            area += f'{self.area_border_sprite}\n'
        area += self.area_border_sprite * (COLUMNS + 1)
        area += f'\n\n\n {self.logs}'
        return area

    def controller(self, input):
        with self.condition_move:
            self.move(input)

    def move(self, input):
        x, y = self.player.position[0]
        match input:
            case 'w':
                y -= 1
            case 'a':
                x -= 1
            case 's':
                y += 1
            case 'd':
                x += 1
            case ' ':
                sx, sy = self.player.position[0]
                sx += 1
                self.lock_shots.acquire()
                self.shots[(sx, sy)] = self.player.shot()

                self.lock_shots.release()

        self.player.position[0] = (x, y)
        self.condition_move.notify()


def spawn_enemy(space):
    while not space.game_over:
        enemy = Enemy()
        space.add_enemy(enemy)
        time.sleep(1)


def controller(window, space):
    while not space.game_over:
        char = window.getch()
        space.logs += f'input char: {char}\n'
        space.controller(chr(char))


def start(window):
    space = Space()

    control = threading.Thread(target=controller, args=(window, space))
    control.start()

    enemy_spawner = threading.Thread(target=spawn_enemy, args=(space,))
    enemy_spawner.start()

    while not space.game_over:
        window.clear()
        window.insstr(0, 0, str(space))
        window.refresh()
        time.sleep(0.15)
        space.refresh()

    control.join()
    enemy_spawner.join()


if __name__ == "__main__":
    curses.wrapper(start)
