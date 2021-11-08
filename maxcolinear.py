from collections import defaultdict
n = int(input())

def slope(a, b):
    if a[0] == b[0]:
        return "inf"
    elif a[0] < b[0]:
        return (b[1]-a[1])/(b[0]-a[0])
    else:
        return (a[1]-b[1])/(a[0]-b[0])

while n != 0:
    points = []
    for _ in range(n):
        points.append([int(x) for x in input().split()])
    
    if n == 1:
        print(1)
        n = int(input())
        continue
    maxnum = 0
    for point in points:
        slopes = defaultdict(int)
        for other in points:
            if other != point:
                slopes[slope(point, other)] += 1
        maxnum = max(maxnum, max(slopes.values()))

    print(maxnum + 1)
    
    n = int(input())