N = int(input())

pengalista = [1, 5, 10, 20, 50, 100, 200, 500, 1000]
vallist = [0]*(N+1)

# def sättattskriva(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 1
#     values = [val for val in pengalista if val <= n]
#     summa = 0
#     for x in values:
#         summa += sättattskriva(n-x)
#     return summa

# print(sättattskriva(N))
for n in range(N+1):
    if n == 0 or n == 1:
        vallist[n] = 1
    else:
        summa = 0
        for x in pengalista:
            if x > n:
                break
            summa += vallist[n-x]
        vallist[n] = summa

print(vallist[N])