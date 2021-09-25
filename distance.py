xs, ys = [], []
for _ in range(int(input())):
    x, y = [int(a) for a in input().split()]
    xs.append(x)
    ys.append(y)

xs = sorted(xs)
ys = sorted(ys)

resx, resy = 0, 0
sx, sy = 0, 0
for i in range(len(xs)):
    resx += xs[i] * (i) - sx
    sx += xs[i]
    resy += ys[i] * (i) - sy
    sy += ys[i]

print(resx + resy)