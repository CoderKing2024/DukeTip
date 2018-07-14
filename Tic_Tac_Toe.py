global playerTurn, one, two, three, four, five, six, seven, eight, nine
playerTurn = "x"
win_condition = 0
drawCondition = False

#Board Spaces
one = "1"
two = "2"
three = "3"
four = "4"
five = "5"
six = "6"
seven = "7"
eight = "8"
nine = "9"

turn = 1

def drawBoard(one, two, three, four, five, six, seven, eight, nine, playerTurn):

    while(win_condition == 0):
        print("------------------")
        print("  Tic Tac Toe!")
        print("    " +one+ " | " +two+ " | " +three+ "\n   ___|___|___\n    " +four+ " | " +five+ " | " +six+ "\n   ___|___|___\n    " +seven+ " | " +eight+ " | " +nine+ "\n      |   |")
        print("It is "+playerTurn+"'s turn")
        print("------------------")

        #Player chooses move
        chooseMove = int((input("Choose where to \n place an x or o... player " + playerTurn + ")\n>")))

        #Tests move and sets it
        if(playerTurn == "x"):
            if(chooseMove == 1):
                one = "x"
            if(chooseMove == 2):
                two = "x"
            if(chooseMove == 3):
                three = "x"
            if(chooseMove == 4):
                four = "x"
            if(chooseMove == 5):
                five = "x"
            if(chooseMove == 6):
                six = "x"
            if(chooseMove == 7):
                seven = "x"
            if(chooseMove == 8):
                eight = "x"
            if(chooseMove == 9):
                nine = "x"
        else:
            if(chooseMove == 1):
                one = "o"
            if(chooseMove == 2):
                two = "o"
            if(chooseMove == 3):
                three = "o"
            if(chooseMove == 4):
                four = "o"
            if(chooseMove == 5):
                five = "o"
            if(chooseMove == 6):
                six = "o"
            if(chooseMove == 7):
                seven = "o"
            if(chooseMove == 8):
                eight = "o"
            if(chooseMove == 9):
                nine = "o"
            #drawBoard(one, two, three, four, five, six, seven, eight, nine, playerTurn)

        if(playerTurn == "x"):
                playerTurn = "o"
        else:
            playerTurn = "x"

      #if(one == "x" and three == "x" and five == "x"):

def ticTacToe():
    #TODO: Draw Board
    #TODO: Get player move
    #TODO: Replace number with user "x" or "o"
    #TODO: Save the response and update board
    #TODO: Check if there are 3  in a row
    #TODO: Swap Player
    #TODO: REPEAT ALL STEPS
    global one
    global win_condition
    global playerTurn
    WIN_COMBINATIONS = [
       (1, 2, 3),
       (4, 5, 6),
       (7, 8, 9),
       (1, 4, 7),
       (2, 5, 8),
       (3, 6, 9),
       (1, 5, 9),
       (3, 5, 7),
    ]

    drawBoard(one, two, three, four, five, six, seven, eight, nine, playerTurn)

    winner = "xyz"

    if(one == "x" and two == "x" and three == "x"):
        win_condition = 1
        winner = "x"
    if(four == "x" and five == "x" and six == "x"):
        win_condition = 1
        winner = "x"
    if(seven == "x" and eight == "x" and nine == "x"):
        win_condition = 1
        winner = "x"
    if(one == "x" and four == "x" and seven == "x"):
        win_condition = 1
        winner = "x"
    if(two == "x" and five == "x" and eight == "x"):
        win_condition = 1
        winner = "x"
    if(three == "x" and six == "x" and nine == "x"):
        win_condition = 1
        winner = "x"
    if(one == "x" and five == "x" and nine == "x"):
        win_condition = 1
        winner = "x"
    if(three == "x" and five == "x" and seven == "x"):
        win_condition = 1
        winner = "x"

    if(one == "o" and two == "o" and three == "o"):
        win_condition = 1
        winner = "o"
    if(four == "o" and five == "o" and six == "o"):
        win_condition = 1
        winner = "o"
    if(seven == "o" and eight == "o" and nine == "o"):
        win_condition = 1
        winner = "o"
    if(one == "o" and four == "o" and seven == "o"):
        win_condition = 1
        winner = "o"
    if(two == "o" and five == "o" and eight == "o"):
        win_condition = 1
        winner = "o"
    if(four == "o" and five == "o" and six == "o"):
        win_condition = 1
        winner = "o"
    if(one == "o" and five == "o" and nine == "o"):
        win_condition = 1
        winner = "o"
    if(three == "o" and five == "o" and seven == "o"):
        win_condition = 1
        winner = "o"

    if(win_condition == 1):
        print ("Player " + winner + " wins!")


    if(one != "1" and two != "2" and three != "3" and four != "4" and five != "5" and six != "6" and seven != "7" and eight != "8" and nine != "9"):
        drawCondition = True

    if(drawCondition == True):
        print("No one wins")

#Controls whether the gane gets restarted.
# Always runs at least once
while True:
    ticTacToe()
    if(win_condition == 1):
        if input("Do you want to play again? (y/n)\n") != "y":
            break
