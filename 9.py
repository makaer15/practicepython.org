import random
num = random.randrange(1,9)
print("Program will generate a random number between 1 and 9 (both inclusive). Give it a shot! Type \'exit\' to terminate.")
guess = input("Your guess: ")
guessN = 0
if guess.__eq__("exit"):
    exit = False
else:
    guessN = int(guess)
    exit = True

while exit:
    if guessN == num:
       print("You got it!")
       break
    elif guessN > num:
        print("Too high.")
    elif guessN < num:
        print("Too low.")
    else:
        print("Wrong, something went. Wrong input type you gave? (Yoda)")
    guess = input("Your guess: ")
    if guess.__eq__("exit"):
        exit = False
        break
    else:
        guessN = int(guess)

print("Random number: " + str(num))