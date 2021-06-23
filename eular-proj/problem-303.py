def compare(n):
    # n=str(n)
    # for digital in n:
    #     if digital > '2':
    #         return False
    # return True
    l = [ int(item) for item in str(n) ]
    return max(l) <3

    

def f(n):
    tmp=n
    while not compare(tmp):
        print(tmp)
        tmp+=n
        
    print(n,tmp)
    return tmp

# sum=0
# for n in range(1,1001):
#     sum+=f(n)/n
# print(sum)
f(999)

# fixme 超时