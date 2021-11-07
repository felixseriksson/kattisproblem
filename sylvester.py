def H(r, c, d):
    if d == 1:
        return 1
    v = H(r % (d//2), c % (d//2), d//2)
    if r >= d//2 and c >= d//2:
        return -1*v
    else:
        return v

# print(H(0,0,4))
# print(H(1,1,4))
# print(H(2,2,4))
# print(H(3,3,4))

cases = int(input())
for _ in range(cases):
    n, x, y, w, h = [int(x) for x in input().split()]
    for j in range(y, y+h):
        row = " ".join([str(H(i, j, n)) for i in range(x, x+w)])
        print(row)
    print()