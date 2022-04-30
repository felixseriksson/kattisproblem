n, q = [int(x) for x in input().split()]

default = (0, 0)
money = [(0, -1) for _ in range(n)]

for i in range(1, q+1):
    cmd, nums = input().split(" ", maxsplit = 1)
    if cmd == "PRINT":
        if default[1] >= money[int(nums)-1][1]:
            print(default[0])
        else:
            print(money[int(nums)-1][0])
    elif cmd == "RESTART":
        default = (int(nums), i)
    else:
        idx, val = [int(x) for x in nums.split()]
        money[idx-1] = (val, i)