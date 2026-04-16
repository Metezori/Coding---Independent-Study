def winCheck (matrix, p1, p2, threshold):

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
                elif matrix[row][col] == p2: return(2)

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
                elif matrix[row][col] == p2: return(2)

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
                elif matrix[row - i][i] == p2: return(2)
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
                elif matrix[len(matrix) - 1 - i][col + i] == p2: return(2)

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
                elif matrix[i][col + i] == p2: return(2)
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
                elif matrix[row + i][i] == p2: return(2)

    return(0)


# MATRIX 1 — COLUMN WIN (X wins)
matrix1 = [
    ['O', 'O', '.', 'O', '.', 'O', 'O'],
    ['O', 'O', '.', 'X', '.', '.', '.'],
    ['O', 'O', '.', 'X', '.', '.', '.'],
    ['X', '.', 'O', 'X', '.', '.', '.'],
    ['X', 'O', '.', 'X', '.', '.', '.'],
    ['O', 'O', '.', '.', '.', '.', '.']
]

# MATRIX 2 — ROW WIN (O wins)
matrix2 = [
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', 'X', 'X', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', 'X', '.'],
    ['X', '.', 'X', '.', 'X', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.']
]

# MATRIX 3 — UPWARD DIAGONAL WIN (X wins)
matrix3 = [
    ['.', '.', '.', '.', '.', '.', 'X'],
    ['.', '.', '.', '.', '.', 'X', 'O'],
    ['.', '.', '.', '.', 'X', 'O', '.'],
    ['.', '.', '.', 'X', 'O', '.', '.'],
    ['.', '.', 'O', '.', '.', '.', '.'],
    ['.', 'O', '.', '.', '.', '.', '.']
]

# MATRIX 4 — DOWNWARD DIAGONAL WIN (O wins)
matrix4 = [
    ['O', '.', '.', '.', '.', '.', '.'],
    ['.', 'O', '.', '.', '.', '.', '.'],
    ['.', '.', 'O', 'X', '.', '.', '.'],
    ['.', '.', '.', 'O', '.', '.', '.'],
    ['.', 'X', '.', '.', 'X', '.', '.'],
    ['X', '.', '.', '.', '.', 'X', '.']
]

# MATRIX 5 — DOWNWARD DIAGONAL WIN (O wins)
matrix5 = [
    ['O', '.', 'O', 'O', '.', 'O', 'O'],
    ['.', 'O', '.', '.', 'O', '.', 'O'],
    ['.', 'O', '.', 'X', '.', 'O', '.'],
    ['O', '.', '.', 'O', '.', 'O', '.'],
    ['O', 'O', '.', '.', 'O', '.', 'O'],
    ['X', '.', 'O', 'O', '.', 'X', '.']
]

# MATRIX 7 — NON-SQUARE (no win)

matrix7 = [
    ['.', 'X', 'O'],
    ['X', '.', 'X'],
    ['.', 'X', 'O'],
    ['X', '.', 'X'],
    ['.', 'X', '.'],
    ['X', '.', 'X'],
    ['.', 'X', '.'],
]

# MATRIX 8 — NON-SQUARE + VERTICAL (O wins)

matrix8 = [
    ['.', '.', 'O'],
    ['.', '.', 'O'],
    ['X', '.', 'O'],
    ['X', '.', 'O'],
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.'],
]

# MATRIX 9 — CLUSTER CHAOS (X wins diagonal hidden in noise)

matrix9 = [
    ['X', 'O', 'X', 'O', 'X', 'O', 'X'],
    ['O', 'X', '.', 'X', 'O', 'X', '.'],
    ['X', 'O', 'X', '.', 'X', '.', '.'],
    ['O', 'X', 'O', 'X', '.', '.', '.'],
    ['X', 'O', 'X', '.', '.', '.', '.'],
]


print(winCheck(matrix9, "X", "O", 4))