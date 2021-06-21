# 博弈 异或
from math import pow
def solve(n):
    for i in range(1,n+1):
            if (n-i)^(2*n)^(3*n)==0:
                return 1
    for j in range(1,2*n+1):
            if n^(2*n-j)^(3*n)==0:
                return 1
    for k in range(1,3*n+1):
            if n^(2*n)^(3*n-k)==0:
                return 1
    return 0

count=0
for n in range(1,(int)(pow(2,30)+1)):
    if solve(n)==1:
        count+=1
print(count)
        
    
            