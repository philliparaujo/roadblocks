import unittest
import pygame
import ui
import board
import pf
from pygame.locals import RESIZABLE


class UITester(unittest.TestCase):
    def test_load(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 800), RESIZABLE)
        pygame.display.set_caption("Roadblocks")
        screen.fill((0, 0, 0))

        b = board.Board.Builder.empty()
        b.load_from_file("maps\\7x7 maze.txt")
        bb = b.build()
        ui_board = ui.SquareBoard(b.width(), b.height(), 10, 5, bb, True)
        ui_board.create_squares()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    ui_board.edit_fills(pos)
                elif event.type == pygame.VIDEORESIZE:
                    ui_board.resize_squares()
            ui_board.draw_squares(screen)
            pygame.display.update()
            pygame.time.wait(1000)
            running = False

    def test_update_tile(self):
        # Visual update only
        pygame.init()
        screen = pygame.display.set_mode((1920, 1080), RESIZABLE)
        pygame.display.set_caption("Roadblocks")
        screen.fill((0, 0, 0))

        b1 = board.Board.Builder.empty()
        b1.load_from_file("maps\\7x7 maze.txt")
        b1 = b1.build()
        ui_board = ui.SquareBoard(b1.width(), b1.height(), 10, 5, b1, True)
        ui_board.create_squares()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    running = False
                    pos = pygame.mouse.get_pos()
                    ui_board.edit_fills(pos)
                elif event.type == pygame.VIDEORESIZE:
                    ui_board.resize_squares()
            ui_board.draw_squares(screen)
            pygame.display.update()
            pygame.mouse.set_pos([660, 220])
            pygame.time.wait(100)
            pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN))
        self.assertEqual(screen.get_at((660, 220)), ui_board.colors['yellow'])

    def test_update_color_wall_column(self):
        # Visual update only
        pygame.init()
        screen = pygame.display.set_mode((1920, 1080), RESIZABLE)
        pygame.display.set_caption("Roadblocks")
        screen.fill((0, 0, 0))

        b1 = board.Board.Builder.empty()
        b1.load_from_file("maps\\7x7 maze.txt")
        b1 = b1.build()
        ui_board = ui.SquareBoard(b1.width(), b1.height(), 10, 5, b1, True)
        ui_board.create_squares()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    running = False
                    pos = pygame.mouse.get_pos()
                    ui_board.edit_fills(pos)
                elif event.type == pygame.VIDEORESIZE:
                    ui_board.resize_squares()
            ui_board.draw_squares(screen)
            pygame.display.update()
            pygame.mouse.set_pos([735, 235])
            pygame.time.wait(100)
            pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN))
        self.assertEqual(screen.get_at((735, 235)), ui_board.colors['red'])

    def test_update_color_wall_row(self):
        # Visual update only
        pygame.init()
        screen = pygame.display.set_mode((1920, 1080), RESIZABLE)
        pygame.display.set_caption("Roadblocks")
        screen.fill((0, 0, 0))

        b1 = board.Board.Builder.empty()
        b1.load_from_file("maps\\7x7 maze.txt")
        b1 = b1.build()
        ui_board = ui.SquareBoard(b1.width(), b1.height(), 10, 5, b1, True)
        ui_board.create_squares()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    running = False
                    pos = pygame.mouse.get_pos()
                    ui_board.edit_fills(pos)
                elif event.type == pygame.VIDEORESIZE:
                    ui_board.resize_squares()
            ui_board.draw_squares(screen)
            pygame.display.update()
            pygame.mouse.set_pos([670, 310])
            pygame.time.wait(100)
            pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN))
        self.assertEqual(screen.get_at((670, 310)), ui_board.colors['blue'])

    def test_update_map_wall(self):
        # Visual update only
        pygame.init()
        screen = pygame.display.set_mode((1920, 1080), RESIZABLE)
        pygame.display.set_caption("Roadblocks")
        screen.fill((0, 0, 0))

        b1 = board.Board.Builder.empty()
        b1.load_from_file("maps\\7x7 maze.txt")
        b1 = b1.build()
        ui_board = ui.SquareBoard(b1.width(), b1.height(), 10, 5, b1, True)
        ui_board.create_squares()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    running = False
                    pos = pygame.mouse.get_pos()
                    ui_board.edit_fills(pos)
                elif event.type == pygame.VIDEORESIZE:
                    ui_board.resize_squares()
            ui_board.draw_squares(screen)
            pygame.display.update()
            pygame.mouse.set_pos([590, 240])
            pygame.time.wait(100)
            pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN))
        self.assertEqual(screen.get_at((590, 240)), ui_board.colors['wall'])

    def test_gameboard_sync(self):
        pygame.init()
        screen = pygame.display.set_mode((1920, 1080), RESIZABLE)
        pygame.display.set_caption("Roadblocks")
        screen.fill((0, 0, 0))

        b1 = board.Board.Builder.empty()
        b1.load_from_file("maps\\7x7 maze.txt")
        b1 = b1.build()
        b2 = board.Board.Builder.empty()
        b2.load_from_file("maps\\7x7 maze.txt")
        b2 = b2.build()
        ui_board = ui.SquareBoard(b1.width(), b1.height(), 10, 5, b1, True)
        ui_board.create_squares()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    running = False
                    pos = pygame.mouse.get_pos()
                    ui_board.edit_fills(pos)
                elif event.type == pygame.VIDEORESIZE:
                    ui_board.resize_squares()
            ui_board.draw_squares(screen)
            pygame.display.update()
            pygame.mouse.set_pos([735, 235])
            pygame.time.wait(100)
            pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN))
        b2.set(4, 3, "|")
        self.assertEqual(b1.board, b2.board)

    def test_resize_scale(self):
        pygame.init()
        screen = pygame.display.set_mode((1920, 1060), RESIZABLE)
        pygame.display.set_caption("Roadblocks")
        screen.fill((0, 0, 0))

        b = board.Board.Builder.empty()
        b.load_from_file("maps\\7x7 maze.txt")
        bb = b.build()
        ui_board = ui.SquareBoard(b.width(), b.height(), 10, 5, bb, True)
        ui_board.create_squares()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    ui_board.edit_fills(pos)
                elif event.type == pygame.VIDEORESIZE:
                    ui_board.resize_squares()
                    ui_board.draw_squares(screen)
                    self.assertEqual(screen.get_at((410, 360)), ui_board.colors['wall'])
                    running = False
            ui_board.draw_squares(screen)
            pygame.display.update()

            pygame.time.wait(100)
            screen = pygame.display.set_mode((500, 1000), RESIZABLE)
            pygame.event.post(pygame.event.Event(pygame.VIDEORESIZE))

    def test_resize_stretch(self):
        pygame.init()
        screen = pygame.display.set_mode((1920, 1060), RESIZABLE)
        pygame.display.set_caption("Roadblocks")
        screen.fill((0, 0, 0))

        b = board.Board.Builder.empty()
        b.load_from_file("maps\\7x7 maze.txt")
        bb = b.build()
        ui_board = ui.SquareBoard(b.width(), b.height(), 10, 5, bb, False)
        ui_board.create_squares()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    ui_board.edit_fills(pos)
                elif event.type == pygame.VIDEORESIZE:
                    ui_board.resize_squares()
                    ui_board.draw_squares(screen)
                    self.assertEqual(screen.get_at((410, 220)), ui_board.colors['wall'])
                    running = False
            ui_board.draw_squares(screen)
            pygame.display.update()

            pygame.time.wait(100)
            screen = pygame.display.set_mode((500, 1000), RESIZABLE)
            pygame.event.post(pygame.event.Event(pygame.VIDEORESIZE))

    def test_pathfinder_sync(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 800), RESIZABLE)
        pygame.display.set_caption("Roadblocks")
        screen.fill((0, 0, 0))

        b = board.Board.Builder.empty()
        b.load_from_file("maps\\7x7 maze.txt")
        bb = b.build()
        ui_board = ui.SquareBoard(b.width(), b.height(), 10, 5, bb, True)
        ui_board.create_squares()

        clicked_once = False
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if clicked_once:
                        running = False
                        self.assertEqual(x.get_path(), "LDLDRDDRDD")
                    else:
                        clicked_once = True
                    pos = pygame.mouse.get_pos()
                    ui_board.edit_fills(pos)
                    x = pf.PathFinder(bb, {'x': 7, 'y': 1}, {'x': 7, 'y': 13})
                elif event.type == pygame.VIDEORESIZE:
                    ui_board.resize_squares()

            ui_board.draw_squares(screen)
            pygame.display.update()
            pygame.mouse.set_pos([240, 190])
            pygame.time.wait(100)
            pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN))

            pygame.mouse.set_pos([290, 240])
            pygame.time.wait(100)
            pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN))
