from collections import deque
n = int(input())
grid = [[char for char in input()] for _ in range(n)]

q = deque()
for i in range(n):
    for j in range(n):
        if grid[i][j] == "K":
            q.append((i, j))
            grid[i][j] = 0

offsets = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

while q:
    currx, curry = q.popleft()
    for ox, oy in offsets:
        newx, newy = currx + ox, curry + oy
        if newx < 0 or newx >= n or newy < 0 or newy >= n:
            continue
        if grid[newx][newy] == ".":
            grid[newx][newy] = grid[currx][curry] + 1
            q.append((newx, newy))

print(-1 if grid[0][0] == "." else grid[0][0])