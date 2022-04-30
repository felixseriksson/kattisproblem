def intervalcover(G, I):
    """
        G = [a, b] and I = [[a_1, b_n], ..., [a_n, b_n]]
        Intervals are [inclusive, inclusive] by default.
        To handle [inclusive, exclusive), modify code as commented below.
        Returns smallest list of indices of intervals in I required to cover G.
        On failure, returns empty list. 
    """
    ret = []
    n = len(I)
    S = list(range(n))
    S = sorted(S, key = lambda x: I[x])
    curr = G[0]
    i = 0
    while curr < G[1] or not ret:
    # To handle [inclusive, exclusive), exchange while loop for
    # while curr < G[1]:
        mx = [curr, -1]
        while i < n and I[S[i]][0] <= curr:
            newpair = [I[S[i]][1], S[i]]
            if mx[0] < newpair[0] or (mx[0] == mx[0] and mx[1] < newpair[1]):
                mx = newpair
            i += 1
        if mx[1] == -1:
            return -1
        curr = mx[0]
        ret.append(mx[1])
    return ret

while True:
    try:
        target = [float(x) for x in input().split()]
        n = int(input())
        intervals = []
        for _ in range(n):
            intervals.append([float(x) for x in input().split()])
        res = intervalcover(target, intervals)
        if res == -1:
            print("impossible")
        else:
            print(len(res))
            print(" ".join([str(x) for x in res]))
    except:
        exit(0)