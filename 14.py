a = [1, 2, 3, 4, 1, 3, 7]

def removeDupsByIteration(li):
    sol = []
    for x in li:
        if x not in sol:
            sol.append(x)
    return sol

def removeDupsBySets(li):
    return list(set(li))

print(removeDupsByIteration(a))
print(removeDupsBySets(a))