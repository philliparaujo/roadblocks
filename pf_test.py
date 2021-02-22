import unittest
import pf
import board


class PathFinderTester(unittest.TestCase):
    def test_sunny(self):
        b = board.Board.Builder([["?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?"],
                                 ["#", " ", " ", " ", " ", " ", " ", "A", "#", " ", "#", " ", " ", " ", "#"],
                                 ["?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?"],
                                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", "#"],
                                 ["?", "#", "?", " ", "?", "#", "?", " ", "?", " ", "?", " ", "?", "#", "?"],
                                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                                 ["?", "#", "?", "#", "?", " ", "?", "#", "?", "#", "?", "#", "?", " ", "?"],
                                 ["#", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                                 ["?", "#", "?", " ", "?", " ", "?", " ", "?", " ", "?", "#", "?", "#", "?"],
                                 ["#", " ", " ", " ", "#", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#"],
                                 ["?", " ", "?", " ", "?", "#", "?", "#", "?", "#", "?", " ", "?", " ", "?"],
                                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", "#"],
                                 ["?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?"],
                                 ["#", " ", " ", " ", " ", " ", " ", "B", "#", " ", "#", " ", " ", " ", "#"],
                                 ["?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?"]]).build()
        sut = pf.PathFinder(b, {'x': 7, 'y': 1}, {'x': 7, 'y': 13})
        result = sut.get_path()
        self.assertEqual(result, "DDLDRRDRDLLD", "did not return correct path")

    def test_skinny_board(self):
        """If the board is not a square, more rows than columns"""
        b = board.Board.Builder([["?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?"],
                                 ["#", " ", " ", " ", " ", " ", " ", "A", "#", " ", "#", " ", "#"],
                                 ["?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?"],
                                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", "#"],
                                 ["?", "#", "?", " ", "?", "#", "?", " ", "?", " ", "?", " ", "?"],
                                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                                 ["?", "#", "?", "#", "?", " ", "?", "#", "?", "#", "?", "#", "?"],
                                 ["#", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#"],
                                 ["?", "#", "?", " ", "?", " ", "?", " ", "?", " ", "?", "#", "?"],
                                 ["#", " ", " ", " ", "#", " ", "#", " ", " ", " ", " ", " ", "#"],
                                 ["?", " ", "?", " ", "?", "#", "?", "#", "?", "#", "?", " ", "?"],
                                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                                 ["?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?"],
                                 ["#", " ", " ", " ", " ", " ", " ", "B", "#", " ", "#", " ", "#"],
                                 ["?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?"]]).build()
        sut = pf.PathFinder(b, {'x': 7, 'y': 1}, {'x': 7, 'y': 13})
        result = sut.get_path()
        self.assertEqual(result, "DDLDRRDRDLLD", "did not return correct path")

    def test_wide_board(self):
        """If the board is not a square, more columns than rows"""
        b = board.Board.Builder([["?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?"],
                                 ["#", " ", " ", " ", " ", " ", " ", "A", "#", " ", "#", " ", " ", " ", "#"],
                                 ["?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?"],
                                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", "#"],
                                 ["?", "#", "?", " ", "?", "#", "?", " ", "?", " ", "?", " ", "?", "#", "?"],
                                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                                 ["?", "#", "?", "#", "?", " ", "?", "#", "?", "#", "?", "#", "?", " ", "?"],
                                 ["#", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                                 ["?", "#", "?", " ", "?", " ", "?", " ", "?", " ", "?", "#", "?", "#", "?"],
                                 ["#", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#"],
                                 ["?", " ", "?", "#", "?", "#", "?", "#", "?", "#", "?", " ", "?", " ", "?"],
                                 ["#", " ", " ", " ", " ", " ", " ", "B", "#", " ", "#", " ", " ", " ", "#"],
                                 ["?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?"]]).build()
        sut = pf.PathFinder(b, {'x': 7, 'y': 1}, {'x': 7, 'y': 11})
        result = sut.get_path()
        self.assertEqual(result, "DDLDDLLDRRR", "did not return correct path")

    def test_a_and_b_same_point(self):
        b = board.Board.Builder([['?', '#', '?', '#', '?'],
                                 ['#', ' ', ' ', ' ', '#'],
                                 ['?', ' ', '?', ' ', '?'],
                                 ['#', ' ', ' ', ' ', '#'],
                                 ['?', '#', '?', '#', '?']]).build()
        with self.assertRaises(pf.SamePointException):
            sut = pf.PathFinder(b, {'x': 1, 'y': 1}, {'x': 1, 'y': 1})

    def test_out_of_bounds_a(self):
        b = board.Board.Builder([['?', '#', '?', '#', '?'],
                                 ['#', ' ', ' ', ' ', '#'],
                                 ['?', ' ', '?', ' ', '?'],
                                 ['#', ' ', ' ', ' ', '#'],
                                 ['?', '#', '?', '#', '?']]).build()
        with self.assertRaises(pf.OutOfBoundsException):
            sut = pf.PathFinder(b, {'x': 0, 'y': 1}, {'x': 2, 'y': 2})

    def test_out_of_bounds_b(self):
        b = board.Board.Builder([['?', '#', '?', '#', '?'],
                                 ['#', ' ', ' ', ' ', '#'],
                                 ['?', ' ', '?', ' ', '?'],
                                 ['#', ' ', ' ', ' ', '#'],
                                 ['?', '#', '?', '#', '?']]).build()
        with self.assertRaises(pf.OutOfBoundsException):
            sut = pf.PathFinder(b, {'x': 1, 'y': 1}, {'x': 3, 'y': 4})

    def test_out_of_bounds_both(self):
        b = board.Board.Builder([['?', '#', '?', '#', '?'],
                                 ['#', ' ', ' ', ' ', '#'],
                                 ['?', ' ', '?', ' ', '?'],
                                 ['#', ' ', ' ', ' ', '#'],
                                 ['?', '#', '?', '#', '?']]).build()
        with self.assertRaises(pf.OutOfBoundsException):
            sut = pf.PathFinder(b, {'x': 0, 'y': 1}, {'x': 3, 'y': 4})

    def test_cornered(self):
        b = board.Board.Builder([['?', '#', '?', '#', '?'],
                                 ['#', ' ', '#', ' ', '#'],
                                 ['?', '#', '?', ' ', '?'],
                                 ['#', ' ', ' ', ' ', '#'],
                                 ['?', '#', '?', '#', '?']]).build()
        sut = pf.PathFinder(b, {'x': 1, 'y': 1}, {'x': 3, 'y': 3})
        with self.assertRaises(pf.NotFoundException):
            sut.get_path()

    def test_not_found(self):
        b = board.Board.Builder([["?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?"],
                                 ["#", " ", " ", " ", " ", " ", " ", "A", "#", " ", "#", " ", " ", " ", "#"],
                                 ["?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?"],
                                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", "#"],
                                 ["?", "#", "?", " ", "?", "#", "?", "#", "?", "#", "?", " ", "?", "#", "?"],
                                 ["#", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                                 ["?", "#", "?", "#", "?", " ", "?", "#", "?", "#", "?", "#", "?", " ", "?"],
                                 ["#", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                                 ["?", "#", "?", " ", "?", " ", "?", " ", "?", " ", "?", "#", "?", "#", "?"],
                                 ["#", " ", " ", " ", "#", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#"],
                                 ["?", " ", "?", " ", "?", "#", "?", "#", "?", "#", "?", " ", "?", " ", "?"],
                                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", "#"],
                                 ["?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?"],
                                 ["#", " ", " ", " ", " ", " ", " ", "B", "#", " ", "#", " ", " ", " ", "#"],
                                 ["?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?"]]).build()
        sut = pf.PathFinder(b, {'x': 7, 'y': 1}, {'x': 7, 'y': 13})
        with self.assertRaises(pf.NotFoundException):
            sut.get_path()

    def test_sinuous_long_path(self):
        b = board.Board.Builder([["?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?"],
                                 ["#", "A", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                                 ["?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", " ", "?"],
                                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                                 ["?", " ", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?"],
                                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                                 ["?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", " ", "?"],
                                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                                 ["?", " ", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?"],
                                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                                 ["?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", " ", "?"],
                                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                                 ["?", " ", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?"],
                                 ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "B", "#"],
                                 ["?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?"]]).build()
        sut = pf.PathFinder(b, {'x': 1, 'y': 1}, {'x': 13, 'y': 13})
        result = sut.get_path()
        self.assertEqual(result, "RRRRRRDLLLLLLDRRRRRRDLLLLLLDRRRRRRDLLLLLLDRRRRRR", "did not return correct path")

    def test_very_large_board(self):
        b = board.Board.Builder([
            ["?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?",
             "#", "?", "#", "?", "#", "?"],
            ["#", "A", " ", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
             " ", " ", " ", " ", " ", "#"],
            ["?", "#", "?", "#", "?", " ", "?", "#", "?", " ", "?", "#", "?", " ", "?", " ", "?", "#", "?", " ", "?",
             " ", "?", " ", "?", " ", "?"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", "#", " ", " ", " ", "#", " ", " ",
             " ", " ", " ", " ", " ", "#"],
            ["?", " ", "?", " ", "?", "#", "?", "#", "?", "#", "?", "#", "?", " ", "?", " ", "?", " ", "?", " ", "?",
             " ", "?", " ", "?", " ", "?"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", "#", " ", " ",
             " ", " ", " ", " ", " ", "#"],
            ["?", " ", "?", " ", "?", " ", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", " ", "?",
             " ", "?", " ", "?", " ", "?"],
            ["#", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ",
             " ", " ", " ", " ", " ", "#"],
            ["?", "#", "?", "#", "?", "#", "?", " ", "?", "#", "?", "#", "?", "#", "?", " ", "?", " ", "?", " ", "?",
             " ", "?", " ", "?", " ", "?"],
            ["#", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ",
             " ", " ", " ", " ", " ", "#"],
            ["?", " ", "?", "#", "?", "#", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?",
             " ", "?", " ", "?", " ", "?"],
            ["#", " ", "#", " ", " ", " ", "#", " ", "#", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
             " ", " ", " ", " ", " ", "#"],
            ["?", "#", "?", " ", "?", "#", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?",
             " ", "?", " ", "?", " ", "?"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
             " ", " ", " ", " ", " ", "#"],
            ["?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?",
             " ", "?", " ", "?", " ", "?"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
             " ", " ", " ", " ", " ", "#"],
            ["?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?",
             " ", "?", " ", "?", " ", "?"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
             " ", " ", " ", " ", " ", "#"],
            ["?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?",
             " ", "?", " ", "?", " ", "?"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
             " ", " ", " ", " ", " ", "#"],
            ["?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?",
             " ", "?", "#", "?", "#", "?"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
             " ", "#", " ", " ", " ", "#"],
            ["?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?",
             "#", "?", " ", "?", "#", "?"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#",
             " ", " ", " ", "#", " ", "#"],
            ["?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?",
             " ", "?", "#", "?", " ", "?"],
            ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
             " ", " ", " ", " ", "B", "#"],
            ["?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?",
             "#", "?", "#", "?", "#", "?"]]).build()
        sut = pf.PathFinder(b, {'x': 1, 'y': 1}, {'x': 25, 'y': 25})
        result = sut.get_path()
        self.assertEqual(result, "RRDLDRDRDDDRUURDRRRRDDDDDDDRRR", "did not return correct path")
