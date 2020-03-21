factornum = int(input())
divisornum = factornum
primefactors = []
divisors = []

for p in range(2, int(factornum**0.5)+2):
    if p > factornum:
        break
    ctr = 0
    if factornum % p == 0:
        while factornum % p == 0:
            factornum = int(factornum / p)
            ctr += 1
        divisornum = int(divisornum/p)
        primefactors.append(p)

if factornum > 1:
    divisornum = int(divisornum/factornum)
    primefactors.append(factornum)

for d in range(1, int(divisornum**0.5)+2):
    if divisornum % d == 0:
        divisors.append(d)
        if d*d < divisornum:
            divisors.append(int(divisornum/d))

divisors.sort()

#S = set(divisors)
S = divisors.copy()
S.remove(1)
for i in primefactors:
    try:
        S.remove(i)
    except KeyError:
        pass


opt = [float("-inf")]*len(divisors)
opt[0] = 0
for member in S:
    ptr = len(divisors)
    for i in range(len(divisors)-1, 0, -1):
        while ptr > 0 and divisors[ptr-1] > divisors[i] / member:
            ptr -= 1
        if ptr == 0:
            break
        if member * divisors[ptr-1] == divisors[i]:
            opt[i] = max(opt[i], opt[ptr-1]+1)

maxi = max(opt) + len(primefactors)
print(maxi)