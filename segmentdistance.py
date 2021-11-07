def dot(a, b):
    return a[0]*b[0] + a[1]*b[1]

def dist(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

def segseg(a, b, c, d):
    if properinter(a, b, c, d):
        return 0
    return min(segpoint(a, b, c), segpoint(a, b, d), segpoint(c, d, a), segpoint(c, d, b))

def cross(a, b):
    return a[0]*b[1] - a[1]*b[0]

def linedist(a, b, c):
    num = abs((b[0] - a[0])*(a[1] - c[1]) - (a[0] - c[0])*(b[1] - a[1]))
    den = ((b[0] - a[0])**2 + (b[1] - a[1])**2)**0.5
    return num/den

def segpoint(a, b, c):
    if a == b:
        return dist(a, c)
    v = [b[0]-a[0], b[1]-a[1]]
    if dot(v,a) < dot(v,c) and dot(v,c) < dot(v,b):
        return linedist(a, b, c)
    return min(dist(a, c), dist(b, c))

def orient(a, b, c):
    v1 = [b[0]-a[0], b[1]-a[1]]
    v2 = [c[0]-a[0], c[1]-a[1]]
    return cross(v1, v2)

def properinter(a, b, c, d):
    oa, ob, oc, od = orient(c, d, a), orient(c, d, b), orient(a, b, c), orient(a, b, d)
    if oa*ob < 0 and oc*od < 0:
        return True
    return False

# print(linedist([0, 0], [-1, -1], [0,-1]))
for _ in range(int(input())):
    x1, y1, x2, y2, x3, y3, x4, y4 = [int(x) for x in input().split()]
    print(segseg([x1, y1], [x2, y2], [x3, y3], [x4, y4]))