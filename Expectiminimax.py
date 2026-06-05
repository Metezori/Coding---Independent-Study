import copy
import tqdm
import random

def minimax (roll, position, depth, maximizing): #DEPTH ON EVEN TURN
    if depth == 0:
        return(evaluate(position[0], position[1], position[2]))
    evaluation = winCheckFast(position[0], position[1], position[2])
    evaluation *= (depth+1)/2
    if evaluation != 0:
        return(evaluation)
    '''elif gameOver(position[0]):
        return(evaluation)'''
    
    if maximizing:
        maxEval = float('-inf')
        childs = nextMoves(roll, position[0], position[1], position[2], True)
        for child in childs:
            evaluation = minimax(child, depth - 1, False)
            maxEval = max(maxEval, evaluation)
        return(maxEval)
    
    else:
        minEval = float('inf')
        childs = nextMoves(position[0], "O")
        for child in childs:
            evaluation = minimax(child, depth - 1, True)
            minEval = min(minEval, evaluation)
        return(minEval)
    
def nextMoves (roll, board, p1, p2, maximizing):

    new = copy.deepcopy(board)
    np1 = copy.deepcopy(p1)
    np2 = copy.deepcopy(p2)
    moves = []
    spots1 = []
    spots2 = []

    #Find where every player is
    for spot in board:
        if spot == 1:
            spots1.append(spot)
        elif spot == -1:
            spots2.append(spot)

    #Gen moves
    if maximizing:
        if len(p1) != 0 and roll > 3 and new[0] <= 0:
            new[0] = 1
            np1.pop()
            if board[0] < 0:
                np2.append(-1)
            moves.append([new, np1, np2])

        np1 = copy.deepcopy(p1)
        for spot in spots1:
            new = copy.deepcopy(board)
            np2 = copy.deepcopy(p2)
            if spot + roll <= 14:
                if board[spot + roll] < 0:
                    np2.append(-1)
                elif board[spot + roll] > 0:
                    continue
                new[spot + roll] = 1
                new[spot] = 0
                moves.append([new, np1, np2])
            else:
                new[spot] = 0
                moves.append([new, np1, np2])
    else:
        if len(p2) != 0 and roll > 3 and new[0] >= 0:
            new[0] = -1
            np2.pop()
            if board[0] > 0:
                np1.append(1)
            moves.append([new, np1, np2])

        np2 = copy.deepcopy(p2)
        for spot in spots2:
            new = copy.deepcopy(board)
            np1 = copy.deepcopy(p1)
            if spot + roll >= 0:
                if board[spot + roll] > 0:
                    np1.append(1)
                elif board[spot + roll] < 0:
                    continue
                new[spot + roll] = -1
                new[spot] = 0
                moves.append([new, np1, np2])
            else:
                new[spot] = 0
                moves.append([new, np1, np2])
    return moves
    
            
def winCheckFast(board, p1, p2):
    p1win = True
    p2win = True
    for spot in board:
        if spot == 1:
            p1win = False
        elif spot == -1:
            p2win = False
    if len(p1) == 0 and p1win:
        return(1)
    elif len(p2) == 0 and p2win:
        return(-1)
    else:
        return(0)
    
def evaluate (board, p1, p2):
    
    score = 0
    
    lp1 = len(p1)
    lp2 = len(p2)
    
    score += (lp1 - lp2)*100

    i = 0
    for spot in board:
        i += 1
        if spot == 1:
            score += i*10
        elif spot == -1:
            score -= i*10

    return(score/1000)

    
def miniLudo ():
    p1 = [1,1,1,1]
    p2 = [-1,-1,-1,-1]
    board = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    print(board)
    print(p1)
    print(p2)

    roll = random.randint(1,6)
    moves = nextMoves(roll, board, p1, p2, True)
    for move in moves:
        eval = minimax(move, 3, float('-inf'), float('inf'), True)
        if eval == 0:
            board = move[0]
            p1 = move[1]
            p2 = move[2]
            print(board)
            break

    print(board)
    print(p1)
    print(p2)

    roll = random.randint(1,6)
    moves = nextMoves(roll, board, p1, p2, False)
    for move in moves:
        eval = minimax(move, 3, float('-inf'), float('inf'), False)
        if eval == 0:
            board = move[0]
            p1 = move[1]
            p2 = move[2]
            print(board)
            break





