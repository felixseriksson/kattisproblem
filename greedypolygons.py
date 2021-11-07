from math import tan, pi
for _ in range(int(input())):
    n, l, d, g = [int(x) for x in input().split()]
    print(pi*(d*g)**2 + n/4*l*l/tan(pi/n) + n*d*g*l)