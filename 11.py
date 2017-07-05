def getNumber(text="Number: "):
    return int(input(text))

def isPrime(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    for m in range(int(number / 2) + 1, 1, -1):
        if (number % m == 0):
            return False
    return True

print("Primality: " +
      str(isPrime(getNumber("Enter the number whose primality will be found: "))))