from typing import Iterator
import primesieve
import math 
import sys
import numpy as np


# 黄志斌 https://www.ituring.com.cn/article/132686?utm_source=tuicool

def a(n):
    it = primesieve.Iterator()
    
    if n<1: return None
    elif n==1:
        it.skipto(int(math.pow(10,14)))
        return it.next_prime()
    else: 
        it.skipto(a(n-1))
        return it.next_prime()


#快速幂解法
def f(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    base = [[1,1],[1,0]]
 
    n = n-2
    return base**(n-2)[0][0]
print(f(10))
#print(f(100000000000031))



def b(n):
    print(a(n))
    print('xiaole',f(a(n)))
    return f(a(n))

# print(f(2),f(3))
# sum=0
# for n in range(1,10):
#     print(b(n))
#     sum+=b(n)
# print(sum%1234567891011)
# print(f2(2),f2(3))
# print(f2(100000000000031))

#todo