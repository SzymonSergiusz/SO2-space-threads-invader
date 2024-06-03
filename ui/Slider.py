import pygame
import CONFIG

class Slider:
    def __init__(self, x, y, width, height, min_val, max_val, initial_val):
        self.rect = pygame.Rect(x, y, width, height)
        self.min_val = min_val
        self.max_val = max_val
        self.value = initial_val
        self.handle_rect = pygame.Rect(x + (initial_val - min_val) / (max_val - min_val) * width - 10, y, 20, height)
        self.dragging = False

    def draw(self, screen):
        pygame.draw.rect(screen, CONFIG.WHITE, self.rect)
        pygame.draw.rect(screen, CONFIG.RED, self.handle_rect)

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.handle_rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                new_x = max(self.rect.left, min(event.pos[0] - 10, self.rect.right - 20))
                self.handle_rect.x = new_x
                self.value = self.min_val + (new_x - self.rect.left) / (self.rect.width) * (self.max_val - self.min_val)

    def get_value(self):
        return self.value