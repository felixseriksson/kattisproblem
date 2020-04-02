string = list(input())
ctr0, ctr1, ctr2 = 0, 0, 0
ustring = string[2:][:]
for char in ustring:
    if char == "D":
        ctr0 += 2
dstring = string[2:][:]
for char in dstring:
    if char == "U":
        ctr1 += 2
if string[0] == "U" and string[1] == "U":
    ctr1 += 1
elif string[0] == "U" and string[1] == "D":
    ctr0 += 2
    ctr1 += 1
elif string[0] == "D" and string[1] == "U":
    ctr0 += 1
    ctr1 += 2
elif string[0] == "D" and string[1] == "D":
    ctr0 += 1
for index in range(len(string)-1):
    if string[index] != string[index+1]:
        ctr2 += 1
print(ctr0, ctr1, ctr2, sep="\n")