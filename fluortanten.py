n = int(input())
a = [int(x) for x in input().split() if int(x) != 0]
h1 = [idx*ai for idx, ai in enumerate(a, start = 1)]
h2 = [idx*ai for idx, ai in enumerate(a, start = 2)]
prefh1 = [0 for _ in range(n)]
prefh1[1] = h1[0]
for i in range(1, n-1):
    prefh1[i+1] = prefh1[i] + h1[i]
posth2 = [0 for _ in range(n)]
posth2[1] = h2[-1]
for i in range(1, n-1):
    posth2[i+1] = posth2[i] + h2[n-i-2]
posth2 = posth2[::-1]

print(max([a+b for a, b in zip(prefh1, posth2)]))