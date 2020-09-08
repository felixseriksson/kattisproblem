# def catalan(n):
#     cat = 1
#     for k in range(2, n+1):
#         cat *= int(((n+k)/k))
#     return cat

# with open("C:\\Users\\felix\\Documents\\GitHub\\kattisproblem\\catalan\\catliststrings.txt", "w") as file:
#     #file.write("l = [")
#     for i in range(5001):
#         k = catalan(i)
#         print(k)
#         file.write(str(k) + ",\n")
#     #file.write("]")
#     #remember to remove last comma

# print("finished writing 5000 first catalan numbers to catlist.txt")
#-----------------------------------------
# # Table to store results of subproblems 
# catalan = [0 for i in range(5001)] 

# # Initialize first two values in table 
# catalan[0] = 1
# catalan[1] = 1

# # Fill entries in catalan[] using recursive formula 
# for i in range(2, 5001):
#     for j in range(i): 
#         catalan[i] = catalan[i] + catalan[j] * catalan[i-j-1] 
#         print(catalan[i])
#---------------------------------------------
queries = int(input())

cat = [0]*5001
cat[0] = 1
cat[1] = 1
catmax = 1

for _ in range(queries):
    q = int(input())
    if q > catmax:
        for n in range(catmax, q):
            cat[n+1] = (cat[n]*2*(2*n+1))//(n+2)
            catmax = q
            print(cat[n])