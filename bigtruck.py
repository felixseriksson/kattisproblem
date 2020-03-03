from collections import defaultdict
from heapq import heapify, heappop, heappush


def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))
    q, seen, mins = [(0, f, ())], set(), {f: 0}
    maxobjects = {1: nodevalues[1]}
    while q:
        (cost, v1, path) = heappop(q)
        objects = maxobjects[v1]
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t:
                return (cost, path, objects)
            for c, v2 in g.get(v1, ()):
                nextobjects = nodevalues[v2]
                if v2 in seen:
                    continue
                prev = mins.get(v2, None)
                try:
                    previousobjects = maxobjects[v2]
                except KeyError:
                    maxobjects[v2] = nodevalues[v2]
                    previousobjects = maxobjects[v2]
                next = cost + c
                new = objects + nextobjects
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))
                    maxobjects[v2] = new
                elif next == prev:
                    if new > previousobjects:
                        mins[v2] = next
                        heappush(q, (next, v2, path))
                        maxobjects[v2] = new
    return float("inf")


def makereadable(foundpath):
    path = []
    for n in str(foundpath):
        if n.isalnum():
            path.append(n)
    lengthofpath = path.pop(0)
    return lengthofpath, reversed(path)


numberofnodes = int(input())
listofnodevalues = [int(x) for x in input().split()]
nodevalues = {}
for n in range(len(listofnodevalues)):
    nodevalues[n+1] = listofnodevalues[n]
numberofedges = int(input())
edges = []
for x in range(numberofedges):
    a, b, d = [int(x) for x in input().split()]
    edges.append((a, b, d))
    edges.append((b, a, d))
try:
    cost, path, objects = dijkstra(edges, 1, numberofnodes)
    print(cost, objects)
except:
    print("impossible")