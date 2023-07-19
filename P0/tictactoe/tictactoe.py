"""
Tic Tac Toe Player
"""

import math, copy

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
    # raise NotImplementedError
    count = 0
    for row in board:
        for element in row:
            if element is EMPTY:
                count += 1

    print(count)

    if count == 9:
        return X 
    
    if count % 2 == 0: 
        return O
    else:
        return X 
    
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    result = set()
    for i, row in enumerate(board):
        for j, element in enumerate(row):
            if element is EMPTY:
                result.add((i, j))
    return result


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # raise NotImplementedError
    board2 = copy.deepcopy(board)
    move = player(board2)

    if action not in actions(board2):
        raise Exception('Error: Invalid Move')
    
    i, j = action
    board2[i][j] = move

    return board2


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # raise NotImplementedError
    def check_line(line):
        if all(cell == line[0] and cell is not None for cell in line):
            return line[0]
        return None

    # Check rows for a winner
    for row in board:
        winner = check_line(row)
        if winner:
            return winner

    # Check columns for a winner
    for col in range(len(board[0])):
        column = [board[row][col] for row in range(len(board))]
        winner = check_line(column)
        if winner:
            return winner

    # Check diagonals for a winner
    diag1 = [board[i][i] for i in range(len(board))]
    winner = check_line(diag1)
    if winner:
        return winner

    diag2 = [board[i][len(board) - 1 - i] for i in range(len(board))]
    winner = check_line(diag2)
    if winner:
        return winner

    return None  # No winner found



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # raise NotImplementedError
    if winner(board) == None:
        return False
    elif len(actions(board)) == 0:
        return True
    else:
        return True
    



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0


def max_value(board):
    if terminal(board):
        return utility(board)

    v = float("-inf")
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)

    v = float("inf")
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        # If it's X's turn, we want to maximize the utility value.
        best_value = float("-inf")
        best_move = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                best_move = action
    else:
        # If it's O's turn, we want to minimize the utility value.
        best_value = float("inf")
        best_move = None
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                best_move = action

    return best_move

