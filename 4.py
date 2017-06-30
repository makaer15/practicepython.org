x = int(input("Number whose divisors to be found: "))
y = range(1, x + 1)
for m in y:
    if x % m == 0:
        print(m)