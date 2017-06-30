a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
sol = []
x = int(input("Number to be compared: "))
for m in a:
    if m < x:
        sol.append(m)
print(sol)