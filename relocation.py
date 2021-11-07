n, q = [int(x) for x in input().split()]
positions = {i:j for i, j in enumerate([int(x) for x in input().split()], start=1)}
for _ in range(q):
    typee, a, b = [int(x) for x in input().split()]
    if typee-1:
        print(abs(positions[a]-positions[b]))
    else:
        positions[a] = b