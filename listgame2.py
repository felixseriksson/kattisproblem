'''
def gen(lista1, lista2, tobeat):
    tot = sum(lista1)
    if lista2 == []:
        lista2.append(0)
    else:
        i = 0
        while i >= len(lista1):
            i += 1
            if i == len(lista2)-1:
                lista2 = [0 for n in range(len(lista2))]
                break
            else:
                lista2[i] = lista2[i+1]+1
                for j in range(0, i):
                    lista2[j]= lista2[i]
    
    if tobeat >= (tot/len(lista2)):
        return tobeat
    g = 0
    notassign = False
    for i in range(len(lista2)):
        if lista1[lista2[i]] != 0:
            notassign = True
            g = []
        lista1[lista2[i]] -= 1
    if notassign == False:
        g = lista1
    if notassign == True:
        tobeat = 1 + gen(g, lista2, max(tobeat-1, 0))
    tobeat = gen(lista1, lista2, tobeat)
    return tobeat

n = int(input())
k = 0
composite = []
for p in range(2, int(n**0.5) + 1):
    apps = 0
    while n % p == 0:
        n /= p
        apps += 1
    if apps != 0:
        k += 1
        if apps != 1:
            composite.append(apps-1)
if n != 1:
    k += 1
    if len(composite) != 0: 
        k += gen(composite, [len(composite)], 0)
print(k)
'''
number = int(input())
k = 0
lista1 = []
for i in range(2, int(number**0.5)+1):
    if i > number:
        break
    occ = 0
    while number % i == 0:
        number /= i
        occ += 1
    if occ != 0:
        k += 1
    if occ > 1:
        lista1.append(occ-1)

if number != 1:
    k += 1
lista2 = [sum(lista1)]
if len(lista1) != 0:
    pass
    #öka k med gen
print(k)