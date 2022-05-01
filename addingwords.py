from sys import stdin

def calc(l):
    ret = [wordtoint[l[0]]]
    l = l[1:]
    for op, term in zip(l[::2], l[1::2]):
        if op == "+":
            ret.append(wordtoint[term])
        else:
            ret.append(-1*wordtoint[term])
    return sum(ret)

wordtoint, inttoword = dict(), dict()
for line in stdin.readlines():
    cmd, *rest = line.strip().split()
    if not rest:
        wordtoint.clear()
        inttoword.clear()
    elif cmd == "def":
        a, b = rest[0], int(rest[1])
        if a in wordtoint.keys():
            oldint = wordtoint[a]
            del wordtoint[a]
            del inttoword[oldint]
        wordtoint[a] = b
        inttoword[b] = a
    else:
        oldrest = rest
        rest = rest[:-1]
        for word in rest[::2]:
            if not word in wordtoint.keys():
                res = "unknown"
                break
        else:
            res = calc(rest)
            if res in inttoword.keys():
                res = inttoword[res]
            else:
                res = "unknown"
        oldrest.append(res)
        print(" ".join(oldrest))