
# test

def hangman(word):
    wrong = 0
    stages = ["", 
            "__________          ",
            "|                   ",
            "|         |         ",
            "|         O         ",
            "|        /|`        ",
            "|        / `        ",
            "|                   "
            ]
    rletters = list(word)
    print(rletters)
    board = ["_"] * len(word)
    print(board)
    win = False
    print("Welcome to HangMan")
    while wrong < len(stages)-1:
        print("\n")
        msg = "Image a char"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
            print(rletters)
        else:
            wrong +=1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win !")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("you lose! Answer is {}.".format(word))
