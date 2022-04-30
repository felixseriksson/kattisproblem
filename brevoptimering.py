from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)

n = int(input())
m = [0 for _ in range(n+1)]
u = [None for _ in range(n+1)]
pred = defaultdict(list)
for i in range(1, n+1):
    mval, pairs, *rest = [int(x) for x in input().split()]
    m[i] = mval
    for p, percentage in zip(rest[::2], rest[1::2]):
        pred[p].append((i, percentage/100))

def getu(i):
    if not u[i] is None:
        return u[i]
    if not pred[i]:
        u[i] = m[i]
        return u[i]
    sumin = 0
    for j, percentage in pred[i]:
        sumin += getu(j)*percentage
    u[i] = min(m[i], sumin)
    return u[i]

ret = [str(i) for i in range(1, n+1) if getu(i) == m[i]]
print(" ".join(ret))