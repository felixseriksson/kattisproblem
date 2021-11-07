n, m = [int(x) for x in input().split()]
known = [ord(x)-97 for x in input()][::-1]
cipher = [ord(x)-97 for x in input()][::-1]

for i in range(m-n):
    known.append((cipher[i]-known[i]) % 26)

print(*[chr(97+w) for w in known][::-1], sep="")