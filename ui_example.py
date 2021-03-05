import board
import pygame
import ui
import pf
from pygame.locals import RESIZABLE

pygame.init()

# Editable window / board properties
border_size = 10
ratio = 5
scale = True

screen = pygame.display.set_mode((800, 800), RESIZABLE)
pygame.display.set_caption("Roadblocks")
screen.fill((0, 0, 0))

# columns = 15
# rows = 15
# b = board.Board.Builder.build_empty_board(columns, rows)
# b.fill_borders()
b = board.Board.Builder.empty()
b.load_from_file("maps\\7x7 maze.txt")
bb = b.build()

ui_board = ui.SquareBoard(b.width(), b.height(), border_size, ratio, bb, scale)
ui_board.create_squares()

x = pf.PathFinder(bb, {'x': 7, 'y': 1}, {'x': 7, 'y': 13})

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            # On click, toggle square color and update game board
            ui_board.edit_fills(pos)
            x = pf.PathFinder(bb, bb.get_start_pos(), x.end)
            print(x.get_path())
            #print(pos)
            #bb.print()

        elif event.type == pygame.VIDEORESIZE:
            # When screen is resized, resizes and redraws squares
            ui_board.resize_squares()

    # While running, draw squares
    ui_board.draw_squares(screen)
    pygame.display.update()

#bb.print()
