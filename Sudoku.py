import copy

def solve(matrix):
    
    childs = nextMoves(matrix)
    for child in childs:
        solved = isSolved(child)
        if solved:
            print(child)
        else:
            solve(child)


def isSolved(matrix):
    for row in range(9):
        for col in range(9):
            if matrix[row][col] == 0:
                return(False)
    return(True)

def nextMoves(matrix):

    #Find next empty cell
    found = False
    for r in range(9):
        for c in range(9):
            if matrix[r][c] == 0:
                row = r
                col = c
                found = True
                break
        if found:
            break

    #Find valid values
    valid = []
    for i in range(1,10):
        if isValid(matrix, row, col, i):
            valid.append(i)

    #Asexually reproduce
    childs = []
    for value in valid:
        child = copy.deepcopy(matrix)
        child[row][col] = value
        childs.append(child)

    return(childs)


def isValid(matrix, row, col, value):

    #Check row
    for i in range(9):
        if matrix[row][i] == value:
            return(False)
        
    #Check column
    for i in range(9):
        if matrix[i][col] == value:
            return(False)

    #Check block
    rowRange = row//3
    colRange = col//3
    for r in range(rowRange*3, (rowRange+1)*3):
        for c in range(colRange*3, (colRange+1)*3):
            if matrix[r][c] == value:
                return(False)

    return(True)


matrix3 = [
    [7, 0, 0, 4, 0, 9, 0, 0, 0],
    [0, 0, 0, 0, 7, 5, 3, 0, 0],
    [0, 5, 0, 1, 0, 0, 0, 7, 0],
    [6, 4, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 8, 0, 0, 0, 4],
    [0, 9, 0, 0, 0, 0, 0, 3, 6],
    [0, 2, 0, 0, 0, 4, 0, 6, 0],
    [0, 0, 7, 9, 5, 0, 0, 0, 0],
    [0, 0, 0, 7, 0, 8, 0, 0, 5]
]
matrix2 = [
    [0, 0, 0, 0, 0, 0, 5, 7, 3],
    [8, 0, 0, 0, 2, 0, 0, 0, 0],
    [7, 0, 0, 9, 0, 0, 8, 1, 0],
    [5, 8, 0, 7, 0, 6, 0, 0, 0],
    [0, 0, 1, 8, 0, 0, 0, 6, 0],
    [2, 3, 0, 0, 4, 0, 0, 0, 9],
    [9, 1, 5, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 6, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 4, 0]
]
matrix = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solve(matrix3)