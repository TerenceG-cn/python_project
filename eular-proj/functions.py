import math

def isPrime(n): 
  if n <= 1: 
    return False 
  for i in range(2, int(math.sqrt(n)) + 1): 
    if n % i == 0: 
        return False 
  return True 

def gcd(a, b):
    if a < b:
        a, b = b, a
    if a == 0 and b == 0:
        return 0
    while b != 0:
        c = a % b
        a, b = b, c
    return a

def digitCount(k, n):
    count=0
    while n>0:
        tmp=n%10
        if tmp==k: count+=1
        n=n//10
    return count

def digitCounts(n):
    count=[0]*10
    while n>0:
        tmp=n%10
        count[tmp]+=1
        n=n//10
    return count

# 欧拉函数
def eular_func(n):
    j=1
    for i in range(2,n):
        a=n
        q=i
        r=a%i
        while r!=1 and r!=0:
            a=int(q)
            q=int(r)
            r=int(a)%int(q)
        if r==1: j+=1
        elif r==0: pass
    return j