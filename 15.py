sent = str(input("Sentence: "))
a = sent.split()

print(a)
b = []

for x in range(len(a)):
    print(len(a) - x - 1)
    b.append(a[len(a) - x - 1])

print(b)
