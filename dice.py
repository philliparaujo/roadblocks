import random
import pygame
import time
from pygame import Surface


class Dice(Surface):
    def __init__(self, x, y, width, roll_options):
        Surface.__init__(self, (width, width))
        self.x = x
        self.y = y
        self.width = width
        self.height = width
        self.roll_options = roll_options  # [1, 2, 3, 4, 5, 6]

        self.last_roll = 1
        self.moves_left = 0
        self.dots = []  # Array of dots, colors
        self.dot_logic = {
            1: [5],
            2: [1, 9],
            3: [1, 5, 9],
            4: [1, 3, 7, 9],
            5: [1, 3, 5, 7, 9],
            6: [1, 3, 4, 6, 7, 9],
            9: [1, 2, 3, 4, 5, 6, 7, 8, 9]  # For testing purposes
        }
        self.color = (255, 255, 255)
        self.fill(self.color)

    def roll(self):
        self.last_roll = self.roll_options[random.randint(0, 5)]
        self.moves_left = self.last_roll
        self.create_dots(self.last_roll)

    def change_roll_options(self, roll_options):
        self.roll_options = roll_options

    def draw(self, screen):
        screen.blit(self, (self.x, self.y))

    def resize(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width
        self.height = width

        return Dice(x, y, width, self.roll_options)

    def create_dots(self, roll):
        roll_logic = self.dot_logic[roll]
        self.dots = []

        for n in range(9):
            if n < 3:
                y = self.height * 1 / 6
            elif n < 6:
                y = self.height * 3 / 6
            else:
                y = self.height * 5 / 6

            if n % 3 == 0:
                x = self.width * 1 / 6
            elif n % 3 == 1:
                x = self.width * 3 / 6
            else:
                x = self.width * 5 / 6

            color = (255, 255, 255)
            for i in roll_logic:
                if i == n+1:
                    color = (0, 0, 0)

            n = pygame.draw.circle(self, color, (x, y), self.width / 10)
            n = {'dot': n, 'color': color}
            self.dots.append(n)

    def animate_roll(self):
        clock = pygame.time.Clock()
        for i in range(10):
            self.roll()
            pygame.display.flip()
            clock.tick(100)
