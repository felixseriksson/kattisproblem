n = int(input())
ints = [int(x) for x in input().split()]
m, s = 0, 0
for n in ints:
    if n <= m:
        s += n
    else:
        s+= m
        m = n
if m >= s:
    print(m*2)
else:
    print(s+m)