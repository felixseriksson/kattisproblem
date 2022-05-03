n = int(input())

root = 1
while root*root <= n:
    root += 1

mu = [1 for _ in range(root + 1)]
prime = [1 for _ in range(root + 1)]

for i in range(2, root + 1):
    if prime[i]:
        for j in range(i, root + 1, i):
            prime[j] = 0
            if not (j//i % i):
                mu[j] = 0
            else:
                mu[j] = -mu[j]

res = 0
i = 1
while i*i <= n:
    res += mu[i]*((n//i)//i)
    i += 1

print(res)