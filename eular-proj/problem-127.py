import math
from sympy import *
from functions import gcd
def multiplyList(myList) :
    result = 1
    for x in myList:
         result = result * x  
    return result 
res=[]
size=120000
for c in range(3,size):
    for b in range(math.ceil(c/2),c):
        a=c-b
        if a<b<c and gcd(b,c)==1 and gcd(a,c)==1 and gcd(a,b)==1 and multiplyList(factorint(a*b*c))<c :
            print(a,b,c)
            res.append((a,b,c))
print(len(res))
print(sum(t[2] for t in res))
# todo overtime