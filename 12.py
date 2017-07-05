import random

a = random.sample(range(random.randint(100, 1000)), random.randint(10, 100))

print(a)
print("First item: " + str(a[0:1]))
print("Last item: " + str(a[-1:]))