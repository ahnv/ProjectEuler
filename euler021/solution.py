listOfAmicableNumbers = [220, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368, 10744, 10856, 12285, 14595, 17296, 18416, 63020, 76084, 66928, 66992, 67095, 71145, 69615, 87633, 79750, 88730]

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [i for i in listOfAmicableNumbers if i <= n]
    print(sum(arr))
