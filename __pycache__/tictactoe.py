from tabnanny import check


def printboard(board):
    for row in board:
        print("|".join(row))


board = [
    ["o", "x", " "],
    ["o", "o", "o"],
    [" ", " ", " "],
]


def checkwinner(board):
    if (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]) and board[1][1] != " ":
        return board[1][1]
    for x in range(3):
        if board[0][x] == board[1][x] == board[2][x] and board[0][x] != " ":
            return board[0][x]
        elif board[x][0] == board[x][1] == board[x][2] and board[x][0] != " ":
            return board[x][0]
    return False

def makeboard():
    return [[" " for x in range(3)] for x in range(3)]


def availablemoves(board):
    moves = []
    for row in range(len(board)):
        for item in range(len(board[row])):
            if board[row][item] == " ":
                moves.append((row, item))
    return moves

def makemove(square, letter):
    board[square[0]][square[1]] = letter


def converttosquare(num):
    return (num // 3 , num % 3)

print(availablemoves(board))

# winner = checkwinner(board)
# if winner:
#     print(winner)
# else:
#     print("No winner, srry")
