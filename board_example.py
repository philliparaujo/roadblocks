import board

# ###?????
# testBoard = board.Board([])
# testBoard.build_board(7, 7)
# testBoard.set("A", 7, 1)
# testBoard.set("B", 7, 13)
# testBoard.print_board()
#
# ## ?????
#
# board = board.Board.Builder() \
#     .dimensions(4, 4) \
#     .fill_borders() \
#     .build()
#

builder = board.Board.Builder.empty()
builder.load_from_file("maps\\7x7 maze.txt")
builder.build().print()

builder.save_to_file("test_maps\\test_save.txt")
# builder.build().print()
