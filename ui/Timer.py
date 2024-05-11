import pygame


class Timer:
    def __init__(self):
        self.start_ticks = pygame.time.get_ticks()
        self.actual_time = '0:0:00'

    def refresh(self):
        now = pygame.time.get_ticks() - self.start_ticks
        minutes = now // 60000
        seconds = (now % 60000) // 1000
        milliseconds = (now % 1000) // 10
        self.actual_time = f'{minutes}:{seconds:02}:{milliseconds:02}'

    def __str__(self):
        return self.actual_time
