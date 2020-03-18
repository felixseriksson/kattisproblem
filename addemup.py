num, summ = [int(s) for s in input().split()]
vals = list(zip([int(s) for s in input().split()], [x for x in range(num)]))

def turnable(num):
    if num == "1":
        return 1
    if num == "2":
        return 2
    if num == "3":
        return False
    if num == "4":
        return False
    if num == "5":
        return 5
    if num == "6":
        return 9
    if num == "7":
        return False
    if num == "8":
        return 8
    if num == "9":
        return 6
    if num == "0":
        return 0

totalvals = set()
for val in vals:
    totalvals.add(val)
    rev = ""
    broke = False
    for char in str(val[0]):
        if turnable(char):
            rev += str(char)
        else:
            broke = True
            break
    if broke == False:
        totalvals.add((int(rev[::-1]), val[1]))
totalvals = sorted(list(totalvals))
#print(totalvals)

loffset = 0
roffset = -1
litem = totalvals[loffset][0]
ritem = totalvals[roffset][0]
possible = False
skippedlastright = False
skippedlastleft = False
while ritem > litem:
    if litem + ritem == summ:
        possible = True
        break
        #klar
    elif litem + ritem > summ:
        roffset -= 1
        if skippedlastleft:
            loffset -= 1
            litem = totalvals[loffset][0]
        if totalvals[loffset][1] == totalvals[roffset][1]:
            roffset -= 1
            skippedlastright = True
            ritem = totalvals[roffset][0]
            continue
        ritem = totalvals[roffset][0]
        #minska
    elif litem + ritem < summ:
        loffset += 1
        if skippedlastright:
            roffset += 1
            ritem = totalvals[roffset][0]
        if totalvals[loffset][1] == totalvals[roffset][1]:
            loffset += 1
            skippedlastleft = True
            litem = totalvals[loffset][0]
            continue
        litem = totalvals[loffset][0]
        #öka
    
    
print("YES" if possible else "NO")