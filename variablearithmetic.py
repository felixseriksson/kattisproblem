from collections import defaultdict
tokenvalues = defaultdict()
inp = input()
while inp != "0":
    if "=" in inp:
        name, value = inp.split(" = ")
        tokenvalues[name] = int(value)
    else:
        returnstring, currentsum = [], 0
        tokens = inp.split(" + ")
        for t in tokens:
            if t.isnumeric():
                currentsum += int(t)
            else:
                try:
                    currentsum += tokenvalues[t]
                except:
                    returnstring.append(t)
        if currentsum == 0 and not returnstring:
            print(0)
        elif currentsum == 0:
            print(" + ".join(returnstring))
        elif not returnstring:
            print(str(currentsum))
        else:
            print(str(currentsum) + " + " + " + ".join(returnstring))
    inp = input()