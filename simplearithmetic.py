from decimal import *
getcontext().prec = 35
a, b, c = [Decimal(x) for x in input().split()]
print(a*b/c)