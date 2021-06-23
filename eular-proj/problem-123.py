# 纯粹的数学问题，下列方法overflow
from primesieve import *
from math import pow
n=7037
while True:
    pn=nth_prime(n)
    print(pn)
    remainder= (pow(pn-1,n)+pow(pn+1,n))%pow(pn,2)
    if remainder>pow(10,10):
        print(n)
        break
    else:
        n+=1