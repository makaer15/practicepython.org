s = str(input("word: "))
l = s.__len__()
l1 = l - 1
l2 = int(l/2)
if l % 2 == 0:
    if s[:(l2)].__eq__(s[l1:(l2 - 1):-1]):
        print("Palindrome")
    else:
        print("Not palindrome.")
else:
    if s[:(l2)].__eq__(s[l1:(l2):-1]):
        print("Palindrome")
    else:
        print("Not palindrome.")