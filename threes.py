k = int(input())
while True:
    # try:
    #     assert k == 1
    #     print("{ }")
    # except AssertionError:
    #     pass
    # if k == 0:
    #     exit(0)
    # else:
    #     s = []
    #     k = int(input())
    #     try:
    #         assert k == 0
    #         exit(0)
    #     except AssertionError:
    #         pass
    #     k = enumerate(reversed(str(bin(int(k)-1))[2:]))
    #     for exp, num in k:
    #         if int(num) == 1:
    #             s.append(3**exp)
    #         else:
    #             pass
    #     st = "{ "
    #     for char in s:
    #         st = st + ", {}".format(str(char))

    #     st += " }"
    #     st = "{ " + st[4:]
    #     print(st)
    if k == 0:
        exit(0)
    elif k == 1:
        print("{ }")
        k = int(input())
    else:
        s = []
        k = enumerate(reversed(str(bin(int(k)-1))[2:]))
        for exp, num in k:
            if int(num) == 1:
                s.append(3**exp)
            else:
                pass
        st = "{ "
        for char in s:
            st = st + ", {}".format(str(char))

        st += " }"
        st = "{ " + st[4:]
        print(st)
        k = int(input())