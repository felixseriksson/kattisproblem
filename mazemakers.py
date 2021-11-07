from collections import defaultdict, deque
directions = {
    # xoffset, yoffset
    "0": [[0, 1], [1, 0], [0, -1], [-1, 0]],
    "1": [[0, 1], [1, 0], [0, -1]],
    "2": [[-1, 0], [0, 1], [1, 0]],
    "3": [[0, 1], [1, 0]],
    "4": [[0, -1], [-1, 0], [0, 1]],
    "5": [[0, 1], [0, -1]],
    "6": [[-1, 0], [0, 1]],
    "7": [[0, 1]],
    "8": [[1, 0], [0, -1], [-1, 0]],
    "9": [[1, 0], [0, -1]],
    "A": [[1, 0], [-1, 0]],
    "B": [[1, 0]],
    "C": [[0, -1], [-1, 0]],
    "D": [[0, -1]],
    "E": [[-1, 0]],
    "F": [[None, None]],
}

height, width = [int(x) for x in input().split()]
while height != 0 and width != 0:
    terminals = []
    graph = defaultdict(list)
    for i in range(height):
        row = input()
        for j in range(width):
            cell = row[j]
            dirs = directions[cell]
            for xoffs, yoffs in dirs:
                if xoffs is None:
                    graph[(i, j)] = []
                    continue
                if (i == 0 and yoffs == 1) or (i == height-1 and yoffs == -1) or (j == 0 and xoffs == -1) or (j == width-1 and xoffs == 1):
                    terminals.append((i, j))
                    continue
                graph[(i, j)].append((i - yoffs, j + xoffs))

    # for key, val in graph.items():
    #     print(key)
    #     print(val)
    # print("terminals")
    # print(terminals)

    q = deque()
    q.append(terminals[0])
    goal = terminals[1]
    visited = {a:0 for a in graph.keys()}
    multiplepaths = False
    while q:
        current = q.popleft()
        if visited[current]:
            multiplepaths = True
        visited[current] = 1
        for neighbour in graph[current]:
            if not visited[neighbour]:
                q.append(neighbour)

    if not visited[goal]:
        print("NO SOLUTION")
    elif sum(visited.values()) != width*height:
        print("UNREACHABLE CELL")
    elif multiplepaths:
        print("MULTIPLE PATHS")
    else:
        print("MAZE OK")

    height, width = [int(x) for x in input().split()]