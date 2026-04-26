import copy
import tqdm

def minimax (position, depth, alpha, beta, maximizing): #DEPTH ON EVEN TURN
    evaluation = winCheck(position, "X", "O", 4)
    evaluation *= (depth+1)
    if gameOver(position):
        return(evaluation)
    elif depth == 0:
        return(evaluate(position, maximizing))
    elif evaluation != 0:
        return(evaluation)
    
    if maximizing:
        maxEval = float('-inf')
        childs = nextMoves(position, "X")
        for child in childs:
            evaluation = minimax(child, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, evaluation)
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        return(maxEval)
    
    else:
        minEval = float('inf')
        childs = nextMoves(position, "O")
        for child in childs:
            evaluation = minimax(child, depth - 1, alpha, beta, True)
            minEval = min(minEval, evaluation)
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        return(minEval)
    
def minimax1 (position, depth, alpha, beta, maximizing): #DEPTH ON EVEN TURN
    evaluation = winCheck(position, "X", "O", 4)
    evaluation *= (depth+1)
    if gameOver(position):
        return(evaluation)
    elif depth == 0:
        return(evaluate1(position, maximizing))
    elif evaluation != 0:
        return(evaluation)
    
    if maximizing:
        maxEval = float('-inf')
        childs = nextMoves(position, "X")
        for child in childs:
            evaluation = minimax(child, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, evaluation)
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        return(maxEval)
    
    else:
        minEval = float('inf')
        childs = nextMoves(position, "O")
        for child in childs:
            evaluation = minimax(child, depth - 1, alpha, beta, True)
            minEval = min(minEval, evaluation)
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        return(minEval)

def nextMoves (current, player):
    childs = []
    for col in range(len(current[0])):
        for row in range(5, -1, -1):
                if current[row][int(col)-1] == ".":
                    new = copy.deepcopy(current)
                    new[row][int(col)-1] = player

                    if col < 4:
                        childs.insert(0, new)
                    else:
                        childs.insert(col-3, new)
                    break

    return(childs)

def gameOver (current):
        
    for row in range(len(current)):
        for col in range(len(current[0])):
            if current[row][col] != "X" and current[row][col] != "O":
                return(False)
    return(True)

def evaluate (matrix, maximizing):
    Xc = []
    Oc = []
    Xr = []
    Or = []
    newX = 0
    newO = 0

    #Looking where pieces are
    for row in range(len(matrix)): #CHANGE TO ACTUAL VALUES
        for col in range(len(matrix[row])):
            if matrix[row][col] == "X":
                newX += 1
            elif matrix[row][col] == "O":
                newO += 1
        Xr.append(newX)
        Or.append(newO)
        newX, newO = 0, 0
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            if matrix[row][col] == "X":
                newX += 1
            elif matrix[row][col] == "O":
                newO += 1
        Xc.append(newX)
        Oc.append(newO)
        newX, newO = 0, 0

    #Rewarding centeredness
    score = 0
    score += (Xr[2]+Xr[3])*45 + (Xr[1]+Xr[4])*35 + (Xr[0]+Xr[5])*25
    score += Xc[3]*50 + (Xc[4]+Xc[2])*40 + (Xc[5]+Xc[1])*30 + (Xc[6]+Xc[0])*20
    score -= (Or[2]+Or[3])*45 + (Or[1]+Or[4])*35 + (Or[0]+Or[5])*25
    score -= Oc[3]*50 + (Oc[4]+Oc[2])*40 + (Oc[5]+Oc[1])*30 + (Oc[6]+Oc[0])*20

    #Endgame check
    for col in range(len(matrix[0])):
        new = copy.deepcopy(matrix)
        for row in range(5, -1, -1):
            if matrix[row][col] == ".":
                if row % 2 != 0:
                    new[row][col] = "X"
                else:
                    new[row][col] = "O"
                win = winCheck(new, "X", "O", 4)
                if win == 1:
                    score += 500
                elif win == -1:
                    score -= 500

    return(score/10000)

def evaluate1 (matrix, maximizing):
    Xc = []
    Oc = []
    Xr = []
    Or = []
    newX = 0
    newO = 0

    #Looking where pieces are
    for row in range(len(matrix)): #CHANGE TO ACTUAL VALUES
        for col in range(len(matrix[row])):
            if matrix[row][col] == "X":
                newX += 1
            elif matrix[row][col] == "O":
                newO += 1
        Xr.append(newX)
        Or.append(newO)
        newX, newO = 0, 0
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            if matrix[row][col] == "X":
                newX += 1
            elif matrix[row][col] == "O":
                newO += 1
        Xc.append(newX)
        Oc.append(newO)
        newX, newO = 0, 0

    #Rewarding centeredness
    score = 0
    score += (Xr[2]+Xr[3])*45 + (Xr[1]+Xr[4])*35 + (Xr[0]+Xr[5])*25
    score += Xc[3]*50 + (Xc[4]+Xc[2])*40 + (Xc[5]+Xc[1])*30 + (Xc[6]+Xc[0])*20
    score -= (Or[2]+Or[3])*45 + (Or[1]+Or[4])*35 + (Or[0]+Or[5])*25
    score -= Oc[3]*50 + (Oc[4]+Oc[2])*40 + (Oc[5]+Oc[1])*30 + (Oc[6]+Oc[0])*20

    return(score/10000)
    
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



def connectFour ():
    matrix1 = [[".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", "X", ".", "O", "."],  
              [".", "X", ".", "O", "X", "X", "O"],
              [".", "O", ".", "X", "O", "O", "X"],
              ["X", "O", "X", "O", "X", "X", "O"],
              ["X", "O", "O", "X", "O", "O", "O"]]

    matrix = [[".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", "."],  
              [".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", "."],
              [".", ".", ".", ".", ".", ".", "."]]
    
    guide = "|1|2|3|4|5|6|7|"

    #print board
    for row in range(6):
        printLine = "|"
        for col in range(7):
            printLine += matrix[row][col]
            printLine += "|"
        print(printLine)
    print("---------------")
    print(guide)
    print()
    
    On = True

    while On:

        #use plays
        moves = nextMoves(matrix, "X")
        bestEval = float('-inf')
        bestMove = copy.deepcopy(matrix)
        alpha = float("-inf")
        beta = float("inf")
        for move in tqdm.tqdm(moves):
            eval = minimax1(move, 8, alpha, beta, False)
            bestEval = max(bestEval, eval)
            '''print(eval) #PLEASE TRY TO FIND HOW TO GET THE ALPHA BETA THING TO WORK'''
            if eval == bestEval:
                bestMove = copy.deepcopy(move)
        matrix = copy.deepcopy(bestMove)
    
        #print board
        for row in range(6):
            printLine = "|"
            for col in range(7):
                printLine += matrix[row][col]
                printLine += "|"
            print(printLine)
        print("---------------")
        print(guide)
        print()

        #Check for win
        evaluation = winCheck(matrix, "X", "O", 4)
        if gameOver(matrix): return(evaluation)
        elif evaluation != 0: return(evaluation)
        
        #Computer plays
        moves = nextMoves(matrix, "O")
        bestEval = float('inf')
        bestMove = copy.deepcopy(matrix)
        alpha = float("-inf")
        beta = float("inf")
        for move in tqdm.tqdm(moves):
            eval = minimax(move, 8, alpha, beta, True)
            bestEval = min(bestEval, eval)
            '''print(eval) #PLEASE TRY TO FIND HOW TO GET THE ALPHA BETA THING TO WORK'''
            if eval == bestEval:
                bestMove = copy.deepcopy(move)
        matrix = copy.deepcopy(bestMove)

        #print board
        for row in range(6):
            printLine = "|"
            for col in range(7):
                printLine += matrix[row][col]
                printLine += "|"
            print(printLine)
        print("---------------")
        print(guide)
        print()

        #Check for win
        evaluation = winCheck(matrix, "X", "O", 4)
        if gameOver(matrix): return(evaluation)
        elif evaluation != 0: return(evaluation)
            
    
print(connectFour())