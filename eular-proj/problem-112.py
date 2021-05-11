def isBouncy(n):
    if n<100:
        return False
    n=str(n)
    digs=[dig for dig in n]
    inc=digs[:]
    inc.sort()#上升数
    dec=digs[:]
    dec.sort(reverse=True)#下降数
    #print(digs,inc,dec)
    return digs!=inc and digs!=dec



cnt=0
n=100
flag=0.99
while True:
    if isBouncy(n):
        cnt+=1
    if cnt/n>=flag:
        print(n)
        break
    n+=1