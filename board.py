magic_create_key = "TheQuickBrownFox"


class Board:
    class Builder:
        def __init__(self, board):
            if len(board) == 0:
                raise InvalidBoardException("Board is empty")
            self.board = board
            self.min_array_size = 5  # Min board size is 3
            self.start_char = "A"
            self.end_char = "B"

        @staticmethod
        def empty():
            return Board.Builder([[]])

        def load_from_file(self, file_name):
            """
            :param file_name: The file where the board will be derived from
            :return: None, but the resulting array board will be stored in self.board
            """
            board_file = open(file_name, "r")

            # Get rows and columns from text file
            rows = 0
            cols = 0
            for line in board_file:
                if rows == 0:
                    cols = len(line)
                rows += 1

            # Checks if line lengths are consistent
            current_row = 0
            for line in board_file:
                if len(line) != cols and current_row != rows:
                    board_file.close()
                    raise InvalidBoardException("Inconsistent line lengths")
                current_row += 1

            board_file.seek(0)  # Return to the start of the text file
            cols = int(cols / 2)

            # Makes array
            if rows >= self.min_array_size and cols >= self.min_array_size:
                file_array = self.build_empty_board(rows, cols)
            else:
                board_file.close()
                raise InvalidBoardException("Board too small")

            # Fills the array
            previous_element = ""
            for r in range(len(file_array)):
                for c in range(len(file_array[0])):
                    # Checks consistency of inner walls
                    if not (r == 0 and c == 0):
                        previous_element = next_array_element
                    next_array_element = board_file.read(2)
                    if not (r == 0 and c == 0):
                        if c % 2 == 1:
                            if previous_element[1] != next_array_element[1]:
                                board_file.close()
                                raise InvalidBoardException("Invalid inner walls")

                    if next_array_element[0] == "+":
                        file_array[r][c] = "?"
                    elif next_array_element[0] == "/" or next_array_element[0] == "\\":
                        file_array[r][c] = "?"
                    elif next_array_element[0] == "|":
                        file_array[r][c] = "#"
                    elif next_array_element[0] == "-":
                        if next_array_element[1] == next_array_element[0]:
                            file_array[r][c] = "#"
                        else:
                            board_file.close()
                            raise InvalidBoardException("Invalid inner walls")
                    elif next_array_element[0] == " ":
                        if next_array_element[1] == next_array_element[0]:
                            file_array[r][c] = " "
                        else:
                            board_file.close()
                            raise InvalidBoardException("Invalid inner walls")
                    elif next_array_element[0] == self.start_char:
                        file_array[r][c] = self.start_char
                    elif next_array_element[0] == self.end_char:
                        file_array[r][c] = self.end_char

            self.board = file_array
            board_file.close()

        def save_to_file(self, file_name):
            """
            :param file_name: The file where the board will be written onto
            :return: None, but the resulting text board will be written in the file given
            """
            new_file = open(file_name, "w")
            for r in range(len(self.board)):
                current_line = ""
                for c in range(len(self.board[0])):
                    # Corners
                    if r == 0 and c == 0:
                        current_line += "/-"
                    elif r == 0 and c == len(self.board[0]) - 1:
                        current_line += "\\"
                    elif r == len(self.board) - 1 and c == 0:
                        current_line += "\\-"
                    elif r == len(self.board) - 1 and c == len(self.board[0]) - 1:
                        current_line += "/"

                    # Regular elements
                    elif self.board[r][c] == "#":
                        if r % 2 == 0:
                            current_line += "--"
                        else:
                            if c == len(self.board[0]) - 1:
                                current_line += "|"
                            else:
                                current_line += "| "
                    elif self.board[r][c] == " ":
                        current_line += "  "
                    elif self.board[r][c] == "?":
                        if c == len(self.board[0]) - 1:
                            current_line += "+"
                        elif self.board[r][c + 1] == " ":
                            current_line += "+ "
                        elif self.board[r][c + 1] == "#":
                            current_line += "+-"
                    elif self.board[r][c] == self.start_char:
                        current_line += (self.start_char + " ")
                    elif self.board[r][c] == self.end_char:
                        current_line += (self.end_char + " ")
                new_file.write(current_line + "\n")
            new_file.close()

        def clear(self):
            self.board = Board.Builder.empty().board
            return self

        def append_row(self, cols):
            row = []
            for c in range(cols):
                row.append(" ")

            self.board.append(row)
            return self

        def set(self, x, y, what):
            self.board[y][x] = what
            return self

        def width(self):
            return len(self.board[0])

        def height(self):
            return len(self.board)

        @staticmethod
        def build_empty_board(rows, cols):
            """
            :param rows: The # of rows (int) for the array
            :param cols: The # of columns (int) for the array
            :return: A new empty array with the given rows and columns
            """

            new_board = []

            for r in range(rows):
                row = []
                for c in range(cols):
                    row.append(" ")
                new_board.append(row)

            return new_board

        def fill_borders(self):
            """ Fills outer walls with #?#?#? pattern and fills corners with ?"""

            for r in range(len(self.board)):
                # Fills outer columns with ?#?#?# pattern
                if r % 2 == 0:
                    self.board[r][0] = "?"
                    self.board[r][len(self.board[0]) - 1] = "?"
                else:
                    self.board[r][0] = "#"
                    self.board[r][len(self.board[0]) - 1] = "#"

            for c in range(len(self.board[0])):
                # Fills outers rows with ?#?#?# pattern
                if c % 2 == 0:
                    self.board[0][c] = "?"
                    self.board[len(self.board) - 1][c] = "?"
                else:
                    self.board[0][c] = "#"
                    self.board[len(self.board) - 1][c] = "#"

            for r in range(len(self.board)):
                for c in range(len(self.board[0])):
                    if r % 2 == 0 and c % 2 == 0:
                        self.board[r][c] = "?"

        def validate(self):
            """
            :return: None if no exceptions are raised, exceptions make sure the board fit all needed criteria
            """
            if self.width() < self.min_array_size or self.height() < self.min_array_size:
                # Board too small
                raise InvalidBoardException("Board too small")

            for r in range(len(self.board)):
                # Checking if outer wall columns follow ?#?#?# pattern
                if r % 2 == 0:
                    if not (self.board[r][0] == "?" and self.board[r][len(self.board[0]) - 1] == "?"):
                        raise InvalidBoardException("Invalid outer columns")
                else:
                    if not (self.board[r][0] == "#" and self.board[r][len(self.board[0]) - 1] == "#"):
                        raise InvalidBoardException("Invalid outer columns")

            for c in range(len(self.board[0])):
                # Checking if outer wall rows follow ?#?#?# pattern
                if c % 2 == 0:
                    if not (self.board[0][c] == "?" and self.board[len(self.board) - 1][c] == "?"):
                        raise InvalidBoardException("Invalid outer rows")
                else:
                    if not (self.board[0][c] == "#" and self.board[len(self.board) - 1][c] == "#"):
                        raise InvalidBoardException("Invalid outer rows")

            for r in range(len(self.board)):
                for c in range(len(self.board[0])):
                    tile = self.board[r][c]
                    if tile == "#" and (r + c) % 2 == 0:
                        # Wall is not placed on edge
                        raise InvalidBoardException("Invalid wall placement")
                    if tile == "?" and not (r % 2 == 0 or c % 2 == 0):
                        # Corner is not placed on corner
                        raise InvalidBoardException("Invalid corner placement")

        def build(self):
            """
            :return: A new Board object using the map created by the Builder
            """
            self.validate()
            return Board(magic_create_key, self.board)

    def __init__(self, magic, board):
        """
        :param magic: A key that prevents a Board object to be created without the Builder
        :param board: The 2D board array to be built and edited
        """
        if magic != magic_create_key:
            raise Exception("Can't create directly")
        self.board = board

    def set(self, x, y, what):
        """
        :param x: The x index of the array (different from cols)
        :param y: The y index of the array (different from rows)
        :param what: The string value to be written
        """
        self.board[y][x] = what

    def get(self, x, y):
        return self.board[y][x]

    def get_start_pos(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                if self.board[r][c] == "A":
                    return {'x': c, 'y': r}

    def width(self):
        return len(self.board[0])

    def height(self):
        return len(self.board)

    def print(self):
        """ Prints the board, row by row
        :return: The array output of the print, to test the value of in board_test
        """
        output = []
        for r in range(len(self.board)):
            print(self.board[r])
            output.append(self.board[r])
        return output


class InvalidBoardException(Exception):
    def __init__(self, why):
        self.why = why
