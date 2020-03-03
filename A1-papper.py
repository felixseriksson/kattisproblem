smallest, numbers, basarea, basomkrets, area, omkrets, broke = int(input()), [int(x) for x in input().split()], 1, 2*(((2**0.25)+(2**(-0.25)))), 0, 0, False
for size, amount in list(enumerate(numbers, 2)):
    area, omkrets = area + min(amount, ((0.5-area) // (2**(-size))))*basarea*((2**(size)))**(-1), omkrets + min(amount, ((0.5-area) // (2**(-size))))*basomkrets*(((2**(0.5))**size)**(-1))
    if area >= 0.5:
        broke = True
        break
if broke == False: print("impossible")
else: print((omkrets-(basomkrets*((2**0.5)**(-1))))/2)