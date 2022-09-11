X = "X"
O = "O"
EMPTY = None
from tictactoe import winner



board = [[X, X, X],
         [X, O, EMPTY],
         [O, EMPTY, EMPTY]]


print(winner(board))