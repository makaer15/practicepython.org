print("Welcome to the Rock Paper Scissors game!\n")
p1 = 0
p2 = 0

while True:
    p1 = int(input("Player 1, please choose from rock, paper and scissors (input a number):\n"
          "1. Rock\n"
          "2. Paper\n"
          "3. Scissors\n"))

    p2 = int(input("Player 2, please choose from rock, paper and scissors (input a number):\n"
           "1. Rock\n"
           "2. Paper\n"
           "3. Scissors\n"))

    if p1 == 1:
        if p2 == 1:
            print("Draw.")
        elif p2 == 2:
            print("Player 2 won.")
        elif p2 == 3:
            print("Player 1 won.")
        else:
            print("Crashed. Must be the wrong input.")
    elif p1 == 2:
        if p2 == 1:
            print("Player 1 won.")
        elif p2 == 2:
            print("Draw.")
        elif p2 == 3:
            print("Player 2 won.")
        else:
            print("Crashed. Must be the wrong input.")
    elif p1 == 3:
        if p2 == 1:
            print("Player 2 won.")
        elif p2 == 2:
            print("Player 1 won.")
        elif p2 == 3:
            print("Draw")
        else:
            print("Crashed. Must be the wrong input.")
    else:
        print("Crashed. Must be the wrong input.")

    cont = int(input("Do you want to play again? Type 1 for yes, 0 for no."))
    if cont == 1:
        print("--- --- ---")
    else:
        break