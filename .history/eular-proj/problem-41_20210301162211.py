import math
from itertools import permutations

def is_prime(num):
    i=2
    while i<=int(pow(num,0.5)):
        if num%i==0: return False
        i+=1
    return True

for permu in permutations("987654321"):
    num=int(''.join(permu))
    if is_prime(num):
        print(num)


