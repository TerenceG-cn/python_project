from math import *
# 误差,还没用上
delt=0.00000001
count=0
def distance(x, y):
    return pow(pow(x[0]-y[0],2)+pow(x[1]-y[1],2),0.5)

def similar(tr1,tr2):
    # a<b<c fixme
    if round(tr1[0]/tr2[0],10)==round(tr1[1]/tr2[1],10)==round(tr1[2]/tr2[2],10):
        return True
    else:
        # print(tr1[0]/tr2[0],tr1[1]/tr2[1],tr1[2]/tr2[2])
        return False


def fun(a,b,d):
    pl=[(x,a-x) for x in range(1,a)]
    for p in pl:
        if is_right((a,0),(b,0),(0,a),(0,d),p):
            print(a,b,d)
            return True

def is_right(a,b,c,d,p):
    ab=distance(a,b)
    ap=distance(a,p)
    cp=distance(c,p)
    bp=distance(b,p)
    dp=distance(d,p)
    bd=distance(d,b)
    cd=distance(c,d)
    tr_abp=sorted([ab,ap,bp])
    tr_cdp=sorted([cd,cp,dp])
    tr_bdp=sorted([bd,bp,dp])
    if similar(tr_abp,tr_bdp) and similar(tr_bdp,tr_cdp) and similar(tr_abp,tr_cdp):
        return True
    else: return False

count=0
for b in range(2,99_999):
    for d in range(2,100_000-b):
        m=min(b,d)
        for a in range(1,m):
            if fun(a,b,d):
                count+=1
print(count)