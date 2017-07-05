def getNumber(text = "Number: "):
    return int(input(text))

num = getNumber("Enter the number whose primality will be found: ")

def isPrime(number):
    for m in range(number - 1, 1, -1):
        if (number % m == 0):
            return False
    return True

print("Primality: " + str(isPrime(num)))