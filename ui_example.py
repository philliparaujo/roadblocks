import board
import pygame
import ui
import pf
from pygame.locals import RESIZABLE

pygame.init()

# Editable window / board properties
border_size = 15
ratio = 4

screen = pygame.display.set_mode((1200, 600), RESIZABLE)
pygame.display.set_caption("Roadblocks1")
screen.fill((0, 0, 0))

# columns = 15
# rows = 15
# b = board.Board.Builder.build_empty_board(columns, rows)
# b.fill_borders()

# Initialize first SquareBoard
b = board.Board.Builder.empty(1)
b.load_from_file("maps\\7x7 maze.txt")
bb = b.build()
ui_board = ui.SquareBoard(b.width(), b.height(), border_size, ratio, bb, True, 1)
ui_board.create_squares()
x = pf.PathFinder(ui_board.Board, {'x': 7, 'y': 1}, {'x': 7, 'y': 13})

# Initialize second SquareBoard
b2 = board.Board.Builder.empty(2)
b2.load_from_file("maps\\7x7 maze.txt")
bb2 = b2.build()
ui_board2 = ui.SquareBoard(b2.width(), b2.height(), border_size, ratio, bb2, False, 2)
ui_board2.create_squares()
y = pf.PathFinder(ui_board2.Board, {'x': 1, 'y': 7}, {'x': 13, 'y': 7})


# Set visual fills for other player's start and end
ui_board.set_opponent_tiles(ui_board2)
ui_board2.set_opponent_tiles(ui_board)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if ui_board.turn:
                    ui_board.end_turn()
                    ui_board2.start_turn()
                    pygame.display.set_caption("Roadblocks2")
                elif ui_board2.turn:
                    ui_board2.end_turn()
                    ui_board.start_turn()
                    pygame.display.set_caption("Roadblocks1")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            # On click, toggle square color and update game board
            if ui_board.turn:
                ui_board.edit_fills(pos, ui_board2)
                x = pf.PathFinder(ui_board.Board, ui_board.Board.get_start_pos(), x.end)
                print(x.get_path())
                ui_board.Board.print()
            elif ui_board2.turn:
                ui_board2.edit_fills(pos, ui_board)
                y = pf.PathFinder(ui_board2.Board, ui_board2.Board.get_start_pos(), y.end)
                print(y.get_path())
                ui_board2.Board.print()

            #print(pos)

        elif event.type == pygame.VIDEORESIZE:
            # When screen is resized, resizes and redraws squares
            ui_board.resize_squares(ui_board2)
            ui_board2.resize_squares(ui_board)

    # While running, draw squares
    ui_board.draw_squares(screen)
    ui_board2.draw_squares(screen)
    pygame.display.update()

#ui_board.Board.print()
