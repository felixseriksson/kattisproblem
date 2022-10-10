n = int(input())
s = [int(input()) for _ in range(n)]

def indexLargerThan(arr, l, r, key):
    while r - l > 1:
        m = (r + l) // 2
        if arr[m] >= key:
            r = m
        else:
            l = m
    return r

def lis(s, n):
    tail = [0 for _ in range(n+1)]
    empty = 0
    tail[0] = s[0]
    empty = 1
    for i in range(1, n):
        if s[i] < tail[0]:
            tail[0] = s[i]
        elif s[i] > tail[empty - 1]:
            tail[empty] = s[i]
            empty += 1
        else:
            index = indexLargerThan(tail, -1, empty - 1, s[i])
            tail[index] = s[i]
    return empty

print(lis(s, n))