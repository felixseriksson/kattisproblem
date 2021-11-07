# precomputation
# from math import log2
# highest = [] # highest for 4, 8, 16, ..., 4*2**21
# bits = 4
# logsum, i = 0, 1
# while bits <= 4*2**20:
#     if logsum < bits:
#         i += 1
#         logsum += log2(i)
#     else:
#         highest.append(i-1)
#         bits *= 2
# print(highest)
vals = [3, 5, 8, 12, 20, 34, 57, 98, 170, 300, 536, 966, 1754, 3210, 5910, 10944, 20366, 38064, 71421, 134480, 254016]
inp = int(input())
while inp != 0:
    print(vals[(inp-1960)//10])
    inp = int(input())