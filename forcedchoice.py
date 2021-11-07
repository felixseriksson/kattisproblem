n, p, s = [int(x) for x in input().split()]
for _ in range(s): print("KEEP" if p in [int(x) for x in input().split()][1:] else "REMOVE")