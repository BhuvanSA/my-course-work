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
    return X if sum(row.count(EMPTY) for row in board) % 2 == 1 else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action")

    # Why does it need to be a deep copy?
    # Because we don't want to modify the original board
    # We want to return a new board with the action applied
    # If we modify the original board, it will be a side effect
    # and the function will not be pure anymore

    new_board = [row.copy() for row in board]
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not None:
            return board[0][j]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # If there is a winner, the game is over
    if winner(board) is not None:
        return True

    # If there are no more empty cells, the game is over
    if all(cell is not None for row in board for cell in row):
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    # If X has won, return 1
    if winner(board) == X:
        return 1

    # If O has won, return -1
    if winner(board) == O:
        return -1

    # If it's a tie, return 0
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # If the game is over, return None
    if terminal(board):
        return None

    # If the player is X, maximize
    if player(board) == X:
        v = -math.inf
        best_action = None
        for action in actions(board):
            min_val = min_value(result(board, action))
            if min_val > v:
                v = min_val
                best_action = action
        return best_action

    # If the player is O, minimize
    if player(board) == O:
        v = math.inf
        best_action = None
        for action in actions(board):
            max_val = max_value(result(board, action))
            if max_val < v:
                v = max_val
                best_action = action
        return best_action


def max_value(board):
    """
    Returns the maximum utility value for the current player on the board.
    """

    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v


def min_value(board):
    """
    Returns the minimum utility value for the current player on the board.
    """

    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v
