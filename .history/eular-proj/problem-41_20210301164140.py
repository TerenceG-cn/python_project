import math
from itertools import permutations


def is_prime(num):
    if num==1 or num==0:  return False
    i = 2
    while i <= int(pow(num, 0.5)):
        if num % i == 0: return False
        i += 1
    return True


MAX_FULL_NUM = "987654321"
for i in range(0, 9):
    for permu in permutations(MAX_FULL_NUM[i:]):
        num = int(''.join(permu))
        if is_prime(num):
            print(num)
