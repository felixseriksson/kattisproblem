rows, columns, k = [int(x) for x in input().split()]
grid = []
string = "#"*(columns+2)
grid.append(string)
for n in range(rows):
    grid.append([char for char in input()])
    grid[n+1].insert(0, "#")
    grid[n+1].append("#")
string = "#"*(columns+2)
grid.append(string)

currentlayer = [(1, 1)]
grid[1][1] = 0
while currentlayer:
    nextlayer = []
    for x, y in currentlayer:
        neighbours = [(x, y+1), (x, y-1), (x-1, y), (x+1 ,y)]
        for neighbour in neighbours:
            if grid[neighbour[0]][neighbour[1]] == ".":
                grid[neighbour[0]][neighbour[1]] = int(grid[x][y]) + 1
                nextlayer.append((neighbour))
    currentlayer = nextlayer
val = grid[-2][-2]
if val == "#" or val == ".":
    print("nej")
else:
    print(val)