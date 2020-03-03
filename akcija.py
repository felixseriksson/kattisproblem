'''
books = int(input())
booklist = []
for n in range(books):
    booklist.append(int(input()))
booklist.sort(reverse=True)
pricecounter = 0
for price in list(enumerate(booklist,)):
    if price[0] % 3 != 2:
        pricecounter += price[1]

print(pricecounter)
'''
print(sum([num for index, num in list(enumerate(sorted([int(input()) for n in range(int(input()))], reverse=True))) if index % 3 != 2]))