def checkpossibilities(listtocheck, goallist, depth, currentpath):
    if listtocheck == goallist:
        #kolla legitimitet
        #spara på nåt vis
        print("ja")
        return
    if depth == 3:
        del currentpath[-1]
        return
    for length in reversed(range(1, 4)):
        if length > len(listtocheck):
            continue
        for position in range(len(listtocheck)-length+1):
            combo = listtocheck[position:position+length]
            for letter in ["A", "B", "C"]:
                newlist = listtocheck.copy()
                del newlist[position:position+length]
                if letter in newlist:
                    continue
                if len(combo) == 1 and combo[0] == letter:
                    continue
                currentpath.append([tuple(combo), letter])
                newlist.insert(position, letter)
                newdepth = depth + 1
                #nåt med spara vägen
                checkpossibilities(newlist, goallist, newdepth, currentpath)




goal = [x for x in input()]
start = [x for x in input()]
checkpossibilities(start, goal, 0, [])