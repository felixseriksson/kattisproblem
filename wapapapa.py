testcases = int(input())
for testcase in range(testcases):
    words = input().split()
    inp = input().split()
    while inp[-1] != "say?":
        sound = inp[-1]
        words = [word for word in words if word != sound]
        inp = input().split()
    print(" ".join(words))