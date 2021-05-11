import math 
from functions import isPrime
from functions import digitCount
from functions import digitCounts
# M4d=[0]*10
# N4d=[0]*10
# S4d=[0]*10
# for n in range(1000,10000):
#     if isPrime(n):
#         cnts=digitCounts(n)
#         for i in range(0,10):
#             if cnts[i]>M4d[i]:
#                 M4d[i]=cnts[i]
#                 N4d[i]=1
#                 S4d[i]=n
#             elif cnts[i]==M4d[i]:
#                 N4d[i]+=1
#                 S4d[i]+=n

# print(M4d,N4d,S4d)
# print(sum(S4d))
from primesieve import *
M10d=[0]*10
N10d=[0]*10
S10d=[0]*10
for n in primes(1000_000_000, 10_000_000_000):
        cnts=digitCounts(n)
        for i in range(0,10):
            if cnts[i]>M10d[i]:
                M10d[i]=cnts[i]
                N10d[i]=1
                S10d[i]=n
            elif cnts[i]==M10d[i]:
                N10d[i]+=1
                S10d[i]+=n

print(M10d,N10d,S10d)
print(sum(S10d))
# [8, 9, 8, 9, 9, 9, 9, 9, 8, 9] [8, 11, 39, 7, 1, 1, 1, 9, 32, 8] [38000000042, 12882626601, 97447914665, 23234122821, 4444444447, 5555555557, 6666666661, 59950904793, 285769942206, 78455389922]
# 612407567715