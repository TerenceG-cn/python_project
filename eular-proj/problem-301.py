# 博弈 异或 Nim game
from math import pow
def solve2(n):
    return n^(2*n)^(3*n)==0

size=int(pow(2,30))
count=0
for n in range(1,int(pow(2,30)+1)):
    if solve2(n):
        count+=1
print(count)

            