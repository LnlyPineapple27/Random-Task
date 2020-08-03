
def check_state_game(move):
    return 0

def find_best_move(board):
    bestMove = "NULL"
    for currentMove in board:
        # current move is better than bestMove
        if currentMove > bestMove:
            bestMove = currentMove

    return bestMove

def minimax(board, depth, isMaximizingPlayer):
    curMove = "none"
    evaluation = check_state_game(curMove)
    if evaluation == WIN_GAME:
        return MAX - depth
    elif evaluation == LOSE_GAME:
        return MIN - depth
    elif evaluation == DRAW_GAME:
        return DRAW_VALUE
    else:
        if isMaximizingPlayer == True:
            bestVal = -INFINITY
            for move in board:
                value = minimax(board, depth + 1, False)
                bestVal = max(bestVal, value)
            return bestVal
        else:
            bestVal = +INFINITY
            for move in board:
                value = minimax(board, True)
                bestVal = min(bestVal, depth + 1, value)
            return bestVal
