import sys
import heapq
ja = False
if "heapq" in sys.modules:
    ja = True

perioderN = int(input())
superlista = []
for n in range(perioderN):
    superlista.append([float(char) for char in input().split()])

def multiplylist(lista):
    resultat = 1
    for x in lista:
        resultat = resultat*x
    return resultat

adjustedlista = []
for element in superlista:
    adjustedlista.append(multiplylist(element))

if ja == True:
    print(sum(adjustedlista))
elif ja == False:
    print("nej")