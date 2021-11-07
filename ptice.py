n = int(input())
problems = [char for char in input()]
a, b, g = 0, 0, 0

for i in range(len(problems)):
    if i % 3 == 0:
        if problems[i] == "A":
            a += 1
    elif i % 3 == 1:
        if problems[i] == "B":
            a += 1
    else:
        if problems[i] == "C":
            a += 1
    if i % 4 == 0 or i % 4 == 2:
        if problems[i] == "B":
            b += 1
    elif i % 4 == 1:
        if problems[i] == "A":
            b += 1
    else:
        if problems[i] == "C":
            b += 1
    if i % 6 == 0 or i % 6 == 1:
        if problems[i] == "C":
            g += 1
    elif i % 6 == 2 or i % 6 == 3:
        if problems[i] == "A":
            g += 1
    else:
        if problems[i] == "B":
            g += 1

vals = [(a, "Adrian"), (b, "Bruno"), (g, "Goran")]
maxx = max([a, b, g])
vals = [a[1] for a in vals if a[0] == maxx]
vals = sorted(vals)
print(maxx)
for val in vals:
    print(val)