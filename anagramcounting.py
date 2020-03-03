from math import factorial
from collections import Counter
import sys

for word in sys.stdin:
    word = word.strip("\n")
    length = len(word)
    t = factorial(length)
    freq = dict(Counter(word))
    for occ in freq.values():
        t //= int(factorial(occ))
    print(int(t))