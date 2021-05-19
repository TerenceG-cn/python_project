from primesieve import *
from math import pow
print(nth_prime(7037))
n=7037
while True:
    pn=nth_prime(n)
    remainder= (pow(pn-1,2)+pow(pn+1,2))%pow(pn,2)
    if remainder>pow(10,10):
        print(n)
        break
    else:
        n+=1