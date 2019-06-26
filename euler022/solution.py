def calcScore(name):
    return sum([(ord(c) - 64) for c in list(name)])

n = int(input())
listOfNames = []
for _ in range(n):
    listOfNames.append(input())

listOfNames.sort()

q = int(input())
for _ in range(q):
    query = input()
    index = listOfNames.index(query)
    print((index+1) * calcScore(query))
