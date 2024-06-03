import pygame
import CONFIG
from ui.Slider import Slider
from CONFIG import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK

class Menu:
    def __init__(self):
        self.font = pygame.font.Font(None, 50)
        self.resume_button = pygame.Rect((SCREEN_WIDTH - 200) // 2, SCREEN_HEIGHT // 2 - 50, 200, 50)
        self.quit_button = pygame.Rect((SCREEN_WIDTH - 200) // 2, SCREEN_HEIGHT // 2 + 50, 200, 50)
        self.volume_slider = Slider((SCREEN_WIDTH // 2 - 150), (SCREEN_HEIGHT - SCREEN_HEIGHT // 4), 300, 20, 0, 1, 0.5)
        self.background_fade = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.faded = False

    def display(self, screen):
        if not self.faded:
            self.background_fade.fill(BLACK)
            self.background_fade.set_alpha(200)
            screen.blit(self.background_fade, (0, 0))
            self.faded = True

        pygame.draw.rect(screen, WHITE, self.resume_button)
        pygame.draw.rect(screen, WHITE, self.quit_button)

        paused_text = pygame.font.Font(None, 100).render("Paused", True, WHITE)
        resume_text = self.font.render("Resume", True, BLACK)
        quit_text = self.font.render("Quit", True, BLACK)
        volume_text = pygame.font.Font(None, 50).render("Volume Control", True, WHITE)

        screen.blit(paused_text, ((SCREEN_WIDTH - paused_text.get_width()) // 2, SCREEN_HEIGHT // 2 - 200))
        screen.blit(resume_text, (self.resume_button.centerx - resume_text.get_width() // 2, self.resume_button.centery - resume_text.get_height() // 2))
        screen.blit(quit_text, (self.quit_button.centerx - quit_text.get_width() // 2, self.quit_button.centery - quit_text.get_height() // 2))
        screen.blit(volume_text, ((SCREEN_WIDTH - volume_text.get_width()) // 2, (SCREEN_HEIGHT - SCREEN_HEIGHT // 4 - 50)))

        self.volume_slider.draw(screen)
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type in [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION]:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.resume_button.collidepoint(event.pos):
                        self.faded = False
                        return True
                    elif self.quit_button.collidepoint(event.pos):
                        return False
                self.volume_slider.update(event)
                pygame.mixer.music.set_volume(self.volume_slider.get_value())
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.faded = False
                    return True
        return None