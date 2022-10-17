from math import sqrt

def squaredDist(x_1, x_2):
    return (x_1[0] - x_2[0]) * (x_1[0] - x_2[0]) + (x_1[1] - x_2[1]) * (x_1[1] - x_2[1])

def closestPairBruteforce(px, length):
    x_1, x_2 = px[0], px[1]
    if length == 2:
        return x_1, x_2
    md = squaredDist(px[0], px[1])
    for i in range(length - 1):
        for j in range(i + 1, length):
            d = squaredDist(p[i], p[j])
            if d < md:
                x_1 = p[i]
                x_2 = p[j]
    return x_1, x_2

def closestPairSplit(px, py, d, p_1, p_2):
    length = len(px)
    midpoint = px[length // 2]

    s = [x for x in py if squaredDist(x, midpoint) <= d]

    best = d
    ls = len(s)
    for i in range(ls - 1):
        for j in range(i + 1, min(i + 7, ls)):
            p, q = s[i], s[j]
            if squaredDist(p, q) < best:
                p_1, p_2 = p, q
    return p_1, p_2

def closestPairRecursive(px, py):
    length = len(px)
    if length <= 3:
        return closestPairBruteforce(px, length)
    mid = length // 2
    lx = px[:mid]
    rx = px[mid:]

    midpoint = px[mid][0]
    ly, ry = [], []
    for x in py:
        if x[0] < midpoint:
            ly.append(x)
        else:
            ry.append(x)
    p_1, q_1 = closestPairRecursive(lx, ly)
    p_2, q_2 = closestPairRecursive(rx, ry)

    if squaredDist(p_1, q_1) > squaredDist(p_2, q_2):
        p_1, q_1 = p_2, q_2
    
    minSquaredDist = squaredDist(p_1, q_1)
    
    p_2, q_2 = closestPairSplit(px, py, minSquaredDist, p_1, q_1)

    if minSquaredDist <= squaredDist(p_2, q_2):
        return p_1, q_1
    else:
        return p_2, q_2

def closestPair(p):
    """
        Given a list of 2d points p = [(x_1, y_1), ..., (x_n, y_n)],
        returns (x_i, y_i), (x_j, y_j) such that d((x_i, y_i),(x_j, y_j))
        is minimal over the list of points. We guarantee x_i <= x_j and
        if equality holds y_i <= y_j.
    """
    x_sorted = sorted(p, key = lambda x: x[0])
    y_sorted = sorted(p, key = lambda x: x[1])
    a, b = closestPairRecursive(x_sorted, y_sorted)
    if a[0] < b[0]:
        return a, b
    elif a[0] > b[0]:
        return b, a
    else:
        if a[1] <= b[1]:
            return a, b
        else:
            return b, a

n = int(input())
while n != 0:
    p = []
    for _ in range(n):
        p.append(tuple(float(x) for x in input().split()))
    a, b = closestPair(p)
    print(*a, *b)
    # print(sqrt(squaredDist(a, b)))
    n = int(input())