import board
import pygame
from pygame.locals import RESIZABLE

pygame.init()

# Editable window / board properties
border_size = 10
columns = 13
rows = 13
screen = pygame.display.set_mode((800, 600), RESIZABLE)
pygame.display.set_caption("Roadblocks")
screen.fill((0, 0, 0))

# Creates 3 arrays (game board, squares, position of squares)
b = board.Board.Builder.build_empty_board(columns, rows)
ui_board = []
position_board = []

# b.load_from_file("maps\\7x7 maze.txt")
b.fill_borders()
b.build().print()


def create_squares(b):
    width = 0
    height = 0

    for r in range(b.height()):
        row = []
        for c in range(b.width()):
            screen_width, screen_height = pygame.display.get_surface().get_size()

            width = int((screen_width - 3 * border_size - border_size * b.width()) / b.width())
            height = int((screen_height - 3 * border_size - border_size * b.height()) / b.height())

            square = pygame.Surface([width, height])
            square.fill((255, 255, 255))
            row.append(square)

        ui_board.append(row)

    return width, height


width, height = create_squares(b)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            # On click, toggle square color
            for r in range(len(ui_board)):
                for c in range(len(ui_board[0])):
                    if (position_board[r][c][0] < pos[0] < position_board[r][c][0] + width) and \
                            (position_board[r][c][1] < pos[1] < position_board[r][c][1] + height):
                        if pygame.Surface.get_at(screen, position_board[r][c]) == (255, 255, 255, 255):
                            pygame.Surface.fill(ui_board[r][c], (60, 60, 60))
                        elif pygame.Surface.get_at(screen, position_board[r][c]) == (60, 60, 60, 255):
                            pygame.Surface.fill(ui_board[r][c], (255, 255, 255))

        elif event.type == pygame.VIDEORESIZE:
            # When screen is resized, resizes and redraws squares
            ui_board = []
            position_board = []
            width, height = create_squares(b)

    if len(position_board) == 0:
        # On start and when screen resized, fill position_board
        for r in range(len(ui_board)):
            row = []
            for c in range(len(ui_board[0])):
                row.append([2 * border_size + (width + border_size) * r, 2 * border_size + (height + border_size) * c])
            position_board.append(row)

        print(position_board)

    # While running, draw squares
    for r in range(len(ui_board)):
        for c in range(len(ui_board[0])):
            screen.blit(ui_board[r][c],
                        (2 * border_size + (width + border_size) * r, 2 * border_size + (height + border_size) * c))

    pygame.display.update()
