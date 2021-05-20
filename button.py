import pygame
import square


class Button(pygame.Rect):
    def __init__(self, dice, right_board, number, color):
        if number == 1:
            self.x = right_board.board[0][len(right_board.Board.board[0]) - 1].x + right_board.board[0][len(right_board.Board.board[0]) - 1].width - 2 * dice.height
            self.y = dice.y
            self.width = 2 * dice.height
            self.height = dice.height / 2 - 2
        elif number == 2:
            self.x = right_board.board[0][len(right_board.Board.board[0]) - 1].x + right_board.board[0][len(right_board.Board.board[0]) - 1].width - 2 * dice.height
            self.y = dice.y + dice.height / 2
            self.width = 2 * dice.height
            self.height = dice.height / 2 - 2

        pygame.Rect.__init__(self, self.x, self.y, self.width, self.height)
        self.right_board = right_board
        self.number = number
        self.color = color  # color format: [r, g, b]

        self.mask = None
        self.create_mask()

        self.outline = False  # Has outline visible = True/False
        self.outline_rect = None
        self.create_outline_rect()

    def draw(self, screen, engine):
        if self.outline and not self.mask_is_visible():
            self.outline_rect.draw_square(screen)

        pygame.draw.rect(screen, self.color, self)
        self.mask.draw_square(screen)

        # Logic for grayed-out buttons
        if self.number == 1:
            self.mask.set_alpha(128)
            if engine.walls_left()[0] == 0 and engine.walls_left()[1] >= 0:  # If between range of correct # placed
                player, other = engine.get_player_turn()
                if player.wall_time:
                    self.mask.set_alpha(0)
        elif self.number == 2:
            if engine.moves_left() <= 0:
                self.mask.set_alpha(0)
            else:
                self.mask.set_alpha(128)

    def click(self, mouse_pos, engine):
        if self.collidepoint(mouse_pos):
            if not self.mask_is_visible():
                if self.number == 1:
                    engine.end_wall_time()
                elif self.number == 2:
                    engine.switch_turns()
                    engine.set_old_board()

    def resize(self, dice):
        if self.number == 1:
            self.x = self.right_board.board[0][len(self.right_board.Board.board[0]) - 1].x + self.right_board.board[0][
                len(self.right_board.Board.board[0]) - 1].width - 2 * dice.height
            self.y = dice.y
            self.width = 2 * dice.height
            self.height = dice.height / 2 - 2
        elif self.number == 2:
            self.x = self.right_board.board[0][len(self.right_board.Board.board[0]) - 1].x + self.right_board.board[0][
                len(self.right_board.Board.board[0]) - 1].width - 2 * dice.height
            self.y = dice.y + dice.height / 2
            self.width = 2 * dice.height
            self.height = dice.height / 2 - 2

        self.create_mask()
        self.create_outline_rect()

    def create_mask(self):
        self.mask = square.Square(self.x, self.y, self.size[0]+1, self.size[1]+1)
        self.mask.change_fill((0, 0, 0))
        self.mask.set_alpha(128)  # Defaults to showing

    def create_outline_rect(self):
        self.outline_rect = square.Square(self.x - 2, self.y - 2, self.size[0]+4, self.size[1]+4)
        self.outline_rect.change_fill((255, 255, 0))

    def draw_outline_rect(self, mouse_pos):
        if self.collidepoint(mouse_pos):
            self.outline = True
        elif self.outline:
            self.outline = False

    def mask_is_visible(self):
        if self.mask.get_alpha() == 0:
            return False
        else:
            return True
