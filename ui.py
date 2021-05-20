import math

import pygame

import outline_square
import pf
import square


class SquareBoard:
    def __init__(self, cols, rows, border_size, ratio, Board, turn, player):
        self.cols = cols
        self.rows = rows
        self.border_size = border_size
        self.ratio = ratio  # ratio between wall and tile size
        self.Board = Board  # functional game board
        self.turn = turn  # If False, won't be drawn
        self.player = player  # 1 (blue, horiz) or 2 (red, vert)

        self.pathfinder = pf.PathFinder(self.Board, self.Board.get_start_pos(), self.Board.get_end_pos())
        self.mask = None
        self.board = []  # array of Squares
        self.outline_board = []  # array of yellow OutlineSquares
        self.wall_pieces = []  # array of Squares, represents walls outside the board (default = 7)
        self.wall_time = True  # True means it's time to place walls, False means it's time to move the player
        self.colors = {'red': (120, 0, 0),
                       'blue': (0, 0, 120),
                       'player': (0, 0, 0),

                       'empty_tile': (255, 255, 255),
                       'empty_wall': (240, 240, 240),

                       'wall': (60, 60, 60)
                       }
        if self.player == 1:
            self.start = "A"
            self.end = "B"
            self.colors['player'] = (0, 120, 240)
            self.align = "left"
        else:
            self.start = "a"
            self.end = "b"
            self.colors['player'] = (240, 20, 20)
            self.align = "right"

        self.create_squares()

    def create_squares(self):
        self.board = []
        self.outline_board = []

        screen_width, screen_height = pygame.display.get_surface().get_size()

        p_s_w = (screen_width - 2 * self.border_size) / 2
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
        full_height = h_module * (self.rows + 3) / 2 + h_small
        w_scale_ratio = p_s_w / full_width
        h_scale_ratio = p_s_h / full_height
        w_small = int(w_small * w_scale_ratio)
        w_large = int(w_large * w_scale_ratio)
        h_small = int(h_small * h_scale_ratio)
        h_large = int(h_large * h_scale_ratio)

        if w_small > h_small:
            w_small = h_small
            w_large = h_large
        else:
            h_small = w_small
            h_large = w_large

        # Calculates offset needed to center board
        h_offset = (screen_height - ((h_small + h_large) * (self.rows - 1) / 2 + h_small)) / 2
        board_height = ((h_small + h_large) * (self.rows - 1) / 2) / 2
        board_width = (w_small + w_large) * (self.cols - 1) / 2 + w_small
        if self.align == "right":
            w_offset = board_width + 2 * ((screen_width - 2 * board_width) / 3)
        elif self.align == "left":
            w_offset = (screen_width - 2 * board_width) / 3
        h_offset = (screen_height - 2 * board_height) / 2

        # Creates Square, fills it depending on the loaded map, adds it to array
        for r in range(self.rows):
            sq_row = []
            outline_row = []
            for c in range(self.cols):
                width, height = self.specific_size(r, c, w_small, w_large, h_small, h_large)
                x = w_offset + w_small * math.ceil(c / 2) + w_large * math.floor(c / 2)
                y = h_offset + h_small * math.ceil(r / 2) + h_large * math.floor(r / 2)

                sq = square.Square(x, y, width, height)
                outline_sq = outline_square.OutlineSquare(x, y, width, height)

                if self.Board.board[r][c] == "?" or self.Board.board[r][c] == "#":
                    sq.change_fill(self.colors['wall'])
                elif self.Board.board[r][c] == "|":
                    sq.change_fill(self.colors['red'])
                elif self.Board.board[r][c] == "-":
                    sq.change_fill(self.colors['blue'])
                elif self.Board.board[r][c] == self.start or self.Board.board[r][c] == self.end:
                    sq.change_fill(self.colors['player'])
                elif r % 2 == 1 and c % 2 == 1:
                    sq.change_fill(self.colors['empty_tile'])
                else:
                    sq.change_fill(self.colors['empty_wall'])
                # print(r, c, sq.x, sq.y, sq.width, sq.height, sq.get_color())
                sq_row.append(sq)
                outline_row.append(outline_sq)

            self.outline_board.append(outline_row)
            self.board.append(sq_row)

        self.create_mask()

    def draw(self, screen):
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                self.board[r][c].draw_square(screen)
                self.outline_board[r][c].draw_square(screen)

        self.mask.draw_square(screen)

        for wall in self.wall_pieces:
            wall.draw_square(screen)

    def edit_fills(self, mouse_pos, other):
        if self.get_mouse_index(mouse_pos) is not None:
            r, c = self.get_mouse_index(mouse_pos)
            if (self.player == 1 and not (r % 2 == 1 and c % 2 == 0)) or (self.player == 2 and not (r % 2 == 0 and c % 2 == 1)):
                if self.wall_time or self.get_click_adjacency(mouse_pos) == 2:
                    if self.board[r][c].get_color() == (self.colors['empty_tile']) or self.board[r][c].get_color() == (
                            self.colors['empty_wall']):
                        self.specific_fill(r, c, self.colors['wall'], self.colors['blue'], self.colors['red'],
                                           self.colors['player'], other)
                        self.specific_update(r, c, "?", "-", "|", self.start)

                        other.specific_fill(r, c, other.colors['wall'], other.colors['blue'], other.colors['red'],
                                            other.colors['player'], self)
                        other.specific_update(r, c, "?", "-", "|", other.start)

                    # If not empty and not a map tile, make it empty
                    elif not (self.board[r][c].get_color() == self.colors['wall']):
                        self.specific_fill(r, c, self.colors['wall'], self.colors['empty_wall'],
                                           self.colors['empty_wall'], self.colors['player'], other)
                        self.specific_update(r, c, "?", " ", " ", self.start)

                        other.specific_fill(r, c, other.colors['wall'], other.colors['empty_wall'],
                                            other.colors['empty_wall'], other.colors['player'], self)
                        other.specific_update(r, c, "?", " ", " ", other.start)

                for r in range(len(self.outline_board)):
                    for c in range(len(self.outline_board[0])):
                        self.outline_board[r][c].set_cooldown()
            else:
                print("Can't click here, dude!")

    def edit_outline(self, mouse_pos):
        for r in range(len(self.outline_board)):
            for c in range(len(self.outline_board[0])):
                self.outline_board[r][c].set_invisible()

        if self.get_mouse_index(mouse_pos) is not None:
            r, c = self.get_mouse_index(mouse_pos)
            if (self.player == 1 and not (r % 2 == 1 and c % 2 == 0)) or (
                    self.player == 2 and not (r % 2 == 0 and c % 2 == 1)):
                if not self.board[r][c].get_color() == self.colors['wall']:
                    if self.wall_time and not (r % 2 == 1 and c % 2 == 1):
                        self.outline_board[r][c].set_visible()
                    elif not self.wall_time and (r % 2 == 1 and c % 2 == 1):
                        self.outline_board[r][c].set_visible()

    def resize_squares(self, other):
        self.create_squares()
        self.set_opponent_tiles(other)
        self.set_your_tiles()

    def update_game_board(self, r, c, what):
        self.Board.set(c, r, what)

    def specific_fill(self, r, c, corner, horiz, vert, tile, other):
        if self.turn:
            wall_time = self.wall_time
        else:
            wall_time = other.wall_time

        if r % 2 == 0 and c % 2 == 0 and wall_time:
            self.board[r][c].change_fill(corner)
        elif r % 2 == 0 and c % 2 == 1 and wall_time:
            self.board[r][c].change_fill(horiz)
        elif r % 2 == 1 and c % 2 == 0 and wall_time:
            self.board[r][c].change_fill(vert)
        elif r % 2 == 1 and c % 2 == 1 and not wall_time:
            if self.turn:
                self.board[self.Board.get_start_pos()['y']][self.Board.get_start_pos()['x']].change_fill(
                    self.colors['empty_tile'])
                self.board[r][c].change_fill(tile)

                other.board[self.Board.get_start_pos()['y']][self.Board.get_start_pos()['x']].change_fill(
                    self.colors['empty_tile'])
                other.board[r][c].change_fill(tile)
            else:
                self.board[other.Board.get_start_pos()['y']][other.Board.get_start_pos()['x']].change_fill(
                    other.colors['empty_tile'])
                self.board[r][c].change_fill(other.colors['player'])

                other.board[other.Board.get_start_pos()['y']][other.Board.get_start_pos()['x']].change_fill(
                    other.colors['empty_tile'])
                other.board[r][c].change_fill(other.colors['player'])

    def specific_update(self, r, c, corner, horiz, vert, tile):
        if r % 2 == 0 and c % 2 == 0 and self.wall_time:
            self.update_game_board(r, c, corner)
        elif r % 2 == 0 and c % 2 == 1 and self.wall_time:
            self.update_game_board(r, c, horiz)
        elif r % 2 == 1 and c % 2 == 0 and self.wall_time:
            self.update_game_board(r, c, vert)
        elif r % 2 == 1 and c % 2 == 1 and not self.wall_time:
            if self.turn:
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

    def start_turn(self):
        self.turn = True

    def end_turn(self):
        self.turn = False
        self.wall_time = True

    def set_opponent_tiles(self, other):
        self.board[other.Board.get_start_pos()['y']][other.Board.get_start_pos()['x']].change_fill(
            other.colors['player'])
        self.board[other.Board.get_end_pos()['y']][other.Board.get_end_pos()['x']].change_fill(other.colors['player'])

    def set_your_tiles(self):
        self.board[self.Board.get_start_pos()['y']][self.Board.get_start_pos()['x']].change_fill(self.colors['player'])
        self.board[self.Board.get_end_pos()['y']][self.Board.get_end_pos()['x']].change_fill(self.colors['player'])

    def update_pathfinder(self):
        self.pathfinder = pf.PathFinder(self.Board, self.Board.get_start_pos(), self.pathfinder.end)

    def get_path(self):
        return self.pathfinder.get_path()

    def create_wall_pieces(self, screen, number):
        self.wall_pieces = []
        # number = # of starting walls for each player (7)
        if self.player == 1:
            width = self.board[2][1].width
            height = self.board[2][1].height
            color = self.colors['blue']
        else:
            width = self.board[1][2].width
            height = self.board[1][2].height
            color = self.colors['red']

        # y = pygame.display.get_surface().get_size()[1] - height - width/2

        y = self.get_size()[1] + self.board[0][0].y + width / 2

        for n in range(number):
            x = self.board[0][2 * n + 1].x
            sq = square.Square(x, y, width, height)
            sq.change_fill(color)
            self.wall_pieces.append(sq)
            sq.draw_square(screen)

        self.change_wall_piece_fills(screen, number - self.Board.get_num_walls())

    def change_wall_piece_fills(self, screen, number):
        # number = # of walls still not in play (7 - # walls on board)
        if self.player == 1:
            color = self.colors['blue']
        else:
            color = self.colors['red']

        for n in range(len(self.wall_pieces)):
            if n < number:
                self.wall_pieces[n].change_fill(color)
            else:
                self.wall_pieces[n].change_fill((0, 0, 0))
            self.wall_pieces[n].draw_square(screen)

    def get_size(self):
        width = self.board[len(self.board) - 1][len(self.board[0]) - 1].x + \
                self.board[len(self.board) - 1][len(self.board[0]) - 1].width - \
                self.board[0][0].x
        height = self.board[len(self.board) - 1][len(self.board[0]) - 1].y + \
                 self.board[len(self.board) - 1][len(self.board[0]) - 1].height - \
                 self.board[0][0].y

        return width, height

    def create_mask(self):
        self.mask = square.Square(self.board[0][0].x, self.board[0][0].y, self.get_size()[0] + 1,
                                  self.get_size()[1] + 1)
        self.mask.change_fill((0, 0, 0))
        self.toggle_mask_visible()

    def toggle_mask_visible(self):
        if self.turn:
            self.mask.set_alpha(0)
        else:
            self.mask.set_alpha(128)

    def get_mouse_index(self, mouse_pos):
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                # If clicks within the square
                if (self.board[r][c].x < mouse_pos[0] < self.board[r][c].x + self.board[r][c].width) and \
                        (self.board[r][c].y < mouse_pos[1] < self.board[r][c].y + self.board[r][c].height):
                    return r, c
        return None

    def get_click_adjacency(self, mouse_pos):
        if self.get_mouse_index(mouse_pos) is not None:
            old_r = self.Board.get_start_pos()['y']
            old_c = self.Board.get_start_pos()['x']
            r, c = self.get_mouse_index(mouse_pos)
            return math.fabs(old_r - r) + math.fabs(old_c - c)
