from math import sqrt
def needed(node, parent):
    if nodes[node] != -1:
        return nodes[node]
    else:
        ret = 0
        for edge in edges[node]:
            if edge[0] == parent:
                continue
            else:
                child = edge[0]
                if edge[2] == 0:
                    ret = max(ret, needed(child, node)*100/edge[1])
                else:
                    mn = needed(child, node)
                    if mn > 1:
                        ret = max(ret, sqrt(mn)*100/edge[1])
                    else:
                        ret = max(ret, mn*100/edge[1])
        return ret

from collections import defaultdict
n = int(input())
edges = defaultdict(list)
for _ in range(n-1):
    a, b, flow, sup = [int(x) for x in input().split()]
    edges[a-1].append([b-1, flow, sup])
    edges[b-1].append([a-1, flow, sup])
nodes = [float(x) for x in input().split()]
print(needed(0, None))