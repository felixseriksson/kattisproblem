from math import sqrt
def fibmod(n):
    return (1/(sqrt(5))*(((1+sqrt(5))/2)**n - ((1-sqrt(5))/2)**n))%10**9
for _ in range(int(input())):
    i, num = [int(x) for x in input().split()]
    print(i, fibmod(num))