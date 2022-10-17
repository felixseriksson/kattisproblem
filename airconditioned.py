n = int(input())
# Need to sort primarily by second coord, secondarily by first.
# Python default is the opposite of this
l, r = sorted([[int(x) for x in input().split()][::-1] for _ in range(n)]), 1
l = [a[::-1] for a in l]
temp = l[0][1]
for a in l[1:]:
    if a[0] > temp:
        temp, r = a[1], r + 1
print(r)