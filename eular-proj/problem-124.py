from operator import itemgetter, attrgetter 
from sympy import *
def multiplyList(myList) :
    result = 1
    for x in myList:
         result = result * x  
    return result 
class Num:
    def __init__(self, n, rad_n, k):  
        self.n = n 
        self.rad = rad_n  
        self.k = k
    def __repr__(self):  
        return repr((self.n, self.rad, self.k))  

# Nums=[
#     Num(1,1,0),
#     Num(2,2,0),
#     Num(3,3,0),
#     Num(4,2,0),
#     Num(5,5,0),
#     Num(6,6,0),
#     Num(7,7,0),
#     Num(8,2,0),
#     Num(9,3,0),
#     Num(10,10,0)
# ]
n=100000
k=10000
Nums=[ Num(i,multiplyList(factorint(i).keys()),0) for i in range(1,n+1)]
E=sorted(Nums,key=attrgetter('rad', 'n'))
for i in range(0,n):
    E[i].k=i+1
print(E[k-1].n)