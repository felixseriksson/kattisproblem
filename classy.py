from functools import cmp_to_key

def compare(p1, p2):
    s1 = d[p1].split("-")[::-1]
    s2 = d[p2].split("-")[::-1]

    if len(s1) > len(s2):
        for _ in range(len(s1)-len(s2)):
            s2.append("middle")
    elif len(s2) > len(s1):
        for _ in range(len(s2)-len(s1)):
            s1.append("middle")

    # return < 0 when s1 < s2
    # return > 0 when s1 > s2
    # return 0 when s1 == s2
    for a, b in zip(s1, s2):
        if c[a] == c[b]:
            continue
        elif c[a] < c[b]:
            return -1
        elif c[a] > c[b]:
            return 1
    else:
        if p1 < p2:
            return 1
        elif p1 > p2:
            return -1
    return 0

c = {"lower": 1, "middle": 2, "upper": 3}

for _ in range(int(input())):
    d = dict()
    people = []
    for _ in range(int(input())):
        person, identifier = input().split(": ")
        identifier = identifier[:-6]
        d[person] = identifier
        people.append(person)
    people = sorted(people, key = cmp_to_key(compare), reverse = True)
    for person in people:
        print(person)
    print("="*30)