d = {"clank": "a", "bong": "b", "click": "c",
     "tap": "d", "poing": "e", "clonk": "f",
     "clack": "g", "ping": "h", "tip": "i",
     "cloing": "j", "tic": "k", "cling": "l",
     "bing": "m", "pong": "n", "clang": "o",
     "pang": "p", "clong": "q", "tac": "r",
     "boing": "s", "boink": "t", "cloink": "u",
     "rattle": "v", "clock": "w", "toc": "x",
     "clink": "y", "tuc": "z", "whack": " "}
capsflag = False
shiftflag = False
ret = []
for _ in range(int(input())):
    s = input()
    if s == "pop":
        try:
            del ret[-1]
        except:
            pass
    elif s == "bump":
        capsflag = not capsflag
    elif s == "dink":
        shiftflag = True
    elif s == "thumb":
        shiftflag = False
    else:
        w = d[s]
        if capsflag != shiftflag:
            ret.append(w.upper())
        else:
            ret.append(w)
print("".join(ret))