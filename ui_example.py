import board
import pygame
import ui
import ui_error
import pf
import engine
import dice
import button
from pygame.locals import RESIZABLE

# Editable window / board properties
border_size = 15
ratio = 4

screen = pygame.display.set_mode((1200, 800), RESIZABLE)
pygame.display.set_caption("Roadblocks")

engine = engine.Engine(screen)

# Initialize first SquareBoard
b = board.Board.Builder.empty(1)
b.load_from_file("maps\\7x7 maze.txt")
bb = b.build()
ui_board = ui.SquareBoard(b.width(), b.height(), border_size, ratio, bb, True, 1)
engine.create_game(ui_board)

# Initialize second SquareBoard
b2 = board.Board.Builder.empty(2)
b2.load_from_file("maps\\7x7 maze.txt")
bb2 = b2.build()
ui_board2 = ui.SquareBoard(b2.width(), b2.height(), border_size, ratio, bb2, False, 2)
engine.join_game(ui_board2)

# Set wall pieces outside of board
engine.create_wall_pieces()

# Add dice
dice = dice.Dice(ui_board.board[0][0].x, ui_board.board[0][0].y - 1.3*ui_board.board[1][1].width - border_size, 1.3*ui_board.board[1][1].width, [1,2,3,4,5,6])
dice.roll()
dice.create_dots(dice.last_roll)
engine.set_dice(dice)

bt = button.Button(dice, ui_board2, 1, [255, 255, 255])
bt2 = button.Button(dice, ui_board2, 2, [255, 255, 255])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                engine.switch_turns()
                engine.set_old_board()

            if event.key == pygame.K_w:
                engine.end_wall_time()  # Only happens if placed correct # of walls

            if event.key == pygame.K_l:
                engine.leave_game(ui_board2)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            bt.click(pos, engine)
            bt2.click(pos, engine)

            # On click, toggle square color and update game board
            try:
                engine.play(pos)
                engine.recreate_board()  # For when both players overlap
            except pf.SamePointException as e:
                engine.end_game()
            except pf.NotFoundException as e:
                print("ILLEGAL")

        elif event.type == pygame.VIDEORESIZE:
            # When screen is resized, resizes and redraws squares
            engine.recreate_board()

            temp = dice.last_roll
            dice = dice.resize(ui_board.board[0][0].x, ui_board.board[0][0].y - 1.3*ui_board.board[1][1].width - border_size, 1.3*ui_board.board[1][1].width)
            dice.last_roll = temp
            dice.create_dots(dice.last_roll)

            engine.set_dice(dice)
            bt.resize(dice)
            bt2.resize(dice)

    # While running, draw squares
    screen.fill((0, 0, 0))
    engine.draw(bt, bt2)

    pygame.display.update()
