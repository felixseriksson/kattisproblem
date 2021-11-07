from os import stat


n, l = [int(x) for x in input().split()]
d = dict()
qs, ms, us = 0, 0, 0,
for _ in range(n):
    name, status = input().split()
    d[name] = status
    if status == "?":
        qs += 1
    elif status == "m":
        ms += 1
    elif status == "u":
        us += 1
mm, mu, mq, um, uu, uq, qm, qu, qq = 0, 0, 0, 0, 0, 0, 0, 0, 0
for _ in range(l):
    n1, n2 = input().split(" -> ")
    if d[n1] == "m" and d[n2] == "m":
        mm += 1
    elif d[n1] == "m" and d[n2] == "u":
        mu += 1
    elif d[n1] == "m" and d[n2] == "?":
        mq += 1
    elif d[n1] == "u" and d[n2] == "m":
        um += 1
    elif d[n1] == "u" and d[n2] == "u":
        uu += 1
    elif d[n1] == "u" and d[n2] == "?":
        uq += 1
    elif d[n1] == "?" and d[n2] == "m":
        qm += 1
    elif d[n1] == "?" and d[n2] == "u":
        qu += 1
    elif d[n1] == "?" and d[n2] == "?":
        qq += 1
if mu >= 1:
    print(1)
elif ((mu == 0) and (qu == 0) and (mq == 0) and (qq == 0)) :#or (qs == 0):
    print(0)
else:
    print("?")