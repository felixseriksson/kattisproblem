from math import log
for _ in range(int(input())):
    p, r, f = [int(x) for x in input().split()]
    n = 0
    while p*r**n <= f:
        n += 1
    print(n)