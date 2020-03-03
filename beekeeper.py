import re
def getdoubles(word):
    doubles = 0
    doubles += len(re.findall("aa", word))
    doubles += len(re.findall("ee", word))
    doubles += len(re.findall("ii", word))
    doubles += len(re.findall("oo", word))
    doubles += len(re.findall("uu", word))
    doubles += len(re.findall("yy", word))
    return doubles

while True:
    cases = int(input())
    words = []
    paired = {}
    pairedsorted = []
    if cases == 0:
        break
    for n in range(cases):
        words.append(input())
    for word in words:
        paired[word] = getdoubles(word)
    pairedsorted = sorted(paired.items(), key=lambda x: x[1], reverse=True)
    print(pairedsorted[0][0])