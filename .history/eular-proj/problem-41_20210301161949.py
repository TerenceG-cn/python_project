import math
from itertools import permutations

for permu in permutations("987654321"):
    print(permu)

def isPrime(num):
    i=2
    while i<=int(pow(num,0.5)):
        if num%i==0: return False
    return True
