def closestto1k(l):
    cl = min(l, key=lambda x:abs(x-1000))
    if 2000 - cl in l:
        return 2000-cl
    return cl


numberofweights = int(input())
weights = []
for _ in range(numberofweights):
    weights.append(int(input()))

dptable = [[0 for col in range(2001)] for row in range(numberofweights+1)]
for item in range(1, numberofweights+1):
    for lessthanorequalto in range(1, 2001):
        weight = weights[item-1]
        if lessthanorequalto >= weight:
            dptable[item][lessthanorequalto] = max(dptable[item-1][lessthanorequalto], weight + dptable[item-1][lessthanorequalto-weight])
        else:
            dptable[item][lessthanorequalto] = dptable[item-1][lessthanorequalto]


print(closestto1k(dptable[-1]))