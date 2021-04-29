def is_right(n):
    n=str(n)
    return set(n[0:9])==set('123456789') and set(n[-10:-1])==set('123456789')
        
a=b=1
k=3
while True :
    a,b=b,a+b
    if b>pow(10,9) and is_right(b):
        print(k)
        print(b)
        break
    k+=1