abc = sorted([int(x) for x in input().split()])
d = {"A": 0, "B": 1, "C": 2}
i = [char for char in input()]
print(abc[d[i[0]]], abc[d[i[1]]], abc[d[i[2]]])