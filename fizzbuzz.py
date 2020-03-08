lista = str(input()).split()

for n in range(1,int(lista[2])+1):
    if n % int(lista[1]) == 0 and n % int(lista[1]) == 0:
        print("FizzBuzz")
    elif n % int(lista[0]) == 0:
        print("Fizz")
    elif n % int(lista[1]) == 0:
        print("Buzz")
    else:
        print(n)