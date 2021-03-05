import board

builder = board.Board.Builder.empty()
builder.load_from_file("maps\\7x7 maze.txt")
builder.build().print()

builder.save_to_file("test_maps\\test_save.txt")
