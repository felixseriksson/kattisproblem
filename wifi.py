cases = int(input())
for case in range(cases):
    maxesspoints, numhouses = [int(x) for x in input().split()]
    houses = []
    for _ in range(numhouses):
        houses.append(int(input()))
    if maxesspoints >= numhouses:
        print("1.0")
        continue
    houses = sorted(houses)
    left = 0 # needs numhouses access points
    right = 2000000
    while round(right, 2) != round(left, 2):
        mid = (right + left) / 2
        needed = 1
        furthestright = houses[0] + 2*mid
        for house in houses:
            if house <= furthestright:
                pass
            else:
                needed += 1
                furthestright = house + 2*mid
        if needed > maxesspoints:
            left = mid
        else:
            right = mid
    print(round(left, 1))