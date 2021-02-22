import unittest
import board


class BoardBuilderTest(unittest.TestCase):
    def test_initialize(self):
        b = board.Board.Builder([["?", "#", "?", "#", "?"],
                                 ["#", " ", " ", " ", "#"],
                                 ["?", "#", "?", " ", "?"],
                                 ["#", " ", " ", " ", "#"],
                                 ["?", "#", "?", "#", "?"]])

        self.assertEqual(b.board, [["?", "#", "?", "#", "?"],
                                   ["#", " ", " ", " ", "#"],
                                   ["?", "#", "?", " ", "?"],
                                   ["#", " ", " ", " ", "#"],
                                   ["?", "#", "?", "#", "?"]])

    def test_empty(self):
        b = board.Board.Builder.empty()
        self.assertEqual(b.board, [[]])

    def test_clear(self):
        b = board.Board.Builder([["?", "#", "?", "#", "?"]])
        b.clear()
        self.assertEqual(b.board, board.Board.Builder.empty().board)

    def test_append_rows(self):
        b = board.Board.Builder([["?", "#", "?", "#", "?"]])
        b.append_row(5) \
            .append_row(5) \
            .append_row(5) \
            .append_row(5)
        self.assertEqual(b.board, [["?", "#", "?", "#", "?"],
                                   [" ", " ", " ", " ", " "],
                                   [" ", " ", " ", " ", " "],
                                   [" ", " ", " ", " ", " "],
                                   [" ", " ", " ", " ", " "]])

    def test_set(self):
        b = board.Board.Builder([["?", "#", "?", "#", "?"]])
        b.set(1, 0, " ")
        b.set(3, 0, " ")
        self.assertEqual(b.board, [["?", " ", "?", " ", "?"]])

    def test_validate_when_normal(self):
        b = board.Board.Builder([["?", "#", "?", "#", "?"],
                                 ["#", " ", " ", " ", "#"],
                                 ["?", "#", "?", " ", "?"],
                                 ["#", " ", " ", " ", "#"],
                                 ["?", "#", "?", "#", "?"]])
        b.validate()

    def test_validate_checks_size_width(self):
        b = board.Board.Builder([["?", "#", "?"],
                                 ["#", " ", "#"],
                                 ["?", " ", "?"],
                                 ["#", " ", "#"],
                                 ["?", "#", "?"]])
        with self.assertRaises(board.InvalidBoardException):
            b.validate()

    def test_validate_checks_size_height(self):
        b = board.Board.Builder([["?", "#", "?", "#", "?"],
                                 ["#", " ", "#", " ", "?"],
                                 ["?", "#", "?", "#", "?"]])
        with self.assertRaises(board.InvalidBoardException):
            b.validate()

    def test_validate_checks_columns(self):
        b = board.Board.Builder([["?", "#", "?", "#", "?"],
                                 [" ", " ", " ", " ", "?"],
                                 ["#", " ", " ", " ", " "],
                                 ["?", " ", " ", " ", "#"],
                                 ["?", "#", "?", "#", "?"]])
        with self.assertRaises(board.InvalidBoardException):
            b.validate()

    def test_validate_checks_rows(self):
        b = board.Board.Builder([["?", "?", " ", "#", "?"],
                                 ["#", " ", " ", " ", "#"],
                                 ["?", " ", " ", " ", "?"],
                                 ["#", " ", " ", " ", "#"],
                                 ["?", "#", "#", "#", "?"]])
        with self.assertRaises(board.InvalidBoardException):
            b.validate()

    def test_build_passthru(self):
        b = board.Board.Builder([["?", "#", "?", "#", "?"],
                                 ["#", " ", " ", " ", "#"],
                                 ["?", "#", "?", " ", "?"],
                                 ["#", " ", " ", " ", "#"],
                                 ["?", "#", "?", "#", "?"]])
        b.validate()
        self.assertEqual(b.build().board, [["?", "#", "?", "#", "?"],
                                           ["#", " ", " ", " ", "#"],
                                           ["?", "#", "?", " ", "?"],
                                           ["#", " ", " ", " ", "#"],
                                           ["?", "#", "?", "#", "?"]])

    def test_load_success(self):
        b = board.Board.Builder.empty()
        b.load_from_file("maps\\7x7 maze.txt")
        self.assertEqual(b.build().board,
                         [['?', '#', '?', '#', '?', '#', '?', '#', '?', '#', '?', '#', '?', '#', '?'],
                          ['#', ' ', ' ', ' ', '#', ' ', ' ', 'A', ' ', ' ', '#', ' ', ' ', ' ', '#'],
                          ['?', ' ', '?', '#', '?', ' ', '?', '#', '?', ' ', '?', '#', '?', ' ', '?'],
                          ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
                          ['?', '#', '?', ' ', '?', ' ', '?', ' ', '?', '#', '?', ' ', '?', '#', '?'],
                          ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                          ['?', ' ', '?', '#', '?', ' ', '?', ' ', '?', ' ', '?', '#', '?', ' ', '?'],
                          ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
                          ['?', ' ', '?', ' ', '?', ' ', '?', '#', '?', ' ', '?', ' ', '?', '#', '?'],
                          ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
                          ['?', '#', '?', ' ', '?', ' ', '?', ' ', '?', '#', '?', ' ', '?', '#', '?'],
                          ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
                          ['?', ' ', '?', '#', '?', ' ', '?', ' ', '?', ' ', '?', '#', '?', ' ', '?'],
                          ['#', ' ', ' ', ' ', '#', ' ', ' ', 'B', '#', ' ', '#', ' ', ' ', ' ', '#'],
                          ['?', '#', '?', '#', '?', '#', '?', '#', '?', '#', '?', '#', '?', '#', '?']])

    def test_load_empty_file(self):
        b = board.Board.Builder.empty()
        with self.assertRaises(board.InvalidBoardException):
            b.load_from_file("test_maps\\empty.txt")

    def test_load_inconsistent_borders_1(self):
        """ --. """
        b = board.Board.Builder.empty()
        with self.assertRaises(board.InvalidBoardException):
            b.load_from_file("test_maps\\inconsistent_borders1.txt")

    def test_load_inconsistent_borders_2(self):
        """ .-- """
        b = board.Board.Builder.empty()
        with self.assertRaises(board.InvalidBoardException):
            b.load_from_file("test_maps\\inconsistent_borders2.txt")

    def test_load_inconsistent_borders_3(self):
        """ .-. """
        b = board.Board.Builder.empty()
        with self.assertRaises(board.InvalidBoardException):
            b.load_from_file("test_maps\\inconsistent_borders3.txt")

    def test_load_inconsistent_borders_4(self):
        """ -.- """
        b = board.Board.Builder.empty()
        with self.assertRaises(board.InvalidBoardException):
            b.load_from_file("test_maps\\inconsistent_borders4.txt")

    def test_load_border_where_player_should_be(self):
        b = board.Board.Builder.empty()
        with self.assertRaises(board.InvalidBoardException):
            b.load_from_file("test_maps\\inconsistent_border_player.txt")

    def test_load_player_where_border_should_be(self):
        b = board.Board.Builder.empty()
        with self.assertRaises(board.InvalidBoardException):
            b.load_from_file("test_maps\\inconsistent_player_border.txt")

    def test_load_inconsistent_line_lengths(self):
        b = board.Board.Builder.empty()
        with self.assertRaises(board.InvalidBoardException):
            b.load_from_file("test_maps\\inconsistent_line_lengths.txt")

    def test_save(self):
        b = board.Board.Builder.empty()
        b.load_from_file("maps\\7x7 maze.txt")
        og_board = b.board

        b.save_to_file("test_maps\\test_save.txt")
        b.load_from_file("test_maps\\test_save.txt")
        self.assertEqual(og_board, b.board)
