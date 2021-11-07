t = int(input())
points = [[int(i) for i in input().split()] for _ in range(t)]
print(max([(points[i][1]-points[i-1][1])//(points[i][0] - points[i-1][0]) for i in range(1,t)]))