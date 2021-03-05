import queue


class PathFinder:
    """A class to find the shortest path on a board between two tiles."""

    def __init__(self, board, start, end):
        """
        :param board: A Board object representing the board
        :param start: the starting point. dict('x', 'y')
        :param end: the end point. dict('x', 'y')
        :return: a PathFinder
        """

        if start['x'] == end['x'] and start['y'] == end['y']:
            # Same point
            raise SamePointException()
        elif start['x'] < 1 or start['y'] < 1 or start['x'] > board.width() - 2 or start['y'] > board.height() - 2:
            # Start point out of bounds
            raise OutOfBoundsException()
        elif end['x'] < 1 or end['y'] < 1 or end['x'] > board.width() - 2 or end['y'] > board.height() - 2:
            # End point out of bounds
            raise OutOfBoundsException()

        self.board = board
        self.start = start
        self.end = end

    def move(self, path):
        """Gets the coordinate of a path originating from a starting coordinate (self.start)

        :param path: a string with "U" (up) "D" (down) "L" (left) "R" (right) sequence
        :return: a dict('x', 'y')
        """

        end_coord = {'x': self.start['x'], 'y': self.start['y']}

        for d in range(len(path)):
            tempx = end_coord['x']
            tempy = end_coord['y']

            if path[d] == "L":
                end_coord['x'] -= 2
            elif path[d] == "R":
                end_coord['x'] += 2
            elif path[d] == "U":
                end_coord['y'] -= 2
            elif path[d] == "D":
                end_coord['y'] += 2

            avg_x = int((tempx + end_coord['x']) / 2)
            avg_y = int((tempy + end_coord['y']) / 2)

            if self.board.get(avg_x, avg_y) == "#" or \
                    self.board.get(avg_x, avg_y) == "|" or \
                    self.board.get(avg_x, avg_y) == "-":
                raise CantMoveHitWall()

        if end_coord['x'] < 1 or end_coord['y'] < 1 \
                or end_coord['x'] > self.board.width() - 2 or end_coord['y'] > self.board.height() - 2:
            raise CantMoveOutOfBoard()

        return end_coord

    def get_path(self):
        """Gets the shortest path between two positions in the board.
        Note: A (0 by 0) grid returns NotFoundException

        :return: a string with "U" (up) "D" (down) "L" (left) "R" (right) sequence to get from A to B.
        """

        q = queue.Queue()  # Iterates through items in queue, replaces with longer paths using recursion
        prev_coords = []  # Stores previous coordinates to compare against
        visited = []  # Stores previous paths

        while True:
            if q.qsize() > 0:
                current_path = q.get()
            else:
                current_path = ""

            for d in ["L", "R", "U", "D"]:
                new_path = current_path + d

                if new_path in visited:
                    """If we repeated a path, it means there is __for sure__ no valid path."""
                    raise NotFoundException()
                else:
                    visited.append(new_path)

                try:
                    new_coord = self.move(new_path)
                    count_diff_ends = 0
                    for positions in prev_coords:
                        if not (new_coord == positions):
                            count_diff_ends += 1
                    if count_diff_ends == len(prev_coords):
                        prev_coords.append(new_coord)
                        q.put(new_path)
                        if new_coord == self.end:
                            return new_path
                except CantMoveException:
                    pass


class OutOfBoundsException(Exception):
    pass


class SamePointException(Exception):
    pass


class NotFoundException(Exception):
    pass


class InvalidBoardException(Exception):
    pass


class CantMoveException(Exception):
    pass


class CantMoveHitWall(CantMoveException):
    pass


class CantMoveOutOfBoard(CantMoveException):
    pass
