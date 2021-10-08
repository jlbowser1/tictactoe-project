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
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """# horizontal 
    for i in range(3):
        if ((board[i][0] == board [i][1] ==board [i][2]) and != EMPTY):
           if (board[i][1] == X):
           return X
           else:
           return O
    
           # Column
    for i in range(3)
        if ((board[0][i] == board[1][i]== board[2][i]) and != EMPTY):
         if (board[1][i] == X):
           return X
           else:
           return O
    
    #diagonal
    if((board[0][0] == board[1][1]== board[2][2]) and != EMPTY):
         if (board[1][1] == X):
           return X
           else:
           return O

    #diagonal
    else if((board[0][2]==board[1][1]==board[2][0]) and != EMPTY):
         if (board[1][1] == X):
           return X
           else:
           return O
    
           #counter check for EMPTY spaces
    count =0
    for i in range(3):
        for j in range(3):
            if(board[i][j] != EMPTY):
            count++
    if (count == 9):
    return None
    else:
    break
        'raise NotImplementedError
        

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    'call winner to check for a possible winner
    if (winner == None || winner == X || winner == O):
    return True
    else:
    return False

    'raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
   'returns applicable number value for winner.
    if (winner == X):
    return 1
    else if (winner == O):
    return -1
    else:
    return 0
   
    'raise NotImplementedError 


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
