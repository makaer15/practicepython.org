num = int(input("Number of fibonacci numbers: "))

def fibonacciNumberGenerator(thisMany):
    fib = []
    counter = 0
    cur = 0
    prev = 1

    while(counter != thisMany):
        cur = cur + prev
        prev = cur - prev
        counter = counter + 1
        fib.append(cur)

    print(fib)

fibonacciNumberGenerator(num)