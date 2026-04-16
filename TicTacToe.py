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

def TicTacToe ():

    s = [["1", "2", "3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]
    
    plays = 0

    while plays != 9:

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
        plays += 1

        #Check for win
        winner = winCheck(s, "X", "O", 3)
        if winner != 0: return(winner)

        #Computer plays
        if plays == 1:
            if s[1][1] != "5": s[0][0] = "O"
            else: s[1][1] = "O"
        else:
            if "1" == s[0][0]: s[0][0] = "O"
            elif "2" == s[0][1]: s[0][1] = "O"
            elif "3" == s[0][2]: s[0][2] = "O"
            elif "4" == s[1][0]: s[1][0] = "O"
            elif "6" == s[1][1]: s[1][1] = "O"
            elif "6" == s[1][2]: s[1][2] = "O"
            elif "7" == s[2][0]: s[2][0] = "O"
            elif "8" == s[2][1]: s[2][1] = "O"
            elif "9" == s[2][2]: s[2][2] = "O"
        plays +=1

        #Check for win
        winner = winCheck(s, "X", "O", 3)
        if winner != 0: return(winner)

print(TicTacToe())

