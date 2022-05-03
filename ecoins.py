from collections import deque

def modulus(a, b):
    return (a*a + b*b)**0.5

def bfs(coins, s):
    q = deque()
    q.append((0, 0, 0))
    seen = set()
    seen.add((0, 0))
    
    while q:
        ca, cb, steps = q.popleft()
        for da, db in coins:
            ea, eb = ca + da, cb + db
            if (ea, eb) in seen or modulus(ea, eb) > s:
                continue
            elif modulus(ea, eb) == s:
                return steps + 1
            else:
                q.append((ea, eb, steps + 1))
                seen.add((ea, eb))
    return -1

N = int(input())

for i in range(N):
    n, s = [int(x) for x in input().split()]
    coins = []
    for _ in range(n):
        coins.append([int(x) for x in input().split()])
    ans = bfs(coins, s)
    if ans == -1:
        print("not possible")
    else:
        print(ans)
    if i != N-1:
        input()