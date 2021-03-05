import pygame


class Square(pygame.Surface):
    def __init__(self, x, y, width, height):
        pygame.Surface.__init__(self, (width, height))
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.color = (255, 255, 255)
        self.fill(self.color)

    def change_fill(self, new_color):
        # new_color = (r, g, b)
        self.color = new_color
        self.fill(self.color)

    def change_size(self, width, height):
        self.width = width
        self.height = height

    def change_pos(self, x, y):
        self.x = x
        self.y = y

    def x(self):
        return self.x

    def y(self):
        return self.y

    def get_size(self):
        return self.width, self.height

    def get_color(self):
        return self.color

    def draw_square(self, screen):
        screen.blit(self, (self.x, self.y))
