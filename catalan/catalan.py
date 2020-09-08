def catalan(n):
    cat = 1
    for k in range(2, n+1):
        cat *= int(((n+k)/k))
    return cat

with open("C:\\Users\\felix\\Documents\\GitHub\\competitive\\practice\\catalan\\catlist.txt", "w") as file:
    file.write("l = [")
    for i in range(5001):
        k = catalan(i)
        print(k)
        file.write(str(k) + ",\n")
    file.write("]")
    #remember to remove last comma

print("finished writing 5000 first catalan numbers to catlist.txt")