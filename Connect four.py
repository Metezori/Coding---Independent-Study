import copy
import random

'''def minimax (position, depth, maximizing):
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
        return(minEval)'''

'''def nextMoves (current, player):
    childs = []
    for row in range(len(current)):
        for col in range(len(current[0])):
            if current[row][col] != "X" and current[row][col] != "O":
                new = copy.deepcopy(current)
                new[row][col] = player
                childs.append(new)
    return(childs)'''

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



def connectFour ():
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
        placed = False
        while placed == False:
            x = input("Place an X: ")
            for row in range(5, -1, -1):
                if matrix[row][int(x)-1] == ".":
                    matrix[row][int(x)-1] = "X"
                    placed = True
                    break
    
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
        placed = False
        while placed == False:
            x = random.randint(1, 7)
            for row in range(5, -1, -1):
                if matrix[row][int(x)-1] == ".":
                    matrix[row][int(x)-1] = "O"
                    placed = True
                    break

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