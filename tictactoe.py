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
    # Remember! X Always gets the first move according to the project PDF.
    player_x = 0
    player_o = 0
    # Counts the number of X's and O's on the board. If there are the same amount of X's and O's,
    # then it will return X. Otherwise, it will return O.
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                player_x += 1
            elif board[i][j] == O:
                player_o += 1
    if player_x == player_o:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # This loop goes through every space of the board. Every time it finds an empty space, it adds
    # the empty section to the possible_actions list.
    possible_actions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.append((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board[action[0]][action[1]] = player(board)
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # if the board is terminal, there are no moves to make.
    if terminal(board):
        return utility(board)
    # best_move holds the position of the optimal move for the current player.
    best_move = 0

    for move in actions(board):
        if player(board) == X:
            best_move = max(best_move, minimax(result(board, move)))
        else:
            best_move = min(best_move, minimax(result(board, move)))

    return best_move

