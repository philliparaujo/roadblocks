import unittest
import board


class BoardTester(unittest.TestCase):
    def test_set(self):
        b = board.Board.Builder.empty()
        b.load_from_file("test_maps\\2x2_empty.txt")
        b = b.build()

        b.set(2, 1, " ")
        b.set(2, 3, " ")

        self.assertEqual(b.board, [["?", "#", "?", "#", "?"],
                                   ["#", " ", " ", " ", "#"],
                                   ["?", " ", "?", " ", "?"],
                                   ["#", " ", " ", " ", "#"],
                                   ["?", "#", "?", "#", "?"]])

    def test_get(self):
        b = board.Board.Builder.empty()
        b.load_from_file("test_maps\\2x2_empty.txt")
        b = b.build()
        self.assertEqual(b.get(2, 2), "?")

    def test_width(self):
        b = board.Board.Builder([["?", "#", "?", "#", "?", "#", "?"],
                                 ["#", " ", " ", " ", "#", " ", "#"],
                                 ["?", " ", "?", " ", "?", " ", "?"],
                                 ["#", " ", "#", " ", " ", " ", "#"],
                                 ["?", "#", "?", "#", "?", "#", "?"]]).build()
        self.assertEqual(b.width(), 7)

    def test_height(self):
        b = board.Board.Builder([["?", "#", "?", "#", "?"],
                                 ["#", " ", " ", " ", "#"],
                                 ["?", " ", "?", " ", "?"],
                                 ["#", " ", " ", " ", "#"],
                                 ["?", " ", "?", " ", "?"],
                                 ["#", " ", " ", " ", "#"],
                                 ["?", " ", "?", " ", "?"],
                                 ["#", " ", " ", " ", "#"],
                                 ["?", "#", "?", "#", "?"]]).build()
        self.assertEqual(b.height(), 9)

    def test_print(self):
        b = board.Board.Builder.empty()
        b.load_from_file("test_maps\\2x2_empty.txt")
        b = b.build()
        self.assertEqual(b.print(), b.board)
