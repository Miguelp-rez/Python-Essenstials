# Filling a list using list comprehension
WHITE_PAWN = 'i'
row = [WHITE_PAWN for i in range(8)]
print(row)

# Example two 
squares = [x ** 2 for x in range(10)]
print(squares)

# Example three
twos = [2 ** i for i in range(8)]
print(twos)

# Example four
odds = [x for x in squares if x % 2 != 0]
print(odds)

EMPTY = "."
# Filling a matrix using list comprehension
board = [[EMPTY for i in range(8)] for i in range(8)]
for row in board:
    print(row)

EMPTY = "-"
PAWN = "PAWN"
KNIGHT = "KNIGHT"
BISHOP = "BISHOP"
QUEEN = "QUEEN"
KING = "KING"
ROOK = "ROOK"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

# Filling row 8
board[0][0] = ROOK
board[0][1] = KNIGHT
board[0][2] = BISHOP
board[0][3] = QUEEN
board[0][4] = KNIGHT
board[0][5] = BISHOP
board[0][6] = KNIGHT
board[0][7] = ROOK
# Filling row 7
board[1][0] = PAWN
board[1][1] = PAWN
board[1][2] = PAWN
board[1][3] = PAWN
board[1][4] = PAWN
board[1][5] = PAWN
board[1][6] = PAWN
board[1][7] = PAWN
# Filling row 2
board[6][0] = PAWN
board[6][1] = PAWN
board[6][2] = PAWN
board[6][3] = PAWN
board[6][4] = PAWN
board[6][5] = PAWN
board[6][6] = PAWN
board[6][7] = PAWN
# Filling row 1
board[7][0] = ROOK
board[7][1] = KNIGHT
board[7][2] = BISHOP
board[7][3] = QUEEN
board[7][4] = KNIGHT
board[7][5] = BISHOP
board[7][6] = KNIGHT
board[7][7] = ROOK

for row in board:
    print(row)
