# Problem 1
def below_mean(n):
    total = 0
    for i in n:
        total += i
    mean = total / len(n)
    below = []
    for i in n:
        if i < mean:
            below.append(i)
    return below


#Problem 2
def two_lowest(n):
    n.sort()
    return [n[0], n[1]]


#Function calls
print(below_mean([1, 3, 3, 4, 5]))
print(two_lowest([500, 6, 236, 48, 15, 5555, 15]))

