valuestoops = {}
def getops(n):
    testing = []
    if n % 4 == 0:
        testing.append("*")
    elif n % 4 == 1:
        testing.append("+")
    elif n % 4 == 2:
        testing.append("-")
    elif n % 4 == 3:
        testing.append("//")
    if n % 16 >= 0 and n % 16 < 4:
        testing.append("*")
    elif n % 16 >= 4 and n % 16 < 8:
        testing.append("+")
    elif n % 16 >= 8 and n % 16 < 12:
        testing.append("-")
    elif n % 16 >= 12 and n % 16 < 16:
        testing.append("//")
    if n >= 0 and n < 16:
        testing.append("*")
    elif n >= 16 and n < 32:
        testing.append("+")
    elif n >= 32 and n < 48:
        testing.append("-")
    elif n >= 48 and n < 64:
        testing.append("//")
    return testing

for n in range(64):
    templist = getops(n)
    val = eval("4" + str(templist[0]) + "4" + str(templist[1]) + "4" + str(templist[2]) + "4")
    '''
    if val == 4.25:
        val = 4
        continue
    elif val == -3.75:
        val = -4
    elif val == 3.75:
        val = 4
    elif val == 0.0625:
        val = 0
    elif val == 1:
        val = 0
    else:
        val = eval("4" + str(templist[0]) + "4" + str(templist[1]) + "4" + str(templist[2]) + "4")
        #print(val)
    '''
    val = eval("4" + str(templist[0]) + "4" + str(templist[1]) + "4" + str(templist[2]) + "4")
    #if val not in valuestoops:
    #    valuestoops[float(val)] = str("4 " + str(templist[0]) + " 4 " + str(templist[1]) + " 4 " + str(templist[2]) + " 4 ")
    valuestoops[int(val)] = str("4 " + str(templist[0]) + " 4 " + str(templist[1]) + " 4 " + str(templist[2]) + " 4 ")
    for key in valuestoops.keys():
        if "//" in valuestoops[key]:
            valuestoops[key] = valuestoops[key].replace("//", "/")
#print(valuestoops)

cases = int(input())

for n in range(cases):
    num = int(input())
    if num in valuestoops:
        print(str(valuestoops[num]) + "= " + str(num))
    else:
        print("no solution")