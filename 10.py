import random
a = random.sample(range(100), 10)
b = random.sample(range(100), 12)
print(a)
print(b)

sol = [x for x in a for y in b if x == y]
print(sol)