'''
from heapq import heapify, heappop
n, m = [int(x) for x in input().split()]

l1 = []
for num in range(n):
    l1.append(int(input()))
heapify(l1)

# ctr = 0
# i = 0
# if n >= m:
#     while i < m:
#         heapmin = heappop(l1)
#         inputmin = int(input())
#         i += 1
#         if heapmin == inputmin:
#             ctr += 1
#             continue
#         elif heapmin > inputmin:
#             inputmin = int(input())
#             i += 1
#             continue
#         elif heapmin < inputmin:
#             heapmin = heappop(l1)
#             continue

# elif m > n:
#     while i < n:
#         heapmin = heappop(l1)
#         inputmin = int(input())
#         i += 1
#         if heapmin == inputmin:
#             ctr += 1
#             continue
#         elif heapmin > inputmin:
#             inputmin = int(input())
#             continue
#         elif heapmin < inputmin:
#             heapmin = heappop(l1)
#             i += 1
#             continue
#--------------------------------------------------------------------------------------------------------------------------------
# 3 fall:
# heapmin == inputmin --> ta från båda, öka ctr med en
# heapmin < inputmin --> ta från heap
# heapmin > inputmin --> ta från input
# finns övergripande två fall:
# antingen är den begränsande faktorn |heap| dvs n, eller |input| dvs m
# beroende på vilken det är så måste antal tagna från den som är mindre trackas och loopen köras tills den begränsande är slut, resten i den andra kan räknas bort

i, ctr, tafrånheap, tafråninput = 0, 0, True, True
if n >= m:
    while i < m:
        #först
        if tafrånheap == True:
            heapmin = heappop(l1)
        if tafråninput == True:
            inputmin = int(input())
            i += 1
        #sen
        if heapmin == inputmin:
            tafrånheap = True
            tafråninput = True
            ctr += 1
            continue
        elif heapmin < inputmin:
            tafrånheap = True
            tafråninput = False
            continue
        elif heapmin > inputmin:
            tafrånheap = False
            tafråninput = True
            continue

elif m > n:
    while i < n:
        #först
        if tafrånheap == True:
            heapmin = heappop(l1)
            i += 1
        if tafråninput == True:
            inputmin = int(input())
        #sen
        if heapmin == inputmin:
            tafrånheap = True
            tafråninput = True
            ctr += 1
            continue
        elif heapmin < inputmin:
            tafrånheap = True
            tafråninput = False
            continue
        elif heapmin > inputmin:
            tafrånheap = False
            tafråninput = True
            continue
print(ctr)
#-----------------------------------------------------------------------------------------------------------------------------
'''
'''
from heapq import heapify, heappop
n, m = [int(x) for x in input().split()]

while True:
    if (n,m) == (0,0):
        break
    l1 = []
    for num in range(n):
        l1.append(int(input()))
    heapify(l1)
    i, ctr, tafrånheap, tafråninput = 0, 0, True, True
    if n >= m:
        while i < m:
            #först
            if tafrånheap == True:
                heapmin = heappop(l1)
            if tafråninput == True:
                inputmin = int(input())
                i += 1
            #sen
            if heapmin == inputmin:
                tafrånheap = True
                tafråninput = True
                ctr += 1
                continue
            elif heapmin < inputmin:
                tafrånheap = True
                tafråninput = False
                continue
            elif heapmin > inputmin:
                tafrånheap = False
                tafråninput = True
                continue
        print("ctr:", ctr)
        n, m = [int(x) for x in input().split()]
        continue

    elif m > n:
        while i < n:
            #först
            if tafrånheap == True:
                heapmin = heappop(l1)
                i += 1
            if tafråninput == True:
                inputmin = int(input())
            #sen
            if heapmin == inputmin:
                tafrånheap = True
                tafråninput = True
                ctr += 1
                continue
            elif heapmin < inputmin:
                tafrånheap = True
                tafråninput = False
                continue
            elif heapmin > inputmin:
                tafrånheap = False
                tafråninput = True
                continue
        print("ctr:", ctr)
        inp = ["False"]
        while len(inp) != 2:
            inp = [int(x) for x in input().split()]
        n, m = inp
        continue
'''
#test with sets:
n, m = [int(x) for x in input().split()]
while (n, m) != (0, 0):
    sett = set()
    for i in range(n+m):
        sett.add(int(input()))
    print(n+m-len(sett))
    n, m = [int(x) for x in input().split()]