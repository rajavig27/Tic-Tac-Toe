#Tic Tac Toe Player


import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    #Returns starting state of the board.

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):

    #Returns player who has the next turn on a board.
    #if board == EMPTY:
    X_count = sum(row.count(X) for row in board)
    O_count = sum(row.count(O) for row in board)
    return X if X_count <= O_count else O

    #raise NotImplementedError


def actions(board):
    
    #Returns set of all possible actions (i, j) available on the board.
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}
    #raise NotImplementedError


def result(board, action):
    
    #Returns the board that results from making move (i, j) on the board.
    if board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid action")
    #new_board = copy.deepcopy(board)
    #new_board[action[0]][action[1]] = player(board)
    #return new_board
    new_board = [row[:] for row in board]  # Create a copy of the board
    new_board[action[0]][action[1]] = player(board)
    return new_board
    #raise NotImplementedError


def winner(board):
    
    #Returns the winner of the game, if there is one.
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    return None
    #raise NotImplementedError


def terminal(board):
    
    #Returns True if game is over, False otherwise.
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)

    #raise NotImplementedError


def utility(board):
    
    #Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0
    #raise NotImplementedError


def minimax(board):
    
    #Returns the optimal action for the current player on the board.
    current_player = player(board)

    def max_value(board):
        if terminal(board):
            return utility(board), None
        v = -math.inf
        best_action = None
        for action in actions(board):
            min_val, _ = min_value(result(board, action))
            if min_val > v:
                v = min_val
                best_action = action
        return v, best_action

    def min_value(board):
        if terminal(board):
            return utility(board), None
        v = math.inf
        best_action = None
        for action in actions(board):
            max_val, _ = max_value(result(board, action))
            if max_val < v:
                v = max_val
                best_action = action
        return v, best_action

    if current_player == X:
        _, action = max_value(board)
    else:
        _, action = min_value(board)
    
    return action
    #raise NotImplementedError
