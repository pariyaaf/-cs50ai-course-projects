"""
Tic Tac Toe Player
"""

import math
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
    count_x = sum(row.count(X) for row in board)
    count_o =  sum(row.count(O) for row in board)
    if count_x > count_o:
        return O
    return X
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i,j))
    return actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid action: cell is not empty")

    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board
    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[1][1]

    if board[0][2] == board[1][1] == board[2][0]  != EMPTY:
        return board[1][1]

    
    return None
    



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)

    # raise NotImplementedError


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

    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    player_turn = player(board)
    if player_turn == X:
        return max_value(board)[1]  
    return min_value(board)[1] 


def max_value(board):
    if terminal(board):
        return utility(board), None 
    v = -2**10
    best_move = None
    for action in actions(board):
        value = min_value(result(board, action))[0]
        if value > v:
            v = value
            best_move = action
    return v, best_move 


def min_value(board):
    if terminal(board):
        return utility(board), None
    v = 2**10
    best_move = None
    for action in actions(board):
        value = max_value(result(board, action))[0] 
        if value < v:
            v = value
            best_move = action
    return v, best_move 
