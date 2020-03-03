n = int(input())
cvals = list(input().split())
cvals = [int(n) for n in cvals]
cvals.sort()
cvalsnew = [cvals[n]/(n+1) for n in range(len(cvals))]
impossible = False
for n in cvalsnew:
    if n > 1:
        print("impossible")
        impossible = True
        break

if impossible == False:
    temp = min(cvalsnew)
    if temp == int(temp):
        print(int(temp))
    else:
        print(temp)