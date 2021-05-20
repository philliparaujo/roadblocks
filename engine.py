import math

import numpy
import pygame

import dice
import pf


class Engine:
    def __init__(self, screen):
        self.screen = screen  # pygame.display
        self.dice = None  # Dice object

        self.p1 = None  # ui.SquareBoard
        self.p2 = None  # ui.SquareBoard
        self.game_over = None

        self.old_board = None  # Most recent board state created at start of turn

    def create_game(self, p1):
        self.p1 = p1
        self.game_over = False
        p1.create_squares()

        self.old_board = numpy.array(self.p1.Board.board)

    def join_game(self, p2):
        self.p2 = p2
        p2.create_squares()
        self.p1.set_opponent_tiles(self.p2)
        self.p2.set_opponent_tiles(self.p1)

    def set_dice(self, dice):
        self.dice = dice

    def draw(self, bt, bt2):
        # Has to be run in a while loop
        if self.game_over is not True:
            # Draws left board
            if self.p1 is not None:
                self.p1.draw(self.screen)

            # Draws right board
            if self.p2 is not None:
                self.p2.draw(self.screen)

            # Draws dice
            self.dice.draw(self.screen)

            # Draws top right UI
            self.display_text_right("Walls left: " + str(self.walls_left()[1]), int(self.dice.height / 2),
                                    bt.left - 10, bt.centery)
            self.display_text_right("Moves left: " + str(self.moves_left()), int(self.dice.height / 2),
                                    bt2.left - 10, bt2.centery)
            bt.draw(self.screen, self)
            bt2.draw(self.screen, self)
            self.display_text_center("lock walls", int(bt.height * 2 / 3), bt.centerx, bt.centery)
            self.display_text_center("end turn", int(bt2.height * 2 / 3), bt2.centerx, bt2.centery)

    def edit_outlines(self, pos, dice):
        if self.game_over is not True:
            if not dice.is_rolling():
                player, other = self.get_player_turn()
                player.edit_outline(pos)

    def recreate_board(self):
        if self.game_over is not True:
            if self.p1 is not None:
                self.p1.resize_squares(self.p2)
                self.p1.create_wall_pieces(self.screen, 7)
            if self.p2 is not None:
                self.p2.resize_squares(self.p1)
                self.p2.create_wall_pieces(self.screen, 7)

    def create_wall_pieces(self):
        if self.p1 is not None:
            self.p1.create_wall_pieces(self.screen, 7)
        if self.p2 is not None:
            self.p2.create_wall_pieces(self.screen, 7)

    def set_old_board(self):
        player, other = self.get_player_turn()
        self.old_board = numpy.array(player.Board.board)

    def play(self, pos):
        if self.game_over is not True:
            if not self.dice.is_rolling():
                player, other = self.get_player_turn()
                player.edit_fills(pos, other)
                player.update_pathfinder()
                other.update_pathfinder()
                if player.get_path() is None or other.get_path() is None:  # If illegal move, notify
                    print(player.get_path(), other.get_path())

                if player.wall_time:
                    player.change_wall_piece_fills(self.screen, 7 - player.Board.get_num_walls())
                elif player.get_click_adjacency(pos) == 0:
                    self.dice.moves_left -= 1

                # print(player.Board.get_num_walls())
                # player.Board.print()
                # print(player.get_mouse_index(pos))

    def walls_left(self):
        player, other = self.get_player_turn()
        if player.wall_time:
            high_limit = 7 - self.dice.last_roll
            high_limit -= player.Board.get_changes(self.old_board)
            low_limit = self.dice.last_roll
            low_limit -= player.Board.get_changes(self.old_board)
            if low_limit > high_limit:
                low_limit = high_limit

            if low_limit < 0:
                low_limit = 0

            return low_limit, high_limit
        else:
            return 0, 0

    def moves_left(self):
        return self.dice.moves_left

    def end_wall_time(self):
        player, other = self.get_player_turn()
        if player.wall_time:
            num_changes = player.Board.get_changes(self.old_board)
            print(num_changes)
            # if num_changes == (7 - self.dice.last_roll):
            player.wall_time = False
            print("Wall time over, now move!")

    def wait_next_move(self, player):
        if self.game_over is None:
            return "Game hasn't started"
        elif self.game_over:
            return "Game over"
        else:
            p, o = self.get_player_turn()
            if player == p:
                return "Your turn"
            elif player == o:
                return "Other player's turn"

    def switch_turns(self):
        if not self.game_over:
            player, other = self.get_player_turn()
            player.end_turn()
            other.start_turn()
            print("Player " + str(other.player) + "'s turn")

            player.toggle_mask_visible()
            other.toggle_mask_visible()

            self.dice.trigger_roll()

    def get_player_turn(self):
        if not self.game_over:
            if self.p1.turn:
                return self.p1, self.p2
            elif self.p2.turn:
                return self.p2, self.p1
            else:
                return None

    def display_text_center(self, message, size, x, y):
        """x = centerX, y = centery"""
        player, other = self.get_player_turn()

        pygame.init()
        font = pygame.font.Font(pygame.font.get_default_font(), size)
        text = font.render(message, False, player.colors['player'])
        text_rect = text.get_rect()
        text_rect.centerx = x
        text_rect.centery = y
        self.screen.blit(text, text_rect)

    def display_text_right(self, message, size, x, y):
        """x = right, y = centery"""
        player, other = self.get_player_turn()

        pygame.init()
        font = pygame.font.Font(pygame.font.get_default_font(), size)
        text = font.render(message, False, player.colors['player'])
        text_rect = text.get_rect()
        text_rect.right = x
        text_rect.centery = y
        self.screen.blit(text, text_rect)

    def check_win(self):
        pass

    def leave_game(self, player):
        if player == self.p1:
            self.p1 = None
            self.game_over = None
        elif player == self.p2:
            self.p2 = None
            self.game_over = None

    def end_game(self):
        player, other = self.get_player_turn()
        print("Player " + str(player.player) + " wins!")
        self.p1 = None
        self.p2 = None
        self.game_over = True
