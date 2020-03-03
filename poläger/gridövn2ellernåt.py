from collections import defaultdict
from heapq import heapify, heappop, heappush

def dijkstra(g, f, t):
    # g = defaultdict(list)
    # for l,r,c in edges:
    #     g[l].append((c,r))

    q, seen, mins = [(0,f,())], set(), {f: 0}
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return -1, -1

# def makereadable(foundpath):
#     # tar in input direkt från djikstras
#     path = []
#     for n in str(foundpath):
#         if n.isalnum():
#             path.append(n)
#     lengthofpath = path.pop(0)
#     return lengthofpath, reversed(path)
#     # returnerar längden på kortaste stigen, en lista med noderna i den kortaste stigen som strings

# # graphen görs av en kantlista där varje entry är en tuple på formen (från, till, vikt)
# # där alltså från och till kan vara ints eller strings men vikt är en int


# # output ges på formen (vikt, (sista noden,(näst sista noden,(...,(första noden,())))))
# print(edges)
# res = dijkstra(edges, "A", "C")
# print(res)
# print(makereadable(res))

g = defaultdict(list)

# def coordstoname(tup):
#     return str(tup[0]) + "-" + str(tup[1])
# def nametocoords(string):
#     row, col = [int(x) for x in string.split("-")]
#     return (row, col)

rows, columns = [int(x) for x in input().split()]
for row in range(rows):
    temp = [int(char) for char in input()]
    for col in range(columns):
        name = row*columns + col
        k = temp[col]
        if row + k >= rows:
            pass
        else:
            g[name].append((1, name + k*columns))
        if row - k < 0:
            pass
        else:
            g[name].append((1, name - k*columns))
        if col + k >= columns:
            pass
        else:
            g[name].append((1, name + k))
        if col - k < 0:
            pass
        else:
            g[name].append((1, name - k))
#print(edges)
steps, path = dijkstra(g, 0, rows*columns-1)
print(steps)