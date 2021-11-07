n, m = [int(x) for x in input().split()]
bestcand, bestright = 1, 0
for i in range(n):
    right = 0
    l = input().split()
    for idx in range(m):
        if ((idx + 1) % 15 == 0):
            exp = "fizzbuzz"
        elif ((idx + 1) % 3 == 0):
            exp = "fizz"
        elif ((idx + 1) % 5 == 0):
            exp = "buzz"
        else:
            exp = str(idx + 1)
        if l[idx] == exp:
            right += 1
    if right > bestright:
        bestright = right
        bestcand = i+1
print(bestcand)