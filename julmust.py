r = int(input())
lo, hi = 1, r
for i in range(1, 86):
    mid = (lo+hi)//2
    print(i*mid, flush = True)
    response = input()
    if response == "exact":
        exit(0)
    elif response == "less":
        hi = mid-1
    else:
        lo = mid+1