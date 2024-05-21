import pygame
import CONFIG

class Slider:
    def __init__(self, x, y, width, height, min_val, max_val, initial_val):
        self.rect = pygame.Rect(x, y, width, height)
        self.min_val = min_val
        self.max_val = max_val
        self.value = initial_val
        self.handle_rect = pygame.Rect(x + (initial_val - min_val) / (max_val - min_val) * width - 10, y - 5, 20, height + 10)
        self.dragging = False

    def draw(self, screen):
        pygame.draw.rect(screen, CONFIG.WHITE, self.rect)
        pygame.draw.rect(screen, CONFIG.GREEN, self.handle_rect)

    def get_value(self):
        return self.value