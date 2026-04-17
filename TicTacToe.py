import copy

def minimax (position, depth, maximizing):
    evaluation = winCheck(position, "X", "O", 3)
    if depth == 0 or gameOver(position):
        return(evaluation)
    elif evaluation != 0:
        return(evaluation)
    
    if maximizing:
        maxEval = float('-inf')
        childs = nextMoves(position, "X")
        for child in childs:
            evaluation = minimax(child, depth - 1, False)
            maxEval = max(maxEval, evaluation)
        return(maxEval)
    
    else:
        minEval = float('inf')
        childs = nextMoves(position, "O")
        for child in childs:
            evaluation = minimax(child, depth - 1, True)
            minEval = min(minEval, evaluation)
        return(minEval)

def nextMoves (current, player):
    childs = []
    for row in range(len(current)):
        for col in range(len(current[0])):
            if current[row][col] != "X" and current[row][col] != "O":
                new = copy.deepcopy(current)
                new[row][col] = player
                childs.append(new)
    return(childs)

def gameOver (current):
    for row in range(len(current)):
        for col in range(len(current[0])):
            if current[row][col] != "X" and current[row][col] != "O":
                return(False)
    return(True)
    
def winCheck (matrix, p1, p2, threshold):
    #p1 = 1
    #p2 = -1
    #tie = 0
    
    streak = 0

    #Check rows
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if col - 1 < 0:
                streak = 0
            elif matrix[row][col] != matrix[row][col - 1]:
                streak = 0 #I might be able to compress the if and elif into one
            streak += 1
            if streak == threshold:
                if matrix[row][col] == p1: return(1)
                elif matrix[row][col] == p2: return(-1)

    #Check columns
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            if row - 1 < 0:
                streak = 0
            elif matrix[row][col] != matrix[row - 1][col]:
                streak = 0
            streak += 1
            if streak == threshold:
                if matrix[row][col] == p1: return(1)
                elif matrix[row][col] == p2: return(-1)

    #Check upward diagonals
    for row in range(len(matrix)):
        if row + 1 >= len(matrix[0]): length = len(matrix[0])
        else: length = row + 1 
        for i in range(length):
            if i == 0 or row - i + 1 > len(matrix) - 1:
                streak = 0
            elif matrix[row - i][i] != matrix[row - i + 1][i - 1]:
                streak = 0
            streak += 1
            if streak == threshold:
                if matrix[row - i][i] == p1: return(1)
                elif matrix[row - i][i] == p2: return(-1)
    for col in range(len(matrix[0])):
        if len(matrix[0]) - col >= len(matrix): length = len(matrix)
        else: length = len(matrix[0]) - col
        for i in range(length):
            if i == 0:
                streak = 0
            elif matrix[len(matrix) - 1 - i][col + i] != matrix[len(matrix) - i][col + i - 1]:
                streak = 0
            streak += 1
            if streak == threshold:
                if matrix[len(matrix) - 1 - i][col + i] == p1: return(1)
                elif matrix[len(matrix) - 1 - i][col + i] == p2: return(-1)

    #Check downward diagonals
    for col in range(len(matrix[0])):
        if len(matrix[0]) - col >= len(matrix): length = len(matrix)
        else: length = len(matrix[0]) - col
        for i in range(length):
            if i == 0:
                streak = 0
            elif matrix[i][col + i] != matrix[i - 1][col + i - 1]:
                streak = 0
            streak += 1
            if streak == threshold:
                if matrix[i][col + i] == p1: return(1)
                elif matrix[i][col + i] == p2: return(-1)
    for row in range(len(matrix)):
        if len(matrix) - row >= len(matrix[0]): length = len(matrix[0])
        else: length = len(matrix) - row
        for i in range(length):
            if i == 0:
                streak = 0
            elif matrix[row + i][i] != matrix[row + i - 1][i - 1]:
                streak = 0
            streak += 1
            if streak == threshold:
                if matrix[row + i][i] == p1: return(1)
                elif matrix[row + i][i] == p2: return(-1)

    return(0)


def TicTacToe ():

    s = [["1", "2", "3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]
    
    firstPlay = 0

    while firstPlay > -1:

        #Print the board:
        print(s[0][0] + "|" + s[0][1] + "|" + s[0][2])
        print(s[1][0] + "|" + s[1][1] + "|" + s[1][2])
        print(s[2][0] + "|" + s[2][1] + "|" + s[2][2])

        #User plays
        placed = False
        while placed == False:
            x = input("Place an X: ")
            row = (int(x) - 1) // 3
            col = (int(x) - 1) % 3
            if s[row][col] == x:
                s[row][col] = "X"
                placed = True

        #Check for win
        evaluation = winCheck(s, "X", "O", 3)
        if gameOver(s): return(evaluation)
        elif evaluation != 0: return(evaluation)

        #Computer plays
        if firstPlay == 0:
            if s[1][1] != "5": s[0][0] = "O"
            else: s[1][1] = "O"
            firstPlay = 1
        else:
            moves = nextMoves(s, "O")
            bestEval = float('inf')
            bestMove = copy.deepcopy(s)
            for move in moves:
                eval = minimax(move, 9, True)
                bestEval = min(bestEval, eval)
                if eval == bestEval:
                    bestMove = copy.deepcopy(move)
                if eval == -1:
                    break
            s = copy.deepcopy(bestMove)

        #Check for win
        evaluation = winCheck(s, "X", "O", 3)
        if gameOver(s): return(evaluation)
        elif evaluation != 0: return(evaluation)

print(TicTacToe())

