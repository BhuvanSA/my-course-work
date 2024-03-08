"""
Tic Tac Toe Player
"""

import copy

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
    xCount = oCount = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == X: 
                xCount += 1
            elif board[i][j] == O:
                oCount += 1
    if xCount > oCount:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    moves = set()
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                moves.add((i, j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    nb = copy.deepcopy(board)
    
    curr = player(nb)
    i, j = action 
    if nb[i][j] == EMPTY: 
        nb[i][j] = curr
    else:
        print("Invalid move", i, j)
    
    return nb


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Diagonal Check \
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != EMPTY:
        return board[1][1]

    # Diagonal Check /
    elif board[0][2] == board[1][1] == board[2][0] and board[1][1] != EMPTY:
        return board[1][1]

    # Line Check --- 
    for i in range(0, 3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
    # Line Check |||
    for j in range(0, 3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != EMPTY:
            return board[1][j]
        

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # if there is a winner return true
    if winner(board) != None:
        return True

    # if there is a no moves left return true
    if actions(board) == set():
        return True
    
    # else return false as the game is still on
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

    if player(board) == 'X':
        _, action = maxi(board)
        return action

    else:
        _, action = mini(board)
        return action
    

def maxi(board):

    if terminal(board):
        return utility(board), set()
    v = -100
    bestAction = ""
    for action in actions(board):
        newV, _ = mini(result(board, action))
        if newV > v:
            v = newV
            bestAction = action
            
    return v, bestAction


def mini(board):
    if terminal(board):
        return utility(board), set()
    v = 100
    bestAction = set()
    for action in actions(board):
        newV, _ = maxi(result(board, action))
        if newV < v:
            v = newV
            bestAction = action

    return v, bestAction
