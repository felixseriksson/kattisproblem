# while True:
#     try:
#         n, l, w = [int(x) for x in input().split()]
#         s = []
#         for _ in range(n):
#             s.append([int(x) for x in input().split()])
#         s = sorted(s, key = lambda x: x[0] - (x[1]**2 - w**2/4)**0.5)
#         s = [[x[0] - (x[1]**2 - w**2/4)**0.5, x[0] + (x[1]**2 - w**2/4)**0.5] for x in s]
#         # s.append([10**9, 10**9])
#         curr = 0
#         res = 0
#         i = 0
#         while curr < l:
#             # cands = []
#             # if s[i][0] > curr:
#             #     print(-1)
#             #     break
#             # else:
#             #     while s[i][0] <= curr:
#             #         cands.append(s[i][1])
#             #         i += 1
#             # curr = max(cands)
#             # res += 1
        
#         # else:
#         #     print(res)
#             if i == len(s) or s[i][0] > curr:
#                 print(-1)
#                 break
#             cmax = s[i][1]
#             while (i+1 < len(s)) and s[i+1][0] <= curr:
#                 i += 1
#                 cmax = max(cmax, s[i][1])
#             if cmax < curr:
#                 print(-1)
#                 break
#             res += 1
#             curr = cmax
#             i += 1
#         else:
#             print(res)

#     except Exception as e:
#         exit(0)

def intervalcover(a, target):
    """
        Returns minimum number of intervals [x_1, x_2] in a needed to completely
        cover target = [t_1, t_2]. Intervals are taken to be closed, i. e.
        [x_1, x_2] and [x_2, x_3] cover [x_1, x_3].
        a is a list of lists of the form [x_1, x_2].
        target is a single list [t_1, t_2].
        If covering is impossible, returns -1.
    """
    a = sorted(a)
    maxa = a[-1][1]
    a.append([maxa + 1, maxa + 1])
    left, right = target[0], target[0] - 1
    ret = 0
    i = 0
    while True:
        if a[i][0] <= left:
            right = max(a[i][1], right)
            i += 1
        else:
            left = right
            ret += 1
            if a[i][0] > right or right >= target[1]:
                break
        i += 1
    if right < target[1]:
        return -1
    return ret

while True:
    try:
        n, l, w = [int(x) for x in input().split()]
        s = []
        for _ in range(n):
            s.append([int(x) for x in input().split()])
        s = sorted(s, key = lambda x: x[0] - (x[1]**2 - w**2/4)**0.5)
        s = [[x[0] - (x[1]**2 - w**2/4)**0.5, x[0] + (x[1]**2 - w**2/4)**0.5] for x in s]
        
        print(intervalcover(s, [0, l]))


    except Exception as e:
        exit(0)