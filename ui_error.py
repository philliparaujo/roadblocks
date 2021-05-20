import pygame
from pygame import Surface

from dice import Dice
from square import Square


class UiError(Square):
    def __init__(self, x, y, width, height, message):
        super().__init__(x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.display_count = 0
        self.fill((255, 100, 100))
        self.message = message
        self.set_alpha(255)

        self.text = None
        self.text_rect = None
        self.render_text()

    def draw_square(self, screen):
        if self.display_count > 300:
            return False

        super().draw_square(screen)
        self.display_count += 1

        screen.blit(self.text, self.text_rect)

    def resize(self, width, height):
        self.display_count = 300
        self.render_text()

    def render_text(self):
        pygame.init()
        font = pygame.font.Font(pygame.font.get_default_font(), int(self.height/3))
        self.text = font.render(self.message, False, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.centerx = self.x + self.width / 2
        self.text_rect.centery = self.y + self.height / 2

    # def draw(self, screen):
    #     if self.display_count > 1000:
    #         return False
    #
    #     (screen_width, screen_height) = screen.get_size()
    #
    #     self.display_count = self.display_count + 1
    #     screen.blit(self,
    #                 ((screen_width - self.get_width()) / 2,
    #                  (screen_height - self.get_height()) / 2))
    #     return True
