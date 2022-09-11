import copy
"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    amount = 0
    for row in board:
        amount += (row.count(X)+row.count(O))
    if amount % 2 == 0:
        return X
    elif amount % 2 == 1:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    allactions = set()
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == EMPTY:
                allactions.add((x,y))
    return allactions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    tempboard = copy.deepcopy(board)
    if tempboard[action[0]][action[1]] == EMPTY:
        tempboard[action[0]][action[1]] = player(board)
    else:
        raise Exception("Not valid action")




def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #check rows
    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O
    #check column
    for x in range(len(board)):
        currentcol = []
        for y in range(len(board)):
            currentcol.append(board[y][x])
        if currentcol.count(X) == 3:
            return X
        elif currentcol.count(O) == 3:
            return O
    #check diagonals
    diagonals = [[board[0][0]] + [board[1][1]] + [board [2][2]], [board[2][0]] + [board[1][1]] + [board [0][2]]]
    for diagonal in diagonals:
        if diagonal.count(X) == 3:
            return X
        elif diagonal.count(O) == 3:
            return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    emptycount = 0
    for row in board:
        emptycount += row.count(EMPTY)
    if winner(board) != None or emptycount == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return (2,2)
    return (0,0)
