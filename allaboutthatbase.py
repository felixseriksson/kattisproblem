lookup = dict()
for i in range(1, 10):
    lookup[str(i)] = i
for i in range(97, 123):
    lookup[chr(i)] = i - 87
lookup["#"] = 36
lookup["0"] = 0

ops = {
    "+": lambda x, y: x+y,
    "-": lambda x, y: x-y,
    "*": lambda x, y: x*y,
    "/": lambda x, y: x/y
}

def eval(number, base):
    ret = 0
    for i, val in enumerate(number[::-1]):
        ret += lookup[val]*lookup[base]**i
    return ret

def valid(number, base):
    flag = True
    numbag = set([char for char in number])
    if lookup[base] == 1:
        if len(numbag) > 1 or "1" not in numbag:
            flag = False
    else:
        if max([lookup[val] for val in numbag]) >= lookup[base]:
            flag = False
    evalres = eval(number, base)
    if evalres <= 0 or evalres >= 2**32:
        flag = False
    return flag

n = int(input())
for _ in range(n):
    a, op, b, _, c = input().split(" ")
    retstring = []
    for base in [str(i) for i in range(1, 10)]:
        if valid(a, base) and valid(b, base) and valid(c, base):
            if ops[op](eval(a, base), eval(b, base)) == eval(c, base):
                retstring.append(base)
    for base in [chr(i) for i in range(97, 123)]:
        if valid(a, base) and valid(b, base) and valid(c, base):
            if ops[op](eval(a, base), eval(b, base)) == eval(c, base):
                retstring.append(base)
    for base in ["#"]:
        if valid(a, base) and valid(b, base) and valid(c, base):
            if ops[op](eval(a, base), eval(b, base)) == eval(c, base):
                retstring.append("0")
    if retstring:
        print("".join(retstring))
    else:
        print("invalid")