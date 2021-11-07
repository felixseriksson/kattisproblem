def getindex(des):
    if des[0] == "-":
        return 0, int(des[1:])-1
    elif des[0] == "+":
        return 1, int(des[1:])-1
    elif des[-1] == "-":
        return 2, int(des[:-1])-1
    elif des[-1] == "+":
        return 3, int(des[:-1])-1
    else:
        raise Exception("getindex is wrong")

teeth = [[True]*8 for _ in range(4)]
for i in range(4):
    teeth[i].append("m")
for _ in range(int(input())):
    d, v = input().split()
    row, idx = getindex(d)
    if v == "m":
        teeth[row][idx] = "m"
    else:
        teeth[row][idx] = "b"

if "b" in teeth[0] or "b" in teeth[1]:
    if len(set(teeth[2])) > 1 and len(set(teeth[3])) > 1:
        print(1)
    else:
        print(2)
else:
    if len(set(teeth[0])) > 1 and len(set(teeth[1])) > 1:
        print(0)
    else:
        print(2)