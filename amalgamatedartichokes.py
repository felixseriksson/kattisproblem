from math import sin, cos

p, a, b, c, d, n = [int(x) for x in input().split()]

def f(p, a, b, c, d, x):
    return p*(sin(a*x + b) + cos(c*x + d) + 2)

currentmax = f(p, a, b, c, d, 1)
greatestdecline = 0
for i in range(2, n+1):
    currentf = f(p, a, b, c, d, i)
    greatestdecline = max(greatestdecline, currentmax - currentf)
    currentmax = max(currentmax, currentf)

print(greatestdecline)