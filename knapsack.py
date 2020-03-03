import sys

def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W+1)] for x in range(n+1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w]
    itemnumber = n
    weight = W
    items = ""
    numberofitems = 0
    while K[itemnumber][weight] != 0:
        if K[itemnumber][weight] == K[itemnumber-1][weight]:
            itemnumber -= 1
        else:
            items += str(int(itemnumber-1)) + " "
            numberofitems += 1
            itemnumber -= 1
            weight -= wt[itemnumber]

    return K[n][W], items, numberofitems

# while True:
#     W, n = [int(x) for x in sys.stdin.readline().strip("\n").split()]
#     if not W:
#         break
#     wt = []
#     val = []
#     for n in range(n):
#         value, weight = [int(x) for x in sys.stdin.readline().strip("\n").split()]
#         val.append(value)
#         wt.append(weight)
#     print(knapSack(W, wt, val, n))

counter = 0

# for line in sys.stdin.readlines():
#     if counter == 0:
#         W, n = [int(x) for x in line.strip("\n").split()]
#         wt = []
#         val = []
#         counter = n
#         continue
#     else:
#         value, weight = [int(x) for x in line.strip("\n").split()]
#         val.append(value)
#         wt.append(weight)
#         counter -= 1
#     if counter == 0:
#         value, listofitems, howmanyitems = knapSack(W, wt, val, n)
#         print(howmanyitems)
#         print(listofitems)


#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

counter = 0

while True:
    if counter == 0:
        W, n = [int(x) for x in input().split()]
        wt = []
        val = []
        counter = n
        continue
    else:
        value, weight = [int(x) for x in input().split()]
        val.append(value)
        wt.append(weight)
        counter -= 1
    if counter == 0:
        print(knapSack(W, wt, val, n))
        break