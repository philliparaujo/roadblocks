import pf
import board

b = board.Board.Builder([["?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?"],
                         ["#", " ", " ", " ", " ", " ", " ", "A", "#", " ", "#", " ", " ", " ", "#"],
                         ["?", " ", "?", " ", "?", "#", "?", "#", "?", " ", "?", " ", "?", " ", "?"],
                         ["#", " ", " ", " ", "#", " ", " ", " ", " ", " ", "#", " ", " ", " ", "#"],
                         ["?", "#", "?", " ", "?", "#", "?", " ", "?", " ", "?", " ", "?", "#", "?"],
                         ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
                         ["?", "#", "?", "#", "?", " ", "?", " ", "?", "#", "?", "#", "?", " ", "?"],
                         ["#", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#"],
                         ["?", "#", "?", " ", "?", "#", "?", " ", "?", " ", "?", "#", "?", "#", "?"],
                         ["#", " ", " ", " ", "#", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#"],
                         ["?", " ", "?", " ", "?", "#", "?", "#", "?", "#", "?", " ", "?", " ", "?"],
                         ["#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", "#"],
                         ["?", " ", "?", "#", "?", " ", "?", " ", "?", " ", "?", " ", "?", " ", "?"],
                         ["#", " ", " ", " ", " ", " ", "#", "B", "#", " ", "#", " ", " ", " ", "#"],
                         ["?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?", "#", "?"]]).build()

#b = board.Board.Builder.empty()
x = pf.PathFinder(b, {'x': 7, 'y': 1}, {'x': 7, 'y': 13})
print(x.get_path())
