n = int(input())
figs = []
while n != 0:
    fig = []
    length = 0
    for _ in range(n):
        fig.append([char for char in input()])
        length = max(length, len(fig[-1]))

    for row in fig:
        left = length - len(row)
        for _ in range(left):
            row.append(" ")

    newfig = [[None for _ in range(len(fig))] for _ in range(len(fig[0]))]
    for i in range(1, len(fig)+1):
        for j in range(len(fig[0])):
            newfig[j][i-1] = fig[-i][j]

    for line in newfig:
        for i in range(len(line)):
            if line[i] == "-":
                line[i] = "|"
            elif line[i] == "|":
                line[i] = "-"
    
    figs.append(newfig)
    n = int(input())

for fig in figs:
    for line in fig:
        print("".join(line).rstrip(), end="\n")
    if fig != figs[-1]:
        print()