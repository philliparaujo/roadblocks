import square
import pygame


class OutlineSquare(square.Square):
    def __init__(self, x, y, width, height):
        square.Square.__init__(self, x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.color = (255, 255, 0)
        self.fill(self.color)
        self.visible = False
        self.set_alpha(192)

        self.last = pygame.time.get_ticks()
        self.cooldown = 300

    def draw_square(self, screen):
        if self.visible and self.get_cooldown() > self.cooldown:
            super().draw_square(screen)

    def set_visible(self):
        self.visible = True

    def set_invisible(self):
        self.visible = False

    def get_cooldown(self):
        now = pygame.time.get_ticks()
        return now - self.last

    def set_cooldown(self):
        self.last = pygame.time.get_ticks()


