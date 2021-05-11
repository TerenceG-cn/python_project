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

n=1473274927421111122312111
print(digitCount(1,n))
print(digitCounts(n))
