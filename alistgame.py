num, counter = int(input()), 0
for i in range(2, round(num**0.5)+1):
    while num % i == 0: num, counter = num/i, counter+1
print([(counter+1) if num != 1 else counter][0])
'''
upper = ceil(sqrt(num))+1

while num % 2 == 0:
    factors.append(2)
    num = int(num / 2)

for i in range(3, upper, 2):
    while num % i == 0:
        factors.append(i)
        num = int(num / i)
    if num == 1:
        break
    
if len(factors) == 0:
    print(1)
else:
    print(len(factors))
'''