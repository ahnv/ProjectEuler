import sys

def solve(data):
    while len(data) > 1:
        a = data.pop()
        b = data.pop()
        data.append([max(a[i], a[i+1]) + t for i,t in enumerate(b)])
    return data[0][0]

for _ in range(int(input())):
    rows = int(input())
    data = []
    for __ in range(rows):
        line = sys.stdin.readline().rstrip('\n')
        data.append(list(map(int,line.split())))
    print(solve(data))