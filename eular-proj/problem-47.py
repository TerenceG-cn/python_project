import collections

# 偷来的质因数分解算法
def fun(num):
    res, prim = collections.defaultdict(int), 2
    while num > 1:
        if num % prim == 0:
            num //= prim
            res[prim] += 1
        else:
            prim += 1
    return res
size=100000000000000000
i=210 #有四个不同质因数的最小数
while i<size:
    if len(fun(i+3))<4: i+=4
    elif len(fun(i+2))<4: i+=3
    elif len(fun(i+1))<4: i+=2
    elif len(fun(i))<4: i+=1
    else:
        print(i,fun(i))
        print(i+1,fun(i+1))
        print(i+2,fun(i+2))
        print(i+3,fun(i+3))
        break