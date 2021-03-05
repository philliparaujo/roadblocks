import math

import pygame
import square


class SquareBoard:
    def __init__(self, cols, rows, border_size, ratio, Board, scale):
        self.cols = cols
        self.rows = rows
        self.border_size = border_size
        self.ratio = ratio  # ratio between wall and tile size
        self.Board = Board  # functional game board
        self.scale = scale  # True/False (scale vs. stretch)

        self.board = []  # array of Squares
        self.colors = {'red': (240, 0, 0),
                       'blue': (0, 0, 240),
                       'yellow': (255, 255, 0),

                       'empty_tile': (255, 255, 255),
                       'empty_wall': (240, 240, 240),

                       'wall': (60, 60, 60)
                       }

        self.create_squares()

    def create_squares(self):
        self.board = []
        screen_width, screen_height = pygame.display.get_surface().get_size()

        p_s_w = screen_width - 2 * self.border_size
        p_s_h = screen_height - 2 * self.border_size

        # Makes a default size for the modules (wall + square)
        w_module = 10
        h_module = 10
        w_small = w_module / (self.ratio + 1)
        w_large = w_module * self.ratio / (self.ratio + 1)
        h_small = h_module / (self.ratio + 1)
        h_large = h_module * self.ratio / (self.ratio + 1)

        # Scales the size to fit, rounds with int to appear nicer
        full_width = w_module * (self.cols - 1) / 2 + w_small
        full_height = h_module * (self.rows - 1) / 2 + h_small
        w_scale_ratio = p_s_w / full_width
        h_scale_ratio = p_s_h / full_height
        w_small = int(w_small * w_scale_ratio)
        w_large = int(w_large * w_scale_ratio)
        h_small = int(h_small * h_scale_ratio)
        h_large = int(h_large * h_scale_ratio)

        if self.scale:
            if w_small > h_small:
                w_small = h_small
                w_large = h_large
            else:
                h_small = w_small
                h_large = w_large

        # Calculates offset needed to center board
        w_offset = (screen_width - ((w_small + w_large) * (self.cols - 1) / 2 + w_small)) / 2
        h_offset = (screen_height - ((h_small + h_large) * (self.rows - 1) / 2 + h_small)) / 2

        # Creates Square, fills it depending on the loaded map, adds it to array
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                width, height = self.specific_size(r, c, w_small, w_large, h_small, h_large)
                x = w_offset + w_small * math.ceil(c / 2) + w_large * math.floor(c / 2)
                y = h_offset + h_small * math.ceil(r / 2) + h_large * math.floor(r / 2)

                sq = square.Square(x, y, width, height)
                if self.Board.board[r][c] == "?" or self.Board.board[r][c] == "#":
                    sq.change_fill(self.colors['wall'])
                elif self.Board.board[r][c] == "|":
                    sq.change_fill(self.colors['red'])
                elif self.Board.board[r][c] == "-":
                    sq.change_fill(self.colors['blue'])
                elif self.Board.board[r][c] == "A" or self.Board.board[r][c] == "B":
                    sq.change_fill(self.colors['yellow'])
                elif r % 2 == 1 and c % 2 == 1:
                    sq.change_fill(self.colors['empty_tile'])
                else:
                    sq.change_fill(self.colors['empty_wall'])
                # print(r, c, sq.x, sq.y, sq.width, sq.height, sq.get_color())
                row.append(sq)

            self.board.append(row)

    def draw_squares(self, screen):
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                self.board[r][c].draw_square(screen)

    def edit_fills(self, mouse_pos):
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                # If clicks within the square
                if (self.board[r][c].x < mouse_pos[0] < self.board[r][c].x + self.board[r][c].width) and \
                        (self.board[r][c].y < mouse_pos[1] < self.board[r][c].y + self.board[r][c].height):
                    # If empty, fill it
                    if self.board[r][c].get_color() == (self.colors['empty_tile']) or self.board[r][c].get_color() == (
                            self.colors['empty_wall']):
                        self.specific_fill(r, c, self.colors['wall'], self.colors['blue'], self.colors['red'],
                                           self.colors['yellow'])
                        self.specific_update(r, c, "?", "-", "|", "A")
                    # If not empty and not a map tile, make it empty
                    elif not (self.board[r][c].get_color() == self.colors['wall']):
                        self.specific_fill(r, c, self.colors['wall'], self.colors['empty_wall'],
                                           self.colors['empty_wall'], self.colors['yellow'])
                        self.specific_update(r, c, "?", " ", " ", "A")

    def resize_squares(self):
        self.create_squares()

    def update_game_board(self, r, c, what):
        self.Board.set(c, r, what)

    def specific_fill(self, r, c, corner, horiz, vert, tile):
        if r % 2 == 0 and c % 2 == 0:
            self.board[r][c].change_fill(corner)
        elif r % 2 == 0 and c % 2 == 1:
            self.board[r][c].change_fill(horiz)
        elif r % 2 == 1 and c % 2 == 0:
            self.board[r][c].change_fill(vert)
        elif r % 2 == 1 and c % 2 == 1:
            self.board[self.Board.get_start_pos()['y']][self.Board.get_start_pos()['x']].change_fill(
                self.colors['empty_tile'])
            self.board[r][c].change_fill(tile)

    def specific_update(self, r, c, corner, horiz, vert, tile):
        if r % 2 == 0 and c % 2 == 0:
            self.update_game_board(r, c, corner)
        elif r % 2 == 0 and c % 2 == 1:
            self.update_game_board(r, c, horiz)
        elif r % 2 == 1 and c % 2 == 0:
            self.update_game_board(r, c, vert)
        elif r % 2 == 1 and c % 2 == 1:
            self.update_game_board(self.Board.get_start_pos()['y'], self.Board.get_start_pos()['x'], " ")
            self.update_game_board(r, c, tile)

    def specific_size(self, r, c, w_small, w_large, h_small, h_large):
        # Returns width values
        if r % 2 == 0 and c % 2 == 0:
            return w_small, h_small
        elif r % 2 == 0 and c % 2 == 1:
            return w_large, h_small
        elif r % 2 == 1 and c % 2 == 0:
            return w_small, h_large
        elif r % 2 == 1 and c % 2 == 1:
            return w_large, h_large
