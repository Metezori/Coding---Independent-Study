def TicTacToe ():

    s1=str(1)
    s2=str(2)
    s3=str(3)
    s4=str(4)
    s5=str(5)
    s6=str(6)
    s7=str(7)
    s8=str(8)
    s9=str(9)
    plays = 0

    while plays != 9:

        print(s1 + "|" + s2 + "|" + s3)
        print(s4 + "|" + s5 + "|" + s6)
        print(s7 + "|" + s8 + "|" + s9)

        placed = False
        while placed == False:
            x = input("Place an X: ")
            placed = True
            if x == s1: s1 = "X"
            elif x == s2: s2 = "X"
            elif x == s3: s3 = "X"
            elif x == s4: s4 = "X"
            elif x == s5: s5 = "X"
            elif x == s6: s6 = "X"
            elif x == s7: s7 = "X"
            elif x == s8: s8 = "X"
            elif x == s9: s9 = "X"
            else: placed = False
        plays += 1

        if s1 == s2 == s3 or s1 == s4 == s7 or s1 == s5 == s9: return(s1)
        elif s4 == s5 == s6 or s2 == s5 == s8 or s7 == s5 == s3: return(s5)
        elif s7 == s8 == s9 or s3 == s6 == s9: return(s9)
        elif plays == 9: return("-")

        if plays == 1:
            if s5 != "5": s1 = "O"
            else: s5 = "O"
        else:
            if "1" == s1: s1 = "O"
            elif "2" == s2: s2 = "O"
            elif "3" == s3: s3 = "O"
            elif "4" == s4: s4 = "O"
            elif "6" == s5: s5 = "O"
            elif "6" == s6: s6 = "O"
            elif "7" == s7: s7 = "O"
            elif "8" == s8: s8 = "O"
            elif "9" == s9: s9 = "O"
        plays +=1

        if s1 == s2 == s3 or s1 == s4 == s7 or s1 == s5 == s9: return(s1)
        elif s4 == s5 == s6 or s2 == s5 == s8 or s7 == s5 == s3: return(s5)
        elif s7 == s8 == s9 or s3 == s6 == s9: return(s9)
        elif plays == 9: return("-")


n = TicTacToe()
if n == "X": print ("You win!")
elif n == "O": print ("You lose!")
else: print("Tie!")