import minesweeper

board = minesweeper.Minesweeper(height=8, width=8, mines=8)


board.print()

print(board.nearby_mines((0, 0)))
