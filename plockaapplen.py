# n, k = [int(x) for x in input().split()]
# ls = [[None]*(n+2)]
# for _ in range(2):
#     t = [None]
#     t.extend([int(x) for x in input().split()])
#     t.append(None)
#     ls.append(t)
# ls.append([None]*(n+2))
# for yeet in ls:
#     print(yeet)

# def apples(row, col, treesleft, orchard, numofapples):
#     # if treesleft == 0:
#     #     return numofapples
#     # else:
#     #     numofapples += ls[row][col][0]
#     #     treesleft -= 1
#     #     orchard[row][col][1] = 1
#     #     totry = []
#     #     for direction in [[1,0], [0, -1], [-1, 0], [0, 1]]:
#     #         # down, left, up, right
#     #         if (row+direction[0] == 0 or row+direction[0] == 1) and (col+direction[1] >= 0 and col+direction[1] < n):
#     #             state = orchard[row+direction[0]][col+direction[1]][1]
#     #         else:
#     #             continue
#     #         if state == 0:
#     #             totry.append(direction)
#     #     if not totry:
#     #         return numofapples
#     #     else:
#     #         return max([apples(row+a[0], col+a[1], treesleft, orchard, numofapples) for a in totry])
#     if treesleft == 0:
#         return numofapples
#     elif orchard[row][col] is None:
#         return numofapples
#     else:
#         numofapples += orchard[row][col]
#         # for r in orchard:
#         #     print(r)
#         treesleft -= 1
#         orchard[row][col] = None
#         return max([apples(row+a, col+b, treesleft, orchard, numofapples) for a, b in [(1, 0), (0, -1), (-1, 0), (0, 1)]])

# print(apples(2, 1, k, ls, 0))

n, k = [int(x) for x in input().split()]
ls = [[None]*(n+2)]
for _ in range(2):
    t = [None]
    t.extend([int(x) for x in input().split()])
    t.append(None)
    ls.append(t)
ls.append([None]*(n+2))

def apples(row, col, treesleft, currentapples, orchard):
    if treesleft == 0:
        return currentapples
    elif orchard[row][col] is None:
        return currentapples
    else:
        currentapples += orchard[row][col]
        treesleft -= 1
        pos = []
        for a,b in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
            neworchard = orchard.copy()
            neworchard[row][col] = None
            pos.append(apples(row + a, col + b, treesleft, currentapples, neworchard))
        return max(pos)

print(apples(2, 1, k, 0, ls))