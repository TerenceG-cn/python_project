from typing import Iterator
import primesieve
import math 
import sys

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

def f(n):
    if n==0: return 0
    elif n==1: return 1
    else:
        last, last_last = 1, 1
        for i in range(n-1):
            last, last_last = last_last, last + last_last
    return last_last


def fib_yield_while(max):
    a, b = 0, 1
    while max > 0:
    	a, b = b, (a + b)%1234567891011
    	max -= 1
    	yield a
        
def fib_yield_for(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b)%1234567891011
        yield a

iterator=fib_yield_for(100000000000031)
while True:
    try:
        res=next(iterator)
    except StopIteration:
        print(res)
        sys.exit()

# iterator=fib_yield_for(31)
# for i in iterator:
#     if not next(iterator):
#         print(i%1234567891011)

# print(a(1)) #100000000000031

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