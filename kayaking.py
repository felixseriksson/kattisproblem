def works(maxval, com,  beg, nor, exp, kay):
    sortedcombs = sorted(com.items(), key = lambda x: x[1])
    begav, norav, expav = beg, nor, exp
    works = True
    for kayak in kay:
        for comb in sortedcombs:
            if (comb[0][0] > begav) or (comb[0][1] > norav) or (comb[0][2] > expav):
                continue
            else:
                if maxval <= comb[1]*kayak:
                    begav -= comb[0][0]
                    norav -= comb[0][1]
                    expav -= comb[0][2]
                    break
        else:
            works = False
        if works == False:
            return False
    return True


beginners, normals, experienced = [int(x) for x in input().split()]
sb, sn, se = [int(x) for x in input().split()]
combs = {(2, 0, 0): sb + sb, (1, 1, 0): sb + sn, (1, 0, 1): sb + se, (0, 2, 0): sn + sn, (0, 1, 1): sn + se, (0, 0, 2): se + se}
kayaks = sorted([int(x) for x in input().split()])
left = 2*sb*kayaks[0]
right = 2*se*kayaks[-1]
while round(right, 2) != round(left, 2):
    mid = (left+right)/2
    if works(mid, combs, beginners, normals, experienced, kayaks):
        left = mid
    else:
        right = mid
print(int((left+right)/2))